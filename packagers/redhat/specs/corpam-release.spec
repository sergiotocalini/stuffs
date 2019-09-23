Name:			corpam-release
Version:		1.0
Release:		1.el7
License:		GPLv2
Summary:		Corporacion America release
Group:			System Environment/Base
URL:			http://planning.corpam.com.ar/proden-unix/wiki/RedHat
BuildArch:		noarch
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		linux_logo

%description
This package contains the Corporacion America banners and others stuff.

%clean

%files
%defattr(755,root,root,-)
                /etc/BASH_COLORS
                /etc/profile.d/corpam.sh
                /etc/linux_logo.conf
%dir		/etc/linux_logo/
		/etc/linux_logo/*
		/etc/cron.hourly/issue-maker

%changelog
* Mon Oct 5 2015  <sergiotocalini@gmail.com> - corpam-relase-1.0-1
- Check this out from more information http://planning.corpam.com.ar/proden-unix/wiki/RedHat.
