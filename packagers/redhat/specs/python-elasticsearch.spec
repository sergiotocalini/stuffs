Summary:		Official low-level client for Elasticsearch.
Name:			python-elasticsearch
Version:		1.1.1
Release:		1%{?dist}
License:		GPLv2
URL:			http://www.elasticsearch.org/
Source0:		https://github.com/elasticsearch/elasticsearch-py/archive/elasticsearch-py-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel

%description
Official low-level client for Elasticsearch. Its goal is to provide common ground for all Elasticsearch-related code in Python; because of this it tries to be opinion-free and very extendable.

%prep
%setup -q -n elasticsearch-py-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/elasticsearch
%{python_sitelib}/elasticsearch-%{version}-py2.*.egg-info

%changelog
* Thu Jul 10 2014 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 1.1.1-r1
- Initial spec with python-es-1.1.1 version.
