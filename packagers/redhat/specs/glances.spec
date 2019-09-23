Summary:		Glances - An eye on your system
Name:			glances
Version:		2.5.1
Release:		1%{?dist}
License:		GPLv2
URL:			https://github.com/nicolargo/glances
Source0:		https://github.com/nicolargo/glances/archive/glances-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel
Requires:		python-psutil
Requires:		python-logutils
Requires:		python-setuptools

%description
Glances is a cross-platform curses-based system monitoring tool written in Python.

%prep
%setup -q -n glances-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/glances
/usr/share/
%{python_sitelib}/glances
%{python_sitelib}/Glances-%{version}-py2.*.egg-info

%changelog
* Tue Nov 24 2015 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 2.5.1
- Initial spec with glances-2.5.1 version.
