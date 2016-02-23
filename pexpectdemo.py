#!/usr/bin/python2.6 
# -*- coding: utf-8 -*-
# filename: pexpect_test.py

import pexpect,time,sys

if __name__ == '__main__':
    user = 'natsu'
    ip = '192.168.9.208'
    passwd = '1'
    cmds = ['ps','ls','pwd','ifconfig','date']
    patterns = ['1','[Pp]assword:','Select group:','Select page:','Select server:','Select account:','Input session comment:','#','Select service:']
    CONTINUES,PASSWD,GROUP,PAGE,SERVER,ACCOUNT,ISCOMMT,OPFLAG,SERVICE = range(len(patterns))
    # CONTINUES = '1' #Are you sure you want to continue connecting (yes/no)?
    # PASSWD = '[Pp]assword:'
    # GROUP = 'Select group:'
    # PAGE = 'Select page:'
    # SERVER = 'Select server:'
    # ACCOUNT = 'Select account:'
    # ISCOMMT = 'Input session comment:'
    # OPFLAG = '#'
    # SERVICE = 'Select service:'
    try:
        demo = open("result.txt", "ab")
        demo.write('==========Log Tile: demo==========\n')
        print user
        child = pexpect.spawn('ssh %s@%s' % (user,ip))
        
        # firstTime = child.expect(['password: ', 'continue connecting (yes/no)?'])
        # if firstTime == 1 :
        #     child.sendline('yes')
        while True:
            flag=child.expect(patterns)
            if flag == CONTINUES:#0:
                child.sendline('yes')
            elif flag == PASSWD:
                child.sendline('1')
            elif flag == GROUP:
                child.sendline('1')
            elif flag == PAGE:
                child.sendline('0')
            elif flag == SERVER:
                child.sendline('16.24')
            elif flag == ACCOUNT:
                child.sendline('root')
            elif flag == ISCOMMT:
                child.sendline('natsu')
            elif flag == SERVICE:
                child.sendline('ssh')
            elif flag == OPFLAG:
                break
        # child.sendline(cmds)
        # p = pexpect.spawn(cmds)
        # p.logfile = demo
        # p.expect(pexpect.EOF)
        for cmd in cmds:
            # child.sendline(cmd)
            time.sleep(2)
            p = pexpect.spawn(cmd)
            p.logfile = demo
            p.write('=====================\n')
            p.expect(pexpect.EOF)
        demo.close()
    except pexpect.TIMEOUT:  
        print "TIMEOUT" 
    except pexpect.EOF:
        print "EOF"
    finally:
        child.close()