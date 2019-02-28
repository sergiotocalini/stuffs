#!/usr/bin/env python
import os
import ldap
from hashlib import md5

LDAP_HOST = 'ldap://ldap.amana.vpn:389'
LDAP_BINDDN = 'cn=binduser,ou=auth,dc=amana,dc=vpn'
LDAP_BINDPW = 'BxoANIdpvoB325jA2pdG'
LDAP_BASEDN = 'ou=people,dc=amana,dc=vpn'
LDAP_SCOPE = ldap.SCOPE_SUBTREE
LDAP_FILTER = '(&(jpegPhoto=*))'
LDAP_ATTRS = ['mail', 'jpegPhoto']

def export_photos(output, **kwargs):
    cstr = ldap.initialize(LDAP_HOST)
    cstr.simple_bind_s(LDAP_BINDDN, LDAP_BINDPW)
    cstr.set_option(ldap.OPT_REFERRALS, 0)
    res = cstr.search_ext(LDAP_BASEDN, LDAP_SCOPE, LDAP_FILTER, LDAP_ATTRS)
    while 1:
        result_type, result_data = cstr.result(res, 0)
        if (result_data == []):
            break
        else:
            if result_type == ldap.RES_SEARCH_ENTRY:
                mail = result_data[0][1]['mail'][0].encode('utf-8')
                jpeg = result_data[0][1]['jpegPhoto'][0]
                filename = md5(mail).hexdigest()
                archive = open(filename, 'w')
                archive.write(jpeg)
                archive.close()
                for i in result_data[0][1]['mail'][1:]:
                    os.symlink(filename, md5(i).hexdigest())
    cstr.unbind()
    return output

def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-o", "--outdir", dest="outdir", default=None,
                      help="Specify the domain.", metavar="str")
    parser.add_option("-f", "--fields", dest="fields", default="ip,host",
                      help="Display fields (ip, name, type).",
                      metavar="list")
    parser.add_option("-r", "--regex", dest='regex', default='.*',
                      help="Regular Expression.", metavar="str")
    parser.add_option("-s", "--server", dest="server", default=None,
                      help="DNS Server", metavar="str")
    parser.add_option("-t", "--type", dest="rtype", default="A,CNAME",
                      help="Type filter", metavar="list")
    parser.add_option("-D", "--delimiter", dest="delimiter", default="\t",
                      help="Delimiter", metavar="str")
    (options, args) = parser.parse_args()

    server = options.server if options.server else get_default_resolver('nameserver')
    domain = options.domain if options.domain else get_default_resolver('domain')
    if domain and server:
        options = {
            'server': server, 'domain': domain,
            'type': [t.upper() for t in options.rtype.split(",")],
            'regex': options.regex,
            'delimiter': options.delimiter,
            'fields': [f.lower() for f in options.fields.split(",")]
        }
        DNSAdmin = DNSQuery(options['server'])
        Records = DNSAdmin.get_records(**options)
        DNSAdmin.display_output(Records, options['fields'], 
                                options['delimiter'])
    else:
        print("DNSQuery: Required arguments missing or invalid.")
        print(parser.print_help())
        sys.exit(-1)

if __name__ == '__main__':
    main()
