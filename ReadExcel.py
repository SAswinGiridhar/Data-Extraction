import xlrd#Used to read excel files

def readxls(path):
	book = xlrd.open_workbook(path)
	sdata = []
	noofsh = book.nsheets#counts the no of worksheets
	for i in range(noofsh):
		xlsheet = book.sheet_by_index(i)#takes each worksheet by index
		for row in range(x1sheet.nrows):
			values = []
			for col in range(x1sheet.ncols):
				content = x1sheet.cell(row, col).value
				values.append(content)
			sdata.append(values)
	print sdata
	print "-" * 50
	
path = raw_input("Inputfile name:")
readxls(path)
