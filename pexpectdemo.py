# -*- coding: utf-8 -*-
# filename: pexpect_test.py

import pexpect

if __name__ == '__main__':
    user = 'natsu'
    ip = '192.168.9.208'
    mypassword = '1'
    
    print user
    child = pexpect.spawn('ssh %s@%s' % (user,ip))
#    if child.expect('Are you sure you want to continue connecting (yes/no)?'):
#        child.sendline('yes')    
    child.expect ('Password:')
    child.sendline (mypassword)
    
    child.expect('Select group:')
    child.sendline('1')
    child.expect ('Select page:')
    child.sendline ('1')
    child.expect('Select account:')
    child.sendline('9')
    child.expect('Input session comment:')
    child.sendline('ls')
    print child.before   # Print the result of the ls command.
    child.sendline("echo '112' >> /home/forever/1.txt ")
    child.interact()     # Give control of the child to the user.