#!/usr/bin/env python
import random
import os
import arrow

from config.config import USER_AGENT, LOGGER, TIMEZONE
str1="/root/soapclient/MyNovel/data/user_agents.txt"

def get_data(filename, default=''):
    """
    Get data from a file
    :param filename: filename
    :param default: default value
    :return: data
    """
    root_folder = os.path.dirname("/root/soapclient/MyNovel")
    user_agents_file = os.path.join(
        os.path.join(root_folder, 'data'), filename)
    try:
        with open(user_agents_file) as fp:
            data = [_.strip() for _ in fp.readlines()]
    except:
        data = [default]
    return data


def get_random_user_agent() :
    """
    Get a random user agent string.
    :return: Random user agent string.
    """
    return random.choice(get_data('user_agents.txt', USER_AGENT))


def get_time():
    utc = arrow.utcnow()
    local = utc.to(TIMEZONE)
    time = local.format("YYYY-MM-DD HH:mm:ss")
    return time

