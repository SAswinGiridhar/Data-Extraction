import csv#Used to read and wrie in csv

def csvread(csvobj):
	read = csv.reader(csvobj)#used to read csv files
	for row in read:
		print(" ".join(row))
		
csvpath = raw_input("Input CSV file:")
with open(csvpath,'rb') as cvobj:
	csvread(cvobj)