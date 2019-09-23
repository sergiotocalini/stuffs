Summary:                Bind DNS Server - Corporacion America Version
Name:                   bind
Version:                9.9.5
Release:                P1_1%{?dist}
BuildArch:		x86_64
License:                GPL v2
Group:                  Networking/Admin
Source0:                bind-9.9.5.tar.gz
Source1:		bind
URL:                    www.isc.org/downloads/bind/
Requires:       	python-argparse
Requires:	        openssl
Requires:          	python-dns
BuildRoot:              %{_tmppath}/%{name}-%{version}-root

%define			prefix					/mnt/%{name}-%{version}
%define			_unpackaged_files_terminate_build	0

%description
Bind DNS Server - CA Version

%pre
/usr/bin/getent -s files passwd named &> /dev/null || /usr/sbin/useradd -M -d /mnt/bind -s /sbin/nologin named &> /dev/null
exit 0

%preun
/sbin/service named stop &> /dev/null
/sbin/chkconfig --del named &> /dev/null

%post
/sbin/chkconfig --add named &> /dev/null
ln -sf %{prefix} /mnt/%{name} &> /dev/null

%postun
unlink /mnt/%{name} &> /dev/null

%prep
%setup -q -n %{name}-%{version}

%build
./configure --with-dlz-ldap=yes \
	    --with-python \
	    --with-openssl=yes \
	    --with-dlz-filesystem=yes \
	    --enable-newstats \
	    --enable-threads \
	    --with-libxml2 \
	    --prefix=%{prefix}

%install
make install DESTDIR=${RPM_BUILD_ROOT}
for i in $(find %{S:1}/mnt/bind/ -type d); do
   install -m 755 -d ${i} ${RPM_BUILD_ROOT}${i/"/root/rpmbuild/SOURCES/bind/mnt/bind"/"/mnt/bind-%{version}"}
done
for i in $(find %{S:1}/mnt/bind/ -type f); do
   install -m 755 ${i} ${RPM_BUILD_ROOT}${i/"/root/rpmbuild/SOURCES/bind/mnt/bind"/"/mnt/bind-%{version}"}
done
for i in $(find %{S:1} -type d ! -path "*/mnt/bind*"); do
   install -m 755 -d ${i} ${RPM_BUILD_ROOT}${i/"/root/rpmbuild/SOURCES/bind"/""}
done
for i in $(find %{S:1} -type f ! -path "*/mnt/bind*"); do
   install -m 755 ${i} ${RPM_BUILD_ROOT}${i/"/root/rpmbuild/SOURCES/bind"/""}
done

%files
%defattr(644,named,named,755)
				/mnt/%{name}-%{version}/etc
				/mnt/%{name}-%{version}/include
				/mnt/%{name}-%{version}/lib
				/mnt/%{name}-%{version}/share
				/mnt/%{name}-%{version}/var
				/mnt/%{name}-%{version}/logs
%attr(755,-,-)			/mnt/%{name}-%{version}/bin
%attr(755,-,-)			/mnt/%{name}-%{version}/sbin
%attr(755,root,root)		/etc/init.d/named

%changelog
* Mon Jun 16 2014 Santiago Julian Buczak <sbuczak@aa2000.com.ar> - 9.9.5-P1_1
- Initial spec with bind-9.9.5 version.
