#!/usr/bin/python
import os
import xlrd,xlwt
from xlutils.copy import copy

'''
open excel file 
if excel does not exisit
creatr an new excel file named sourceExcel
rb for Workbook
mysheet for sheet
'''
def open_excel(targetExcel=None):
	if targetExcel:
		ab = xlrd.open_workbook(targetExcel)
		print ab.sheet_names()
		rb = copy(ab)
		mysheet = rb.get_sheet(1)
	else:
		rb = xlwt.Workbook()
		mysheet = rb.add_sheet("sheet1")
	return rb,mysheet


def copy_csvDate(rb,sourceExcel=None):
	with open(sourceExcel,"r") as csvfile:
		list_data = csvfile.read()
	list_data = list_data.split("\n")
	list_data.remove('')
	l=1
	for line in list_data:
		print line
		r=1
		line = line.split(',')
		for i in line:
			mysheet.write(l,r,i)
			r = r+1
		l = l+1
	while l<10000:
		x=1
		while x<len(line)+1:
			mysheet.write(l,x,'')
			x = x+1
		l = l+1
	return csvfile

def save_excel(rb):
	rb.save('test_report.xls')

def close_excel(sb):
	sb.close()
	print "the status of sourceExcel"
	print sb.closed
			

if __name__ == '__main__':
	try:
		rb,mysheet = open_excel("./test_report.xls")
		#rb,mysheet = open_excel()
		sb = copy_csvDate(rb,"./time_report.csv")
		save_excel(rb)
	except Exception, e:
		print e
	finally:
		close_excel(sb)
