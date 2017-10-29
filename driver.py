import argparse
import random
import re
import sys
import time
import signal

import docker

import log_helper

client = docker.from_env()
parser = argparse.ArgumentParser(description='Docker container chaos')
parser.add_argument('--name', help='container name regex pattern', dest='name', required=True)
parser.add_argument('--sleep', type=int, default=30,
                    help='sleep duration in seconds between consecutive actions', dest='sleep')
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
logger = log_helper.get_logger()

def signal_handler(signal, frame):
    """
    handle the Ctrl-C keyboard interrupt by cleanly exiting
    """
    logger.debug("Exiting")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def filter_containers_by_name(pattern):
    """
    filter running containers by their names
    :param pattern: regex name pattern
    :return: list of matched containers
    """
    logger.info("Matching containers using the following pattern %s" % pattern)
    running_containers = client.containers.list()
    logger.info('Running containers %s' % [x.attrs['Name'][1:] for x in running_containers])
    matched_containers = [ctr for ctr in running_containers if re.match(pattern, ctr.attrs['Name'][1:])]
    logger.info('Matched containers %s' % [y.attrs['Name'][1:] for y in matched_containers])
    return matched_containers


def restart_container(ctr):
    """
    restart a container
    :param ctr: container to restart
    """
    logger.info("Restarting %s" % ctr.attrs['Name'][1:])
    logger.debug("Stopping %s" % ctr.attrs['Name'][1:])
    ctr.stop()
    logger.debug("Starting %s" % ctr.attrs['Name'][1:])
    ctr.start()


def sleep_between_restarts(interval):
    """
    sleep
    :param interval: sleep interval
    """
    logger.info("Sleeping for %s seconds" % interval)
    time.sleep(interval)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.verbose:
        log_helper.enable_debug_level()
    container_regex_pattern = args.name
    sleep_interval = args.sleep
    matches = filter_containers_by_name(container_regex_pattern)
    if not matches:
        logger.error("No matched containers, exiting")
        sys.exit(1)
    else:
        while True:
            random_matched_container = random.choice(matches)
            restart_container(random_matched_container)
            sleep_between_restarts(sleep_interval)