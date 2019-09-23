Summary:		Logstash shipper to centralized information about the systems.
Name:			logstash
Version:		1.3.3
Release:		1
License:		GPL v2+
Group:			Applications/Admin
URL:			http://logstash.net
Source0:		%{name}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
BuildArch:		noarch
Requires:		java-1.7.0-openjdk java-1.7.0-openjdk-devel tzdata-java

%description
Logstash shipper to centralized information about the systems.

%pre
/usr/bin/getent -s files group webapps &> /dev/null || /usr/sbin/groupadd -r -g 1001 webapps &> /dev/null
/usr/bin/getent -s files passwd logstash &> /dev/null || /usr/sbin/useradd -r -d /mnt/logstash -s /sbin/nologin -g webapps -c "Logstash User" -u 505 logstash &> /dev/null
exit 0

%preun
/sbin/service logstash-sh stop &> /dev/null
/sbin/chkconfig --del logstash-sh &> /dev/null
/sbin/service logstash stop &> /dev/null
/sbin/chkconfig --del logstash &> /dev/null

%post
/sbin/chkconfig --level 0123456 logstash off
/sbin/chkconfig --level 0123456 logstash-sh off

%postun
/usr/bin/getent -s files passwd logstash && /usr/sbin/userdel logstash

%build

%clean

%files
%defattr(775,logstash,webapps,775)
%attr(755,logstash,webapps)	/mnt/logstash/bin
%attr(755,logstash,webapps)	/mnt/logstash/data
%attr(755,logstash,webapps)	/mnt/logstash/logs
%config(noreplace)              %attr(755,logstash,webapps)  /mnt/logstash/conf
%config(noreplace)              %attr(755,logstash,webapps)  /etc/init.d/logstash
%config(noreplace)              %attr(755,logstash,webapps)  /etc/init.d/logstash-sh
%config(noreplace)              %attr(644,logstash,webapps)  /etc/logrotate.d/logstash
%config(noreplace)              %attr(644,logstash,webapps)  /etc/logrotate.d/logstash-sh
%config(noreplace)		%attr(644,logstash,webapps)  /etc/logstash

%changelog
* Thu May 29 2014  <sergiotocalini@gmail.com> - logstash-1.3.3
- Initial build.

