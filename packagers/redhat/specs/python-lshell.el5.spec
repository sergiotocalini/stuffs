Summary:		lshell is a shell coded in Python.
Name:			python-lshell
Version:		0.9.16
Release:		1.el5
License:		GPLv2
URL:			https://github.com/ghantoos/lshell
Source0:		https://github.com/ghantoos/lshell/releases/download/0.9.16/lshell-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)

%description
lshell is a shell coded in Python, that lets you restrict a user's environment to limited sets of commands, choose to enable/disable any command over SSH (e.g. SCP, SFTP, rsync, etc.), log user's commands, implement timing restriction, and more.

%prep
%setup -q -n lshell-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
                        /etc
                        /usr/share
                        /usr/lib/python2.4/site-packages/lshell
%attr(755,-,-)          /usr/bin


%changelog
* Tue Sep 23 2014 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 0.9.16-r1
- Initial spec with python-lshell-0.9.16 version.
