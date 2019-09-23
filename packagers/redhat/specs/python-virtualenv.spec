Summary:		Tool to create isolated Python environments
Name:			python-virtualenv
Version:		13.1.2
Release:		1%{?dist}
License:		MIT
URL:			http://pypi.python.org/pypi/virtualenv
Source0:		http://pypi.python.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel
Requires:		python-setuptools
Requires:		python-devel
Requires:		python-gunicorn

%description
virtualenv is a tool to create isolated Python environments. virtualenv
is a successor to workingenv, and an extension of virtual-python. It is
written by Ian Bicking, and sponsored by the Open Planning Project. It is
licensed under an MIT-style permissive license.

%prep
%setup -q -n virtualenv-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
				%{python_sitelib}/*
%attr(755,-,-)			/usr/bin/*

%changelog
* Fri Jan 20 2016 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 13.1.2-r1
- Initial spec with python-virtualenv-13.1.2 version.
