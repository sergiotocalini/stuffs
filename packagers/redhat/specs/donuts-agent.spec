Name:			donuts-agent
Version:		0.1.0
Release:		1
License:		GPLv3
Summary:		Donuts Agent for Corporacion America
Group:			Networking/Daemons
URL:			http://planning.corpam.com.ar/projects/donuts
BuildArch:		noarch
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		python-pip
Requires:		python-flask
Requires:		python-setuptools

%description
This package contains the donuts agent container by Corporacion America.

%clean

%pre
/usr/bin/getent -s files group webapps &> /dev/null || /usr/sbin/groupadd -r -g 1001 webapps &> /dev/null
/usr/bin/getent -s files passwd python &> /dev/null || /usr/sbin/useradd -r -d /mnt/webpps/pyadm -s /bin/bash -g webapps -c "Python User" -u 603 python &> /dev/null
exit 0

%post
/bin/ln -sf /mnt/webapps/pyadm/donuts_agent-%{version} /mnt/webapps/pyadm/donuts_agent

%files
%defattr(755,tomcat,webapps,-)
%config(noreplace)	%attr(755,root,root)		/etc/gunicorn.d/donuts_agent.conf
%dir							/mnt/webapps/pyadm/donuts_agent-%{version}/
							/mnt/webapps/pyadm/donuts_agent-%{version}/*
%changelog
* Mon Dec 28 2015 <sergiotocalini@gmail.com> - donuts-agent-0.1.0-1
- Check this out from more information http://planning.corpam.com.ar/projects/donuts.
