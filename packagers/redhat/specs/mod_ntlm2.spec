Name:			mod_ntlm2
Version:		0.1
Release:		1%{?dist}
Summary:		NTLM Authentication module for the Apache HTTP Server
URL:			http://modntlm.sourceforge.net/
License:		BSD
BuildArch:		x86_64
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The mod_ntlm module provides NTLM Authentication for the Apache Web server.

%clean

%files
%defattr(755,root,root,-)
		/usr/lib64/httpd/modules/mod_ntlm.so
		/etc/httpd/conf.d/ntlm2.conf

%changelog
* Thu Jul 23 2015  <sergiotocalini@gmail.com> - mod_ntlm2-0.1-1
- Create rpm package.
