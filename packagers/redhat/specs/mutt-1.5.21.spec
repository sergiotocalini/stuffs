Summary:		A text mode mail user agent
Name:			mutt
Version:		1.5.21
Release:		1%{?dist}
License: 		GPLv2+ and Public Domain
Group: 			Applications/Internet
URL: 			ftp://ftp.mutt.org/pub/mutt/devel/mutt-%{version}.tar.gz
Source0:		%{name}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%define _unpackaged_files_terminate_build	0

%description
Mutt is a small but very powerful text-based MIME mail client.  Mutt
is highly configurable, and is well suited to the mail power user with
advanced features like key bindings, keyboard macros, mail threading,
regular expression searches and a powerful pattern matching language
for selecting groups of messages.

%prep
%setup -q
%build
%configure --prefix=/usr \
	   --enable-smtp \
	   --with-gss \
	   --with-regex \
	   --with-sasl \
	   --with-ssl

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,644)
%{_mandir}/*
%{_docdir}/*
%{_datadir}/locale/es/*
%{_datadir}/locale/pt_BR/*
%{_sysconfdir}/Muttrc*
%attr(755,root,root)	%{_bindir}/*

%changelog
* Wed Aug 14 2013 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 1.5.21-1
- Initial spec with mutt-1.5.21 version.
