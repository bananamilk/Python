#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: ldap_test.py
import ldap,ldap.sasl
import socket

'''
实现LDAP用户登录验证SAAL
'''

ldap.sasl._trace_level=0

ldap.set_option(ldap.OPT_REFERRALS,0)

ipaddr = "demo"
ldapPath = "ldap://" + socket.gethostbyname(ipaddr) + ":389" 

method = "DIGEST-MD5"
username = 'test1'.encode('utf-8')
password = '0'
sasl_dict = {ldap.sasl.CB_AUTHNAME:username, ldap.sasl.CB_PASS:password}
try:
	l = ldap.initialize(ldapPath,trace_level=0)
	l.protocol_version = 3

	sasl_auth = ldap.sasl.sasl(sasl_dict, method)
	print 20*'*',sasl_auth.mech,20*'*'
	print sasl_auth
	l.sasl_interactive_bind_s('', sasl_auth)
#print 'OPT_X_SASL_USERNAME',repr(l.get_option(ldap.OPT_X_SASL_USERNAME))
except ldap.INVALID_CREDENTIALS, e:
	print e
finally:
	l.unbind()