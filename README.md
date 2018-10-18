# stuffs
Stuff's

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
	  "port": [
      7000
	  ]
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
