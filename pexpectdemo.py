#!/usr/bin/python2.6 
# -*- coding: utf-8 -*-
# filename: pexpect_test.py

import pexpect,time,sys

if __name__ == '__main__':
    user = 'natsu'
    ip = '192.168.9.208'
    passwd = '1'
    cmds = ['ps','ls','pwd','ifconfig','date']
    try:
        demo = open("demo.txt", "ab")
        demo.write ('==========Log Tile: demo==========\n')
        print user
        child = pexpect.spawn('ssh %s@%s' % (user,ip))
        
        # firstTime = child.expect(['password: ', 'continue connecting (yes/no)?'])
        # if firstTime == 1 :
        #     child.sendline('yes')
        child.expect('Password:')
        child.sendline(passwd)
        child.expect('Select group:')
        child.sendline('1')
        child.expect('Select page:')
        child.sendline('1') #/16.24
        child.expect('Select account:')
        child.sendline('/root')
        child.expect('Input session comment:')
        child.sendline('natsu')
        # child.sendline(cmds)
        # p = pexpect.spawn(cmds)
        # p.logfile = demo
        # p.expect(pexpect.EOF)
        for cmd in cmds:
            child.sendline(cmd)
            time.sleep(2)
            p = pexpect.spawn(cmd)
            p.logfile = demo
            p.expect(pexpect.EOF)
        demo.close()
    except pexpect.TIMEOUT:  
        print "TIMEOUT" 
    finally:
        child.close()