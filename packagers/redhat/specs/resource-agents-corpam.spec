Name:			resource-agents-corpam
Version:		9999
Release:		2%{?dist}
License:		GPLv2
Summary:		OCF resource agent for CA
Group:			System Environment/Base
URL:			http://planning.corpam.com.ar/
BuildArch:		noarch
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		resource-agents

%description
This package contains the OCF-compliant resource agents for CA.

%clean

%files
%defattr(755,root,root,-)
%dir		/usr/lib/ocf/resource.d/corpam
		/usr/lib/ocf/resource.d/corpam/*
%dir		/usr/lib/ocf/lib/corpam
		/usr/lib/ocf/lib/corpam/*
		

%changelog
* Mon Nov 17 2014  <sergiotocalini@gmail.com> - resource-agents-corpam-9999-2
- Checkout from http://sources.corpam.com.ar/subversion/unix/scripts/pacemaker/ - revision 1039.

* Thu Jun 26 2014  <sergiotocalini@gmail.com> - resource-agents-corpam-9999-1
- Checkout from http://sources.corpam.com.ar/subversion/unix/scripts/pacemaker/ - revision 807.
