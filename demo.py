#!/usr/bin/python2.6 #
#coding: utf-8
import  ldap

'''
实现LDAP用户登录验证，首先获取用户的dn，然后再验证用户名和密码
'''

ldappath = "ldap://10.10.16.14"#ldap服务器地址
baseDN = "cn=root,dc=shterm,dc=com"#根目录
ldapuser = "admin"#ldap服务器用户名
ldappass = "shterm"#ldap服务器密码

#获取用户的dn
def _validateLDAPUser(user):
    try:
        l = ldap.initialize(ldappath)
        l.protocol_version = ldap.VERSION3
        l.simple_bind(ldapuser,ldappass)

        searchScope  = ldap.SCOPE_SUBTREE
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
    except ldap.LDAPError, e:
        print e
        return 0, ''
    finally:
        l.unbind()
        del l

#连接超时，尝试多次连接
def GetDn(user, trynum = 30):
    i = 0
    isfound = 0
    foundResult = ""
    while(i < trynum):
        isfound, foundResult = _validateLDAPUser(user)
        if(isfound):
          break
        i+=1
    return foundResult


def LDAPLogin(userName,Password):
    try:
        if(Password==""):
            print "PassWord empty"
            return
        dn = GetDn(userName,10)
        if(dn==''):
            print "Not Exist User"
            return
        my_ldap = ldap.initialize(ldappath)
        print my_ldap.simple_bind_s(dn,Password)
        print "Login Ok"
    except Exception,e:
        print "Login Fail"
        # print str(e)

LDAPLogin("用户名","密码")