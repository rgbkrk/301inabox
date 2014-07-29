#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado
import tornado.autoreload
import tornado.ioloop
import tornado.web

import logging

import tornado.options
tornado.options.parse_command_line()


redirects = {
        "localhost:8888": "http://lambdaops.com",
        "127.0.0.1:8888": "http://lambdaops.com",
        "lambdaops.net": "http://lambdaops.com",
}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Use domain request originated from
        # Create full URL

        uri = self.request.uri
        origin = self.request.host

        newdomain = redirects.get(origin, "http://example.org")

        url = newdomain + uri

        logging.info("{} -> {}".format(origin, url))
        self.redirect(url, permanent=True)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/.*", MainHandler),
    ])

    application.listen(8888)

    logging.info("Listening on 8888")

    ioloop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(ioloop)
    ioloop.start()
