Summary:		Pacemaker Configuration System
Name:			pcs
Version:		0.9.115
Release:		1%{?dist}
License:		GPLv2
BuildArch:		noarch
URL:			http://github.com/feist/pcs
Source0:		https://codeload.github.com/feist/pcs/tar.gz/pcs-%{version}.tar.gz
Group:			System Environment/Base
BuildRequires:		pam-devel
BuildRequires:		python2-devel
Requires:		pacemaker

%description
pcs is a corosync and pacemaker configuration tool. It permits users to easily view, modify and created pacemaker based clusters.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT PYTHON_SITELIB=%{python_sitelib}
chmod 755 $RPM_BUILD_ROOT/%{python_sitelib}/pcs/pcs.py

%files
%defattr(-,root,root,-)
/etc/bash_completion.d/pcs
%{python_sitelib}/pcs
%{python_sitelib}/pcs-%{version}-py2.*.egg-info
/usr/sbin/pcs
/usr/share/man/man8/pcs.8.gz

%doc COPYING README

%changelog
* Wed Apr 15 2014 - Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.9.115-1
- Update package version

* Tue Jan 14 2014 - Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.9.105-1
- Update package version

* Mon Jan 6 2014 - Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.9.103-1
- Update package version

* Tue Dec 17 2013 - Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.9.102-1
- Update package version

* Tue Jul 23 2013 - Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.9.54-1
- Initial spec with pcs-0.9.54 version
