Summary:		Gunicorn: Python WSGI HTTP Server for UNIX.
Name:			python-gunicorn
Version:		19.4.5
Release:		1%{?dist}
License:		GPLv2
URL:			http://gunicorn.org/
Source0:		http://pypi.python.org/packages/source/g/gunicorn/gunicorn-%{version}.tar.gz
Group:			Development/Languages
BuildArch:		noarch
BuildRequires:		python-devel
Requires:		python-devel
Requires:		python-virtualenv
Requires:		python-setuptools

%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn project. The Gunicorn server is broadly
compatible with various web frameworks, simply implemented, light on server
resource usage, and fairly speedy.

%clean

%prep
%setup -q -n gunicorn-%{version}
/usr/bin/getent -s files group webapps &> /dev/null || /usr/sbin/groupadd -r -g 1001 webapps &> /dev/null
/usr/bin/getent -s files passwd python &> /dev/null || /usr/sbin/useradd -r -d /mnt/webapps/pyadm -s /bin/bash -g webapps -c "Python User" -u 603 python &> /dev/null
exit 0

%preun
/sbin/service gunicorn stop &> /dev/null
/sbin/chkconfig --del gunicorn &> /dev/null

%post
/sbin/chkconfig --level 345 gunicorn on
/sbin/service gunicorn start &> /dev/null

%build
%{__python} setup.py build
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
							%{python_sitelib}/*
							/etc/init.d/*
							/etc/gunicorn.d/*
%config(noreplace)	%attr(755,root,root)		/etc/gunicorn.conf
			%attr(775,python,webapps)	/var/log/gunicorn
			%attr(755,-,-)			/usr/bin/*

%changelog
* Fri Jan 20 2016 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 19.4.5-r1
- Initial spec with python-gunicorn-19.4.5 version.
