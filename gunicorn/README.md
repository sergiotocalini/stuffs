# Gunicorn
To have the service installed you can follow the next step:
```
#~ git clone https://github.com/sergiotocalini/stuffs.git
#~ sudo ./stuffs/gunicorn/install.sh
#~
```

## Dependencies
### Packages
* ksh
* git
* python-pip
* python-gunicorn
* python-setuptools
* python-virtualenv

#### Debian/Ubuntu
```
#~ sudo apt install ksh git python-pip python-gunicorn python-setuptools python-virtualenv
#~
```

#### Red Hat
```
#~ sudo yum install ksh git python-pip python-gunicorn python-setuptools python-virtualenv
#~
```

## Projects
We need to enable the projects we want to run with gunicorn using json format as we can see in the example.json.save
```json
#~ cat /etc/gunicorn/conf.d/example.json.save
{
  "id": "",
  "name": "example",
  "desc": "Example Description",
  "version": "AHEAD",
  "home": "/opt/example",
  "monitoring": {
     "enable": "yes",
     "ws": {
        "url": "http://localhost:7000/",
        "codes": [200]
     },
     "statsd": {
        "host": "localhost:8125",
	"prefix": "gunicorn.example"
     },
     "port": [
        7000
     ],
     "tags": [
	 "example"
     ]
  },
  "syslog": {
     "enable": true,
     "prefix": "example",
     "facility": "user",
     "address": "unix:///run/systemd/journal/syslog"
  },
  "scripts": {
	  "start": "",
	  "stop": ""
  },
  "runtime": {
	  "user": "python",
	  "virtualenv": "yes",
	  "home": "/opt/example",
	  "opts": ["run:example -w 5 -b 0.0.0.0:7000 -e APP_SETTINGS=example.config.Local"]
  }
}
#~
```

Once we have the json completed we can start, stop, reload the project in this way
```
#~ /etc/init.d/gunicorn stop example
Stopping: example ( Example Description )
#~ /etc/init.d/gunicorn start example
Starting: example ( Example Description )
#~ /etc/init.d/gunicorn reload example
Reloading: example ( Example Description )
#~
```

### Virtualenv
Also to create the virtual env and install the requirements.txt file we can use the following function.
```
#~ /etc/init.d/gunicorn virtualenv example

#~
```

## Systemd
To enable the project on systemd we can create the following file.
```
~# cat /etc/systemd/system/example.service
[Unit]
Description=Example Description
After=network.target
SourcePath=/etc/init.d/gunicorn

[Service]
Type=simple
ExecStart=/etc/init.d/gunicorn start example
ExecStop=/etc/init.d/gunicorn stop example
RemainAfterExit=yes
Restart=no
TimeoutSec=5min
IgnoreSIGPIPE=no
KillMode=process
GuessMainPID=no

[Install]
WantedBy=multi-user.target
~# systemctl daemon-reload
~# systemctl enable example
~# systemctl restart example
~# systemctl status example
● example.service - Example Description
   Loaded: loaded (/etc/init.d/gunicorn; enabled; vendor preset: enabled)
   Active: active (exited) since Fri 2018-11-30 09:56:23 UTC; 5min ago
 Main PID: 5874 (code=exited, status=0/SUCCESS)
   CGroup: /system.slice/example.service
           ├─5919 /etc/gunicorn/venvs/example/bin/python2 /etc/gunicorn/venvs/example/bin/gunicorn ...
           ├─5923 /etc/gunicorn/venvs/example/bin/python2 /etc/gunicorn/venvs/example/bin/gunicorn ...
           ├─5924 /etc/gunicorn/venvs/example/bin/python2 /etc/gunicorn/venvs/example/bin/gunicorn ...
           ├─5926 /etc/gunicorn/venvs/example/bin/python2 /etc/gunicorn/venvs/example/bin/gunicorn ...
           ├─5928 /etc/gunicorn/venvs/example/bin/python2 /etc/gunicorn/venvs/example/bin/gunicorn ...
           └─5930 /etc/gunicorn/venvs/example/bin/python2 /etc/gunicorn/venvs/example/bin/gunicorn ...

Nov 30 09:56:23 apy01.example.com systemd[1]: Stopped Example Description.
Nov 30 09:56:23 apy01.example.com systemd[1]: Started Example Description.
Nov 30 09:56:24 apy01.example.com gunicorn[5874]: Starting: example ( Example Description )
~#
```
