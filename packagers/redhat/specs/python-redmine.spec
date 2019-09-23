Summary:		A library for communicating with a Redmine project management
Name:			python-redmine
Version:		0.8.2
Release:		1%{?dist}
License:		GPLv2
URL:			https://github.com/maxtepkeev/python-redmine
Source0:		https://github.com/maxtepkeev/python-redmine/archive/python-redmine-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel


%description
Python Redmine is a library for communicating with a Redmine project management application. Redmine exposes some of it's data via REST API for which Python Redmine provides a simple but powerful Pythonic API inspired by a well-known Django ORM.

%prep
%setup -q -n python-redmine-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/redmine
%{python_sitelib}/python_redmine-%{version}-py2.*.egg-info

%changelog
* Fri Jul 4 2014 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.8.2
- Initial spec with python-redmine-0.8.2 version.
