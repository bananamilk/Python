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
def getLdapUserDN(user):
	l = ldap.initialize(ldapPath)
	# Set LDAP protocol version used
	l.protocol_version = ldap.VERSION3
	l.simple_bind_s(ldapUser,ldapPasswd)
	# l.simple_bind_s(dn,ldapPasswd) 

	searchScope = ldap.SCOPE_SUBTREE
	searchFiltername = "sAMAccountName"
	retrieveAttributes = None
	searchFilter = '(' + searchFiltername + "=" + user +')'
	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
	result_type, result_data = l.result(ldap_result_id,1)
	if(not len(result_data) == 0):
		r_a,r_b = result_data[0]
		print r_b["distinguishedName"]
		return 1, r_b["distinguishedName"][0]
	else:
		return 0, ''

		

if __name__ == '__main__':
	# ldapPath = "ldap://10.10.16.14"
	ldapPath = "ldap://10.10.16.12"
	baseDN = "DC=test,DC=com"
	# ldapUser = "root"
	ldapUser = "CN=admin,DC=test,DC=com"
	ldapPasswd = "demo"
	getLdapUserDN("test1")
	# demo = "test6"
	# dn = "uid=root,ou=People,dc=shterm,dc=com"
	# logonAnnymous()

#循环读取用户来登录ldap
	# file = open("test.txt")
	# while 1:
	#     line = file.readline()
	#     line = line.strip('\n')
	#     print line
	#     ldapUser = line
	#     getLdapUserDN()
	#     print "bind success"
	#     if not line:
	#         break
	# file.close()
