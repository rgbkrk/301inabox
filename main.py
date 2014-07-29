#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado
import tornado.autoreload
import tornado.ioloop
import tornado.web
import tornado.httpclient

import tornado.httputil

import json

import logging

import os

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

        logging.info("Getting redirect")
        newdomain = self.handle_redirect(origin)

        url = newdomain + uri

        logging.info("{} -> {}".format(origin, url))

        self.redirect(url, permanent=True)

    def handle_redirect(self, origin):

        # If using the 301inaboxadmin
        admin = os.environ.get("ADMIN_PORT")
        if(admin):
            admin_url = admin.split("tcp://")[1]

            http_client = tornado.httpclient.HTTPClient()
            try:
                headers = tornado.httputil.HTTPHeaders({"Content-Type": "application/json"})
                response = http_client.fetch(
                        "http://" + admin_url + "/api/records/" + origin,
                        headers=headers)
                body = response.body
            except tornado.httpclient.HTTPError as e:
                logging.error(e)

            http_client.close()

            record = json.loads(body)

            return record['url']
        
        return redirects.get(origin, "http://example.org")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/.*", MainHandler),
    ])

    application.listen(8080)

    logging.info("301inabox Listening on 8080, srsly")

    ioloop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(ioloop)
    ioloop.start()
