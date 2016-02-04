#!/usr/bin/python2.6 
# -*- coding: utf-8 -*-
# filename: pexpect_test.py

import pexpect,time,sys

if __name__ == '__main__':
    user = 'natsu'
    ip = '192.168.9.208'
    passwd = '1'
    cmds = ['ps','ls','pwd','ifconfig','date']
    demo = open("demo.txt", "ab")
    demo.write ('==========Log Tile: demo==========\n')
    print user
    child = pexpect.spawn('ssh %s@%s' % (user,ip))
    try:
        firstTime = child.expect(['password: ', 'continue connecting (yes/no)?'])
        if firstTime == 1 :
            child.sendline('yes')
        child.expect('Password:')
        child.sendline(passwd)
        child.expect('Select group:')
        child.sendline('1')
        child.expect('Select page:')
        child.sendline('16.24')
        child.expect('Select account:')
        child.sendline('\root')
        child.expect('Input session comment:')
        child.sendline('natsu')
        for cmd in cmds:
            child.sendline(cmd)
            print child.before   # Print the result of the ls command.
            child.logfile = demo
            child.expect(pexpect.EOF)
        demo.close()
    except pexpect.EOF:
        print "EOF"
    except pexpect.TIMEOUT:  
        print "TIMEOUT" 
    finally:
        child.close()