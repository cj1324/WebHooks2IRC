#!/usr/bin/env python
# coding: UTF-8

import time
import threading
import logging

from irc import client as irc_client

from webhooks2irc import settings
logger = logging.getLogger(__name__)


class IrcBotService(threading.Thread):
    def __init__(self):
        self.client = irc_client.Reactor()
        server = self.client.server()
        logger.debug('connect to {0}.'.format(settings.IRC_HOST))
        server.connect(settings.IRC_HOST,
                       settings.IRC_PORT,
                       settings.IRC_NICK)
        server_name = server.get_server_name()
        self.server = server
        self.hi = threading.Event()
        super(IrcBotService, self).__init__()

    def run(self):
        while True:
            if not self.server.is_connected():
                logger.debug('server reconnect.')
                self.server.reconnect()
            self.client.process_once(settings.IRC_DATA_TIMEOUT)
            if self.hi.is_set():
                logger.debug('ready send hi message.')
                self.server.join("#{0}".format(settings.IRC_CHANNEL))
                self.server.privmsg("#{0}".format(settings.IRC_CHANNEL),
                                    settings.IRC_HIMSG)
                self.hi.clear()
