#!/usr/bin/env python
# coding: UTF-8

import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

WEB_HOST = "0.0.0.0"
WEB_PORT = 8080

IRC_CHANNEL = "default"
IRC_HOST = "127.0.0.1"
IRC_PORT = 6667

IRC_NICK = "GitLabBot"
IRC_PASSWD = ""
IRC_HIMSG = "Bot Running ok."

IRC_DATA_TIMEOUT = 1

TEMPLATE_DIRS = [os.path.join(PROJECT_DIR, 'templates')]

LOG_CONFIG_DICT = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'loggers': {
        'webhooks2irc': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}
