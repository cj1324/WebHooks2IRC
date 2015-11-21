#!/usr/bin/env python
# coding: UTF-8

import os
import unittest
import json

from webhooks2irc.core.template import MessageTemplate


class MessageTemplateTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MessageTemplateTestCase, self).__init__(*args, **kwargs)
        self.mt = MessageTemplate()

    def get_json_data(self, event):
        testdir = os.path.dirname(os.path.abspath(__file__))
        filename = event.replace(' ', '-').lower()
        path = os.path.join(testdir, 'data', '{0}.json'.format(filename))
        with open(path) as fp:
            return json.load(fp)

    def test_not_found_template(self):
        templ = self.mt.get_message('Push Fail', {})
        self.assertIsNone(templ)

    def test_issue_hook_template(self):
        event = 'Issue Hook'
        templ = self.mt.get_message(event, self.get_json_data(event))
        self.assertIsNotNone(templ)
