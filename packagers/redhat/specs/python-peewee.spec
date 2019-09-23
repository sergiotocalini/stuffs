Summary:		Peewee: a small, expressive orm
Name:			python-peewee
Version:		2.2.5
Release:		1%{?dist}
License:		GPLv2
URL:			https://github.com/coleifer/peewee
Source0:		https://github.com/coleifer/peewee/archive/peewee-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel

%description
A small, expressive orm

%prep
%setup -q -n peewee-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
				%{python_sitelib}/peewee*
				%{python_sitelib}/peewee-%{version}-py2.*.egg-info
				%{python_sitelib}/playhouse
				%{python_sitelib}/pwiz*
%attr(755,-,-)			/usr/bin/pwiz.py

%changelog
* Fri Jul 11 2014 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 2.2.5-r1
- Initial spec with python-peewee-2.2.5 version.
