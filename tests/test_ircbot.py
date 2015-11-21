#!/usr/bin/env python
# coding: UTF-8


import os
import time
import unittest
import json

from webhooks2irc.core.ircbot import IrcBotService


class IrcBotServiceTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IrcBotServiceTestCase, self).__init__(*args, **kwargs)
        self.ibs = IrcBotService()

    def setUp(self):
        self.ibs.start()

    def test_bot_hi(self):
        self.ibs.hi.set()
        time.sleep(1)
        self.assertTrue(self.ibs.is_alive())

    def tearDown(self):
        self.ibs.stop.set()
        time.sleep(1)
