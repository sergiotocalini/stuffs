all:
	echo "i pkginfo" > prototype
	echo "i preinstall" >> prototype
	echo "i postinstall" >> prototype
	echo "i preremove" >> prototype
	echo "i postremove" >> prototype
	echo "i request" >> prototype
	pkgproto /opt/soft/build/zabbix_agent-1.8.11=/usr/local >> prototype
	pkgmk -o -b /usr/local -r /
	pkgtrans /var/spool/pkg  zabbix_agent-1.8.11-sol10-sparc.pkg ZABagent
