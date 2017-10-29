# Docker Chaos Monkey
Chaos monkey for your local docker

## Install
In a python virtual environment  
```
pip install -r requirements.txt
```

## Usage
`python driver.py --help` :
```
usage: driver.py [-h] -n NAME [-s SLEEP] [-v]

Docker container chaos

optional arguments:
  -h, --help              show this help message and exit
  -n NAME, --name NAME    container name regex pattern
  -s SLEEP, --sleep SLEEP sleep duration in seconds between consecutive actions
  -v, --verbose           increase output verbosity
```

## Supported actions
* Randomly restart containers that match a regex
