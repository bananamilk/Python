#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
print "Process %s strat ..." %(os.getpid())
pid = os.fork()
if pid == 0:
	print "This is child process and my pid is %d,my father process is %d" %(os.getpid(),os.getppid())
else:
	print "This is Fater process, And Its child pid is %d" %(pid)