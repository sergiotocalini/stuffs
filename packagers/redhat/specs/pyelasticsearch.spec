Summary:		pyelasticsearch is a clean, future-proof, high-scale API to elasticsearch
Name:			pyelasticsearch
Version:		0.6.1
Release:		1%{?dist}
License:		GPLv2
URL:			http://www.elasticsearch.org/
Source0:		https://github.com/rhec/pyelasticsearch/archive/pyelasticsearch-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel

%description
pyelasticsearch is a clean, future-proof, high-scale API to elasticsearch. It provides features like...
Transparent conversion of Python data types to and from JSON
Translating HTTP status codes representing failure into exceptions
Connection pooling
Load-balancing of requests across nodes in a cluster
Failed-node marking to avoid downed nodes for a period
Optional automatic retrying of failed requests

%prep
%setup -q -n pyelasticsearch-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/pyelasticsearch
%{python_sitelib}/pyelasticsearch-%{version}-py2.*.egg-info

%changelog
* Thu Jul 10 2014 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.6.1-r1
- Initial spec with pyelasticsearch-0.6.1 version.
