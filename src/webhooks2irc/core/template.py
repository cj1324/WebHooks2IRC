#!/usr/bin/env python
# coding: UTF-8

import os

from mako.lookup import TemplateLookup

from webhooks2irc import settings


class MessageTemplate(object):
    def __init__(self):
        self.lookup = TemplateLookup(settings.TEMPLATE_DIRS)

    def _get_template(self, event):
        filename = event.replace(' ', '-').lower()
        return self.lookup.get_template("/{0}.tpl".format(filename))

    def get_message(self, event, json):
        template = self._get_template(event)
        return template.render(**json)
