#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: ldap_test.py
import ldap

'''
实现LDAP用户登录验证，首先获取用户的dn，然后再验证用户名和密码
'''

#ldap用户登录
# def logonAnnymous():
# 	l = ldap.initialize(ldapPath)
# 	# Set LDAP protocol version used
# 	l.protocol_version = ldap.VERSION3
# 	l.simple_bind_s(ldapUser,ldapPasswd)
# 	# l.simple_bind_s(dn,ldapPasswd) 
# 	print "bind success"

#获得用户的dn
def getLdapUserDN():
	l = ldap.initialize(ldapPath)
	# Set LDAP protocol version used
	l.protocol_version = ldap.VERSION3
	l.simple_bind_s(ldapUser,ldapPasswd)
	# l.simple_bind_s(dn,ldapPasswd) 
	print "bind success"
		

if __name__ == '__main__':
	# ldapPath = "ldap://10.10.16.14"
	ldapPath = "ldap://10.10.16.12"
	baseDN = "DC=test,DC=com"
	# ldapUser = "root"
	ldapUser = "admin"
	ldapPasswd = "shterm"
	# demo = "test6"
	# dn = "uid=root,ou=People,dc=shterm,dc=com"
	# logonAnnymous()
	
	file = open("test.txt")
	while 1:
	    line = file.readline()
	    ldapUser = line
	    getLdapUserDN()
	    if not line:
	        break
	file.close()