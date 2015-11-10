#!/usr/bin/env python
# coding: UTF-8

from logging import config as logconfig

from webhooks2irc import settings


def init_logger():
    logconfig.dictConfig(settings.LOG_CONFIG_DICT)
