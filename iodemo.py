#!/usr/bin/python
#import os
import xlrd,xlwt
from xlutils.copy import copy
wb = xlrd.open_workbook('demo.xls')
print wb.sheet_names()

sh = wb.sheet_by_index(0)

for i in range(sh.nrows):
	print sh.row_values(i)

first_col = sh.col_values(0)
print first_col

print sh.cell(0,0).value

wbk = xlwt.Workbook()
sheet = wbk.add_sheet("sheet1")
sheet.write(0,0,'haha')

wbk.save("test.xls")

ul = copy(wb)
uls = ul.get_sheet(0)
uls.write(0,0,'changed')

ul.save('demo.xls')


#os.mkdir('test')
#os.rmdir('test')

#filedemo = open("demo.txt","wb")
#filedemo.write("haha")
#print filedemo.name
#print filedemo.closed
#print filedemo.encoding
#filedemo.close()
#print filedemo.closed



