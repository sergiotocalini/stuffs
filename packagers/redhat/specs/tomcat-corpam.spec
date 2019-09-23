Name:			tomcat-corpam
Version:		8.0.28
Release:		1
License:		Apache Software License
Summary:		Apache Tomcat release for Corporacion America
Group:			Networking/Daemons
URL:			http://tomcat.apache.org/
BuildArch:		noarch
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
Source:			apache-tomcat-%{version}.tar.gz
Requires:		jdk

%description
This package contains the apache-tomcat container by Corporacion America.

%clean

%pre
/usr/bin/getent -s files group webapps &> /dev/null || /usr/sbin/groupadd -r -g 1001 webapps &> /dev/null
/usr/bin/getent -s files passwd tomcat &> /dev/null || /usr/sbin/useradd -r -d /mnt/webapps/apache-tomcat -s /bin/bash -g webapps -c "Tomcat User" -u 501 tomcat &> /dev/null
exit 0

%post
/sbin/chkconfig --level 345 tomcat on
/bin/ln -sf /mnt/webapps/apache-tomcat-%{version} /mnt/webapps/apache-tomcat

%postun
/bin/unlink /mnt/webapps/apache-tomcat
/usr/bin/getent -s files passwd tomcat && /usr/sbin/userdel tomcat

%files
%defattr(755,tomcat,webapps,-)
%config(noreplace)	%attr(755,root,root)		/etc/profile.d/java.sh
%config(noreplace)	%attr(755,root,root)		/etc/profile.d/tomcat.sh
%config(noreplace)	%attr(755,root,root)		/etc/init.d/tomcat
%config(noreplace)    	%attr(755,root,root)		/etc/logrotate.d/tomcat
%dir							/mnt/webapps/apache-tomcat-%{version}/
							/mnt/webapps/apache-tomcat-%{version}/*

%changelog
* Fri Oct 23 2015  <sergiotocalini@gmail.com> - tomcat-corpam-8.0.28-1
- Check this out from more information http://planning.corpam.com.ar/proden-unix/wiki/Java#Tomcat.
