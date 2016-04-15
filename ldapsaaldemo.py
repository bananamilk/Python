#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: ldap_test.py
import ldap,ldap.sasl

'''
实现LDAP用户登录验证SAAL
'''
if __name__ == '__main__' :
	ldap.sasl._trace_level=0

	ldap.set_option(ldap.OPT_DEBUG_LEVEL,0)

	ldapPath = "ldap://10.10.16.11"
	sasl_mech = "DIGEST-MD5"
	sasl_cb_value_dict =  {
      ldap.sasl.CB_AUTHNAME    :'test1',
      ldap.sasl.CB_PASS        :'0',
    }

	sasl_auth = ldap.sasl.sasl(sasl_cb_value_dict,sasl_mech)
	print 20*'*',sasl_auth.mech,20*'*'
	l = ldap.initialize(ldapPath,trace_level=0)
	l.protocol_version = 3
	l.sasl_interactive_bind_s("", sasl_auth)
	print 'OPT_X_SASL_USERNAME',repr(l.get_option(ldap.OPT_X_SASL_USERNAME))
	l.unbind()