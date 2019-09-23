Summary:                                    Mobile phone management utility
License:                                    GPL-2.0
Group:                                      Applications/Communications
Vendor:                                     Michal Čihař <michal@cihar.com>
Name:                                       gammu
Version:                                    1.34.0
Release:                                    1.el6

# Python name
%{!?__python: %define __python python}
%define g_python_sitearch                   %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")
%define g_python_major_version              %(%{__python} -c 'import sys; print sys.version.split(" ")[0][:3]')
%define gammu_docdir                        %_docdir/%{name}-%{version}

BuildRequires:                              bluez-libs-devel >= 2.0
BuildRequires:                              mysql-devel
BuildRequires:                              libdbi-devel libdbi-dbd-sqlite sqlite
BuildRequires:                              unixODBC-devel
BuildRequires:                              libgudev1-devel glib2-devel
BuildRequires:                              python-devel
BuildRequires:                              curl-devel
BuildRequires:                              libcurl-devel
BuildRequires:                              libusb1-devel
BuildRequires:                              gettext cmake pkgconfig gcc

Source:                                     http://dl.cihar.com/gammu/releases/gammu-%{version}.tar.bz2
URL:                                        http://wammu.eu/gammu/
BuildRoot:                                  %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains Gammu binary as well as some examples.

%package devel
Summary:            Development files for Gammu
Group:              Development/Libraries
Requires:           %{name} = %{version}-%{release} pkgconfig

%description devel
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contain files needed for development.

%package -n python-gammu
Summary:            Python module to communicate with mobile phones
Group:              Development/Languages
Requires:           python >= %{g_python_major_version}, python < %{g_python_major_version}.99
%{?py_requires}

%description -n python-gammu
This provides gammu module, that can work with any phone Gammu
supports - many Nokias, Siemens, Alcatel, ...

%package smsd
Summary:            SMS message daemon
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts
Group:              Applications/Communications

%description smsd
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains Gammu SMS Daemon and tool to inject messages
into the queue.

%package -n libGammu7
Summary:            Mobile phone management library
Group:              System/Libraries

%description -n libGammu7
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains Gammu shared library.

%package -n libgsmsd7
Summary:            SMS daemon helper library
Group:              System/Libraries

%description -n libgsmsd7
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains Gammu SMS daemon shared library.

%prep
%setup -q

%build
mkdir build-dir
cd build-dir
cmake ../ \
      -DBUILD_SHARED_LIBS=ON \
      -DINSTALL_LSB_INIT=ON \
      -DBUILD_PYTHON=/usr/bin/python \
      -DCMAKE_INSTALL_PREFIX=%_prefix \
      -DINSTALL_DOC_DIR=%gammu_docdir \
      -DINSTALL_LIB_DIR=%_lib \
      -DINSTALL_LIBDATA_DIR=%_lib
make %{?_smp_mflags} %{!?_smp_mflags:%{?jobs:-j %jobs}}

%check
cd build-dir
ctest -V

%install
make -C build-dir install DESTDIR=%buildroot
%find_lang %{name}
%find_lang libgammu
cat libgammu.lang >> %{name}.lang
install -m644 docs/config/smsdrc %buildroot/etc/gammu-smsdrc

%post -n libGammu7 -p /sbin/ldconfig

%post -n libgsmsd7 -p /sbin/ldconfig

%postun -n libGammu7 -p /sbin/ldconfig

%postun -n libgsmsd7 -p /sbin/ldconfig

%post smsd
/sbin/chkconfig --add gammu-smsd

%preun smsd
if [ $1 = 0 ] ; then
    /sbin/service gammu-smsd stop >/dev/null 2>&1
    /sbin/chkconfig --del <script>
fi

%postun smsd

%files -f %name.lang
%defattr(-,root,root)
%doc %gammu_docdir
%config /etc/bash_completion.d/gammu
%_bindir/gammu
%_bindir/gammu-config
%_bindir/gammu-detect
%_bindir/jadmaker
%_mandir/man1/gammu.1*
%_mandir/man1/gammu-config.1*
%_mandir/man1/gammu-detect.1*
%_mandir/man1/jadmaker.1*
%_mandir/man5/gammurc.5*
%_mandir/man5/gammu-backup.5*
%_mandir/man5/gammu-smsbackup.5*

%files smsd
%defattr(-,root,root)
%_bindir/gammu-smsd
%_bindir/gammu-smsd-inject
%_bindir/gammu-smsd-monitor
%_mandir/man1/gammu-smsd*
%_mandir/man7/gammu-smsd*
%_mandir/man5/gammu-smsd*
%attr(755,root,root) %config /etc/init.d/gammu-smsd
%config /etc/gammu-smsdrc

%files -n libGammu7
%defattr(-,root,root)
%_libdir/libGammu*.so.*
%_datadir/gammu/

%files -n libgsmsd7
%defattr(-,root,root)
%_libdir/libgsmsd*.so.*

%files devel
%defattr(-,root,root)
%_includedir/%name
%_libdir/pkgconfig/%name.pc
%_libdir/pkgconfig/%name-smsd.pc
%_libdir/*.so

%files -n python-gammu
%defattr(-,root,root)
%doc README.Python python/examples
%g_python_sitearch/*

%clean
rm -rf %buildroot

%changelog
* Thu Feb 12 2015 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 1.34.0.-r1
- Initial spec with gammu-1.34.0 version.
