#!/usr/bin/env python
# coding: UTF-8

import threading
import logging

# pylint: disable=import-error
try:
    import queue
except ImportError:
    import Queue as queue
# pylint: enable=import-error

from irc import client as irc_client

from webhooks2irc import settings
logger = logging.getLogger(__name__)


class IrcBotService(threading.Thread):
    def __init__(self):
        self.client = irc_client.Reactor()
        self.queue = queue.LifoQueue(32)
        server = self.client.server()
        logger.info('connect to %s IRC.', settings.IRC_HOST)
        server.connect(settings.IRC_HOST,
                       settings.IRC_PORT,
                       settings.IRC_NICK)
        self.server = server
        self.hi = threading.Event()
        super(IrcBotService, self).__init__()

    def _reconn(self):
        if not self.server.is_connected():
            logger.debug('server reconnect.')
            self.server.reconnect()

    def _send(self, channel, message):
        self._reconn()
        self.server.join("#{0}".format(channel))
        self.server.privmsg("#{0}".format(channel), message)

    def run(self):
        while True:
            self._reconn()
            self.client.process_once(settings.IRC_DATA_TIMEOUT)
            if self.hi.is_set():
                logger.debug('ready send hi message.')
                self._send(self.IRC_CHANNEL,
                           self.IRC_HIMSG)
                self.hi.clear()
            try:
                obj = self.queue.get(block=False)  # FIXME: Python 2 ?
                logger.info("ready send to #%s", obj['channel'])
                self._send(obj['channel'], obj['message'])
            except queue.Empty:
                pass

    def put_message(self, obj):
        self.queue.put(obj)
