Summary:		My Own SMTP Server
Name:			moSMTPD
Version:		1.0.0
Release:		1
License:		GPL v2+
Group:			Applications/Admin
URL:			http://planning.corpam.com.ar/
Source0:		%{name}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
BuildArch:		noarch
Requires:		python python-daemon python-gammu

%description
My Own SMTP Server transform E-MAIL messages to SMS messages.

%pre
/usr/bin/getent -s files group services &> /dev/null || /usr/sbin/groupadd -r -g 1002 services &> /dev/null
/usr/bin/getent -s files passwd mosmtpd &> /dev/null || /usr/sbin/useradd -r -d /opt/mosmtpd -s /sbin/nologin -g services -c "My Own SMTPD" -u 706 mosmtpd &> /dev/null
exit 0

%preun
/sbin/service mosmtpd stop &> /dev/null
/sbin/chkconfig --del mosmtpd &> /dev/null

%post
/sbin/chkconfig --level 0123456 mosmtpd off

%postun
/usr/bin/getent -s files passwd mosmtpd && /usr/sbin/userdel mosmtpd

%build

%clean

%files
%defattr(775,mosmtpd,services,775)
%attr(755,mosmtpd,services)	/opt/mosmtpd
%config(noreplace)              %attr(755,mosmtpd,services)  /etc/init.d/mosmtpd

%changelog
* Wed Feb 18 2015  <sergiotocalini@gmail.com> - mosmtpd-1.0.0
- Initial build.

