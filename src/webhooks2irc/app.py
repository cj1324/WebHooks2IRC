#!/usr/bin/env python
# coding: UTF-8

from __future__ import (absolute_import,
                        unicode_literals)

from webhooks2irc import settings
from webhooks2irc.core.ircbot import IrcBotService

try:
    from urllib import parse as urlparse  # for python3
except ImportError:
    import urlparse

import bottle
from bottle import (get,
                    post,
                    template,
                    request)


# FIXME: main function
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
    return template('ok. channel:{{channel}}', channel=channel)


@get('/irc/hi')
def irc_hi():
    ser.hi.set()
    return 'ok.'

if __name__ == '__main__':
    bottle.run(host=settings.WEB_HOST, port=settings.WEB_PORT)
else:
    app = application = bottle.default_app()
