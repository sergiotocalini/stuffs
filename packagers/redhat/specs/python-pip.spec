Summary:		A tool for installing and managing Python packages.
Name:			python-pip
Version:		1.5.6
Release:		1%{?dist}
License:		GPLv2
URL:			https://github.com/pypa/pip
Source0:		https://github.com/pypa/pip/archive/python-pip-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel

%description
A tool for installing and managing Python packages.

%prep
%setup -q -n pip-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
				%{python_sitelib}/pip
				%{python_sitelib}/pip-%{version}-py2.*.egg-info
%attr(755,-,-)			/usr/bin/*

%changelog
* Mon Jul 21 2014 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 1.5.6-1
- Initial spec with python-pip-1.5.6 version.
