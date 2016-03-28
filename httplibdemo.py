#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import httplib
url="https://192.168.9.209"
conn = httplib.HTTPConnection(url,443)
conn.request('GET','/index.php')

response = conn.getresponse()
print response.status
print response.reason
print response.read()
conn.close()
