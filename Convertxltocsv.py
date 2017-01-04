#*- coding: utf-8 -*-
import xlrd #Used to read excel files
import csv #Used to read and wrie in csv

def exltocsv(excelfile):
	workbook = xlrd.open_workbook(excelfile)#Opens the excel workbok as given
	all_worksheets = worksheet.sheet_names()#Has all the worksheet names in a workbook
	for wrkshtnm in all_worksheets:
		worksheet = workbook.sheet_by_name(wrkshtnm)
		convcsvfile = open(''.join([wrkshtnm,'.csv']),'wb')#makes the outfile as csv
		#writes the strings in csv
		wr = csv.writer(convcsvfile, quoting = csv.QUOTE_ALL)
		for rownum in xrange(worksheet.nrows):
			wr.writerow(
			 list([unicode(entry).encode("utf-8") if type(entry) == type(u'') else entry
			for entry in worksheet.row_valus(rownum)]))
		convcsvfile.close()
		
t = raw_input("Input Excel File:")
exltocsv(t)