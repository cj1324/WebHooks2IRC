#!/usr/bin/env python
# coding: UTF-8

import logging

from mako.lookup import TemplateLookup

from webhooks2irc import settings

logger = logging.getLogger()


class MessageTemplate(object):
    def __init__(self):
        self.lookup = TemplateLookup(settings.TEMPLATE_DIRS)

    def _get_template(self, event):
        filename = event.replace(' ', '-').lower()
        template_name = "/{0}.tpl".format(filename)
        if self.lookup.has_template(template_name):
            return self.lookup.get_template(template_name)

    def get_message(self, event, json):
        template = self._get_template(event)
        if template is None:
            return

        try:
            message = template.render(**json)
        except (KeyError, TypeError, IndexError):
            logger.exception("Template Render Failed.")
            return

        # use replace so. Carriage returns not allowed in privmsg(text)
        # https://github.com/jaraco/irc/blob/master/irc/client.py#L900
        return message.replace('\n', '').replace('\r', '').strip()
