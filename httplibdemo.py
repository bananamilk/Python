#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import httplib
try:
	url="192.168.9.209"
	conn = httplib.HTTPConnection(url,443)
	conn.request('GET','/index.php')

	response = conn.getresponse()
	print response.status
	print response.reason
	print response.read()
except Exception, e:
	print e
finally:
	conn.close()
