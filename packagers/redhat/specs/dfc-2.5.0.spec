Summary:		A simple CLI tool that display file system usage, with colors
Name:			dfc
Version:		2.5.0
Release:		1%{?dist}
License:		GPL v2+
Group:			Applications/Admin
Source0:		http://projects.gw-computing.net/attachments/download/42/%{name}-%{version}.tar.gz
URL:			http://projects.gw-computing.net/projects/dfc
BuildRequires:		gcc
BuildRoot:		%{_tmppath}/%{name}-%{version}-root

%define _prefix		/usr/local
%define _bindir		%{_prefix}/bin
%define _mandir		%{_prefix}/man

%description
A simple CLI tool that display file system usage, with colors

%prep

%setup -q

%build

%{__make} PREFIX="$RPM_BUILD_ROOT%{_prefix}" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)		%{_bindir}/dfc
%attr(755,root,root)		%{_mandir}/man1/dfc.1*

%changelog
* Wed Jun 12 2013 Initial Commit
*  Sergio Tocalini Joerg <sergiotocalini@gmail.com>

Revision 1.0 2013/06/12 00:00:00 Sergio Tocalini Joerg <sergiotocalini@gmail.com>
- Complete RPM Spec file for DFC 2.0.5 for RedHat.
