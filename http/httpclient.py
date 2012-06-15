#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import httplib, urllib
import urlparse

class HttpClient(object):
    """docstring for HttpClient"""

    NORMAL_HEADER = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5",  
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

    def __init__(self, url):
        self.url = url
        pu = urlparse.urlparse(self.url)
        self.host = pu[1]
        self.path = pu[2]
        self.query = pu[4]
        self.content = None
        # print pu

    def get(self):
        conn = httplib.HTTPConnection(self.host)
        path = self.path
        if self.query != None:
            path = path + "?" +self.query
            # print path

        conn.request("GET", path, "", self.NORMAL_HEADER)
        resp = conn.getresponse()
        if resp.status == 200 :
            self.content = resp.read()
        conn.close()
        return self.content

    def post(self, params):
        urlParams = getUrlEncodeParams(params)
        conn = httplib.HTTPConnection(self.host)
        conn.request("POST", self.path, urlParams, self.NORMAL_HEADER)
        resp = conn.getresponse()
        if resp.status == 200 :
            self.content = resp.read()
        conn.close()
        return self.content

    def getUrlEncodeParams(params):
        return urllib.urlencode(params)

        