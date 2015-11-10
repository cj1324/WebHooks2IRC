#!/usr/bin/env python
# coding: UTF-8

WEB_HOST = "0.0.0.0"
WEB_PORT = 8080

IRC_CHANNEL = "default"
IRC_HOST = "10.0.0.0"
IRC_PORT = 6667

IRC_NICK = "GitLabBot"
IRC_PASSWD = ""
IRC_HIMSG = "Bot Running ok."

IRC_DATA_TIMEOUT = 1

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
