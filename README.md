# Docker Chaos Monkey
Chaos monkey for your Docker containers

## Supported actions
* Randomly restart containers that match a regex

## Install
In a python virtual environment
```
pip install docker_chaos_monkey
```

## Usage
Randomly restart a container that matches _my_container*_ each 30 seconds :
```
docker-chaos-monkey -n my_container* -s 30
```

## Help
`docker-chaos-monkey--help` :
```
usage: driver.py [-h] -n NAME [-s SLEEP] [-v]

Docker container chaos

optional arguments:
  -h, --help              show this help message and exit
  -n NAME, --name NAME    container name regex pattern
  -s SLEEP, --sleep SLEEP sleep duration in seconds between consecutive actions
  -v, --verbose           increase output verbosity
```
