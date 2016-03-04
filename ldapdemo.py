#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# filename: ldap_test.py
import ldap

'''
实现LDAP用户登录验证，首先获取用户的dn，然后再验证用户名和密码
'''

#get User Dn
# def getLdapUserDN():
# 	l = ldap.initialize(ldapPath)
# 	# Set LDAP protocol version used
# 	l.protocol_version = ldap.VERSION3
# 	l.simple_bind_s(ldapUser,ldapPasswd)
# 	print "bind success"

if __name__ == '__main__':
	ldapPath = "ldap://10.10.16.12"
	baseDn = "DC=ad,DC=qizhitest,DC=com"
	ldapUser = "test1"
	ldapPasswd = "0"
	# getLdapUserDN()
	l = ldap.initialize(ldapPath)
	# Set LDAP protocol version used
	l.protocol_version = ldap.VERSION3
	l.simple_bind_s(ldapUser,ldapPasswd)
	print "bind success"
