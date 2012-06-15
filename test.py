#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from http.httpclient import HttpClient 

httpc = HttpClient("http://www.sublimetext.com/dev")
resp = httpc.get()
if resp == None:
    print "nothing recived"
else :
    print resp