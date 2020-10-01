#!/usr/bin/env python
import os
import ldap
import sys
import time
from hashlib import md5


def error(message, **kwargs):
    """
    Errors must create non-zero status codes and human-readable, ideally one-line, messages on stderr.
    """
    print(message, file=kwargs.get("file", sys.stderr))
    sys.exit(kwargs.get("code", 1))


def ensure_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)

        
def avatar_sync(**kwargs):
    kwargs.set_default("attrs", ["mail", "jpegPhoto"])
    kwargs.set_default("filter", "(&(jpegPhoto=*))")
    kwargs.set_default("map-index", "mail")
    kwargs.set_default("map-value", "jpegPhoto")
    kwargs.set_default("scope", ldap.SCOPE_SUBTREE)
    required = ["uri", "bind-dn", "bind-pw", "base-dn"]
    for r in required:
        if not kwargs.get(r, False):
            error("Parameter {0}: is missing".format(r))
    cstr = ldap.initialize(kwargs["uri"])
    cstr.simple_bind_s(kwargs["bind-dn"], kwargs["bind-pw"])
    cstr.set_option(ldap.OPT_REFERRALS, 0)
    res = cstr.search_ext(
        kwargs["basedn"], kwargs["scope"], kwargs["filter"], kwargs["attrs"]
    )
    while 1:
        result_type, result_data = cstr.result(res, 0)
        if (result_data == []):
            break
        else:
            if result_type == ldap.RES_SEARCH_ENTRY:
                index = result_data[0][1][kwargs["map-index"]][0].encode('utf-8')
                value = result_data[0][1][kwargs["map-value"]][0]
                filename = md5(index).hexdigest()
                archive = open(filename, 'w')
                archive.write(value)
                archive.close()
                for i in result_data[0][1][kwargs["map-index"]][1:]:
                    os.symlink(filename, md5(i).hexdigest())
    cstr.unbind()
    return output


def main(**kwargs):
    output = avatar_sync(**kwargs)
        
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config",
                      default=None,
                      help="Configuration file")
    parser.add_option("-u", "--uri", dest="uri",
                      default=None,
                      help="LDAP Server URI")
    parser.add_option("--bind-dn", dest="bind-dn",
                      default=None,
                      help="LDAP Bind DN")
    parser.add_option("--bind-pw", dest="bind-pw",
                      default=None,
                      help="LDAP Bind PW")
    parser.add_option("--base-dn", dest="base-dn",
                      default=None,
                      help="LDAP Base DN")
    parser.add_option("--scope", dest="scope",
                      default=ldap.SCOPE_SUBTREE,
                      help="LDAP Search Scope")
    parser.add_option("--filter", dest="filter",
                      default='(&(jpegPhoto=*))',
                      help="LDAP Search Filter")
    parser.add_option("--attrs", dest="attrs",
                      default="mail,jpegPhoto",
                      help="LDAP Search Attributes", metavar="list")
    parser.add_option("--map-index", dest="map-index",
                      default="mail", metavar="str",
                      help="LDAP Mapping Index")
    parser.add_option("--map-value", dest="map-value",
                      default="jpegPhoto", metavar="str",
                      help="LDAP Mapping Value")
    parser.add_option("-o", "--outdir", dest="outdir",
                      default=None, metavar="str",
                      help="Specify the domain.")
    (opts, args) = parser.parse_args()
    params = vars(opts)
    main(**params)
