Summary:		Zabbix - Open Source Monitoring Solution
Name:			zabbix
Version:		2.0.6
Release:		1
License:		GPL v2+
Group:			Networking/Admin
Source0:		http://dl.sourceforge.net/zabbix/%{name}-%{version}.tar.gz
URL:			http://zabbix.sourceforge.net/
BuildRequires:		OpenIPMI-devel
BuildRequires:		curl-devel
BuildRequires:		gcc
BuildRequires:		iksemel-devel
BuildRequires:		libssh2-devel
BuildRequires:		mysql-devel
BuildRequires:		net-snmp-devel
BuildRequires:		openssl-devel
BuildRequires:		sqlite-devel
BuildRequires:		openldap-devel
BuildRoot:		%{_tmppath}/%{name}-%{version}-root

%define _unpackaged_files_terminate_build	0
%define _sysconfdir				/etc/%{name}
%define _sysinitdir				/etc/init.d
%define _prefix					/mnt/soft/%{name}-%{version}
%define _mandir					%{_prefix}/share/man

%description
zabbix is software that monitors numerous parameters of a network and
the servers on that network. It is a useful tool for monitoring
the health and integrity of servers. zabbix uses a flexible
notification mechanism that allows users to configure email based
alerts for virtually any event. All monitored parameters are stored in
a database. zabbix offers excellent reporting and data visualisation
features based on the stored data. zabbix supports both polling and
trapping. All zabbix reports and statistics, as well as configuration
parameters, are accessed through a web-based front end.

%package agent
Summary:		Zabbix Agent
Group:			Networking/Admin
Requires:		%{name} = %{version}
Requires:		openssl-devel >= 0.9.7d

%description agent
This package provides the Zabbix Agent.

%package server-sqlite
Summary:		Zabbix Server
Group:			Networking/Admin
Requires:		%{name} = %{version}

%description server-sqlite
This package provides the Zabbix Server.

%package proxy-sqlite
Summary:		Program used as a proxy between zabbix servers and agents
Group:			Networking/Admin
Requires:		%{name} = %{version}

%description proxy-sqlite
This package provides a program that acts as a proxy between zabbix servers and agents, to assist in passing through firewalls and NAT.

%prep
%setup -q

%build
%configure \
	   --enable-agent \
	   --enable-proxy \
	   --enable-server \
	   --enable-ipv6 \
	   --with-jabber \
	   --with-ldap \
	   --with-libcurl \
	   --with-net-snmp \
	   --with-openipmi \
	   --with-sqlite3 \
	   --with-ssh2 \
	   --prefix=%{_prefix} \
	   --mandir=%{_mandir} \

%{__make} install \
	  DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre
grep zabbix /etc/group &> /dev/null || groupadd zabbix
id zabbix &> /dev/null || useradd -s /bin/false -c "Zabbix Monitoring" -g zabbix -d %{_prefix} zabbix &> /dev/null

%post
ln -s "%{name}-%{version}" "/mnt/soft/%{name}"

%post agent
[[ -d "%{_sysconfdir}/scripts" ]] || mkdir "%{_sysconfdir}/scripts"
[[ -d "%{_sysconfdir}/agent.d" ]] || mkdir "%{_sysconfdir}/agent.d"
if [[ ! -f "%{_sysconfdir}/zabbix_agentd.conf" ]]; then
   cat > "%{_sysconfdir}/zabbix_agentd.conf" <<EOF
LogFile=/tmp/zabbix_agentd.log
PidFile=/tmp/zabbix_agentd.pid
Server=${server-prd}
Hostname=`hostname -s`
Include=/etc/zabbix/agent.d/
EOF
   ln -s "zabbix_agentd.conf" "%{_sysconfdir}/zabbix_agent.conf"
fi
cat > "%{_sysinitdir}/zabbix-agent" <<EOF
#!/bin/sh
#
# chkconfig: - 86 14
# description: ZABBIX agent daemon
# processname: zabbix_agentd
# config: /etc/zabbix/zabbix_agentd.conf
#

### BEGIN INIT INFO
# Provides: zabbix-agent
# Required-Start: $local_fs $network
# Required-Stop: $local_fs $network
# Should-Start: zabbix zabbix-proxy
# Should-Stop: zabbix zabbix-proxy
# Default-Start:
# Default-Stop: 0 1 2 3 4 5 6
# Short-Description: Start and stop ZABBIX agent
# Description: ZABBIX agent
### END INIT INFO

# Source function library.
. /etc/rc.d/init.d/functions

exec=/mnt/soft/zabbix/sbin/zabbix_agentd
prog=\${exec##*/}
lockfile=/var/lock/subsys/zabbix-agent

start() {
   echo -n "Starting ZABBIX agent: "
   daemon \$exec
   rv=\$?
   echo
   [ \$rv -eq 0 ] && touch \$lockfile
   return \$rv
}

stop() {
   echo -n "Shutting down ZABBIX agent: "
   killproc \$prog
   rv=\$?
   echo
   [ \$rv -eq 0 ] && rm -f \$lockfile
   return \$rv
}

restart() {
   stop
   start
}

case "\$1" in
   start|stop|restart)
      \$1
      ;;
   force-reload)
      restart
      ;;
   status)
      status \$prog
      ;;
   try-restart|condrestart)
      if status \$prog >/dev/null ; then
         restart
      fi
      ;;
   reload)
      action "Service \${0##*/} does not support the reload action: " /bin/false
      exit 3
      ;;
   *)
   echo "Usage: \$0 {start|stop|status|restart|try-restart|force-reload}"
   exit 2
   ;;
esac
EOF
chkconfig --add zabbix-agent

%post server-sqlite
if [[ ! -f "%{_sysconfdir}/zabbix_server.conf" ]]; then
   cat > "%{_sysconfdir}/zabbix_server.conf" <<EOF
#NodeID=
LogFile=/tmp/zabbix_server.log
PidFile=/tmp/zabbix_server.pid
#DBHost=localhost
#DBName=zabbix
#DBUser=zabbix
#DBPassword=zabbix2011
EOF
fi
cat > "%{_sysinitdir}/zabbix-server" <<EOF
#!/bin/sh
#
# chkconfig: - 85 15
# description: ZABBIX server daemon
# config: /etc/zabbix/zabbix_server.conf
#

### BEGIN INIT INFO
# Provides: zabbix
# Required-Start: $local_fs $network
# Required-Stop: $local_fs $network
# Default-Start:
# Default-Stop: 0 1 2 3 4 5 6
# Short-Description: Start and stop ZABBIX server
# Description: ZABBIX server
### END INIT INFO

# Source function library.
. /etc/rc.d/init.d/functions

exec=/mnt/soft/sbin/zabbix_server
prog=\${exec##*/}
lockfile=/var/lock/subsys/zabbix

start() {
   echo -n "Starting ZABBIX server: "
   daemon \$exec
   rv=\$?
   echo
   [ \$rv -eq 0 ] && touch \$lockfile
   return \$rv
}

stop() {
   echo -n "Shutting down ZABBIX server: "
   killproc \$prog
   rv=\$?
   echo
   [ \$rv -eq 0 ] && rm -f \$lockfile
   return \$rv
}

restart() {
   stop
   start
}

case "\$1" in
   start|stop|restart)
      \$1
      ;;
   force-reload)
      restart
      ;;
   status)
      status \$prog
      ;;
   try-restart|condrestart)
      if status \$prog >/dev/null ; then
         restart
      fi
      ;;
   reload)
      action "Service \${0##*/} does not support the reload action: " /bin/false
      exit 3
      ;;
   *)
   echo "Usage: \$0 {start|stop|status|restart|try-restart|force-reload}"
   exit 2
   ;;
esac
EOF
chkconfig --add zabbix-server

%post proxy-sqlite
if [[ ! -f "%{_sysconfdir}/zabbix_proxy.conf" ]]; then
   cat > "%{_sysconfdir}/zabbix_proxy.conf" <<EOF
LogFile=/tmp/zabbix_proxy.log
PidFile=/tmp/zabbix_proxy.pid
Hostname=$(hostname -s)
#DBHost=localhost
DBName=/etc/zabbix/zabbix_proxy.sqlite
#DBUser=zabbix
#DBPassword=zabbix2011
#ListenPort=10052
EOF
fi
cat > "%{_sysinitdir}/zabbix-proxy" <<EOF
#!/bin/sh
#
# chkconfig: - 86 14
# description: ZABBIX proxy
# processname: zabbix_proxy
# config: /etc/zabbix/zabbix_proxy.conf
#

### BEGIN INIT INFO
# Provides: zabbix-proxy
# Required-Start: $local_fs $network
# Required-Stop: $local_fs $network
# Should-Start: zabbix
# Should-Stop: zabbix
# Default-Start:
# Default-Stop: 0 1 2 3 4 5 6
# Short-Description: Start and stop ZABBIX proxy
# Description: ZABBIX proxy
### END INIT INFO

# Source function library.
. /etc/rc.d/init.d/functions

exec=/mnt/soft/zabbix/sbin/zabbix_proxy
prog=\${exec##*/}
lockfile=/var/lock/subsys/zabbix-agent

start() {
   echo -n "Starting ZABBIX proxy: "
   daemon \$exec
   rv=\$?
   echo
   [ \$rv -eq 0 ] && touch \$lockfile
   return \$rv
}

stop() {
   echo -n "Shutting down ZABBIX proxy: "
   killproc \$prog
   rv=\$?
   echo
   [ \$rv -eq 0 ] && rm -f \$lockfile
   return \$rv
}


restart() {
   stop
   start
}

case "\$1" in
   start|stop|restart)
      \$1
      ;;
   force-reload)
      restart
      ;;
   status)
      status \$prog
      ;;
   try-restart|condrestart)
      if status \$prog >/dev/null ; then  
         restart
      fi
      ;;
   reload)
      action "Service \${0##*/} does not support the reload action: " /bin/false
      exit 3
      ;;
   *)   
      echo "Usage: \$0 {start|stop|status|restart|try-restart|force-reload}"
      exit 2
      ;;
esac
EOF
chkconfig --add zabbix-proxy

%postun
id zabbix &> /dev/null && userdel --force zabbix &> /dev/null
unlink /mnt/soft/zabbix

%files
%defattr(644,root,root,755)
%attr(750,zabbix,zabbix)	%dir %{_sysconfdir}
%attr(755,root,root)		%{_bindir}/zabbix_get
%attr(755,root,root)		%{_bindir}/zabbix_sender
%attr(755,root,root)		%{_mandir}/man1/zabbix_get.1*
%attr(755,root,root)		%{_mandir}/man1/zabbix_sender.1*

%files agent
%defattr(644,root,root,755)
%attr(755,root,root)		%{_sbindir}/zabbix_agentd
%attr(755,root,root)		%{_sbindir}/zabbix_agent
%attr(755,root,root)		%{_mandir}/man8/zabbix_agentd.8*

%files server-sqlite
%defattr(644,root,root,755)
%attr(755,root,root)		%{_sbindir}/zabbix_server
%attr(755,root,root)		%{_mandir}/man8/zabbix_server.8*

%files proxy-sqlite
%defattr(644,root,root,755)
%attr(755,root,root)		%{_sbindir}/zabbix_proxy
%attr(755,root,root)		%{_mandir}/man8/zabbix_proxy.8*

%changelog
* Mon Jun 03 2013 Initial Commit
*  Sergio Tocalini Joerg <sergiotocalini@gmail.com>

Revision 1.0   2013/06/03 00:00:00  Sergio Tocalini Joerg <sergiotocalini@gmail.com>
- Complete RPM Spec file for Zabbix 2.0.6 for RedHat.
