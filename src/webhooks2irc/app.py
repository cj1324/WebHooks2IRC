#!/usr/bin/env python
# coding: UTF-8

from __future__ import (absolute_import,
                        unicode_literals)

try:
    from urllib import parse as urlparse  # for python3
except ImportError:
    import urlparse

import bottle
from bottle import (get,
                    post,
                    template,
                    request)


@get('/')
def index():
    URI = urlparse.urljoin(request.url, '/hooks.json')
    return template("""<h1>{{message}}</h1>
                    <h2>Web Hooks Address:</h2></br>
                    <input value="{{URI}}" size="40" />
                    """,
                    message='Web Hooks 2 IRC Running..',
                    URI=URI)


@post('/hooks.json')
def hooks():
    pass

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8080)
else:
    app = application = bottle.default_app()
