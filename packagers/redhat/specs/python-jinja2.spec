Summary:		Jinja2 is a template engine written in pure Python.
Name:			python-jinja2
Version:		2.7.3
Release:		1%{?dist}
License:		GPLv2
URL:			https://github.com/mitsuhiko/jinja2/
Source0:		https://github.com/mitsuhiko/jinja2/archive/python-jinja2-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel

%description
Jinja2 is a template engine written in pure Python. It provides a Django inspired non-XML syntax but supports inline expressions and an optional sandboxed environment.

%prep
%setup -q -n jinja2-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/jinja2
%{python_sitelib}/Jinja2-%{version}*-py2.*.egg-info

%changelog
* Thu Jul 17 2014 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 2.7.3-1
- Initial spec with python-jinja2-2.7.3 version.
