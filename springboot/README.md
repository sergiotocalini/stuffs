# Springboot
To have the service installed you can follow the next step:
```
#~ git clone https://github.com/sergiotocalini/stuffs.git
#~ sudo ./stuffs/springboot/install.sh
#~
```

## Dependencies
### Packages
* ksh
* git
* jps

__**Debian/Ubuntu**__
```
#~ sudo apt install ksh git default-jre-headless openjdk-<version>-jre-headless
#~
```

__**Red Hat**__
```
#~ sudo yum install ksh git java-<version>-openjdk-devel
#~
```

## Projects
We need to enable the projects we want to run with gunicorn using json format as we can see in the example.json.save
```json
#~ cat /etc/springboot/conf.d/example.json.save
{
  "id": "",
  "name": "example",
  "desc": "Example Description",
  "version": "AHEAD",
  "home": "/opt/springboot/example",
  "exec": "/opt/springboot/example/example.jar",
  "monitoring": {
     "enable": "yes",
     "ws": {
        "url": "http://localhost:8080/",
        "codes": [200]
     },
     "port": [
        8080
     ],
     "tags": [
        "example"
     ]
  },
  "scripts": {
	  "start": "",
	  "stop": ""
  },
  "runtime": {
	  "java_home": "/opt/springboot/example",
	  "java_opts": []
  }
}
#~
```
