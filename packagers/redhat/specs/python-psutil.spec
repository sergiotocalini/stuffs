Summary:		A cross-platform process and system utilities module for Python
Name:			python-psutil
Version:		3.2.2
Release:		1%{?dist}
License:		GPLv2
URL:			https://github.com/giampaolo/psutil
Source0:		https://github.com/giampaolo/psutil/archive/psutil-release-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		x86_64
BuildRequires:		python-devel

%description
psutil (python system and process utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes. It implements many functionalities offered by command line tools such as: ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap. It currently supports Linux, Windows, OSX, FreeBSD, OpenBSD and Sun Solaris, both 32-bit and 64-bit architectures, with Python versions from 2.6 to 3.5 (users of Python 2.4 and 2.5 may use 2.1.3 version). PyPy is also known to work.

%prep
%setup -q -n psutil-release-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitearch}/psutil
%{python_sitearch}/psutil-%{version}-py2.*.egg-info

%changelog
* Tue Nov 24 2015 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 3.2.2
- Initial spec with python-psutil-3.2.2 version.
