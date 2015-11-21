#!/usr/bin/env python
# coding: UTF-8

from __future__ import (absolute_import,
                        unicode_literals)
import logging
# pylint: disable=import-error
try:
    from urllib import parse as urlparse  # for python3
except ImportError:
    import urlparse
# pylint: enable=import-error

import bottle
from bottle import (get,
                    post,
                    template,
                    request)

from webhooks2irc import settings
from webhooks2irc.core.logger import init_logger
from webhooks2irc.core.ircbot import IrcBotService
from webhooks2irc.core.template import MessageTemplate


# FIXME: main function
init_logger()
msgtempl = MessageTemplate()
logger = logging.getLogger('webhooks2irc')
ser = IrcBotService()
ser.daemon = True
ser.start()


@get('/')
def index():
    URI = urlparse.urljoin(request.url, '/{0}/hooks.json'.format(
                                        settings.IRC_CHANNEL))
    return template("""<h1>{{message}}</h1>
                    <h2>Web Hooks Address:</h2></br>
                    <input value="{{URI}}" size="40" />
                    """,
                    message='Web Hooks 2 IRC Running..',
                    URI=URI)


@post('/<channel>/hooks.json')
def hooks(channel):
    event = request.get_header('X-Gitlab-Event')
    logger.info('X-Gitlab-Event: %s', event)
    logger.debug(repr(request.json))
    message = msgtempl.get_message(event, request.json)
    if message:
        logger.debug(message)
        ser.put_message({'channel': channel, 'message': message})
    else:
        logger.info('not found template.')
    return template('ok. channel:{{channel}} event: {{event}}',
                    channel=channel,
                    event=event)


@get('/irc/hi')
def irc_hi():
    ser.hi.set()
    return 'ok.'

if __name__ == '__main__':
    logger.info("Running Develope Mode.")
    bottle.run(host=settings.WEB_HOST, port=settings.WEB_PORT)
else:
    app = application = bottle.default_app()
