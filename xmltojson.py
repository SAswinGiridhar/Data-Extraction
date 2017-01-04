import json
import xml.etree.ElementTree as ET
import xmltodict#used to convert xml to dictionary(open source-MIT lisence)

def xmltojson():
	m = raw_input("Input XML file:")
	n = m.replace(".xml","")
	tree = ET.parse(m)#takes the entire xml hierarchy in the tree
	root = tree.getroot()#gets the root of the tree
	strroot = ET.tostring(root)#converts the root as a string
	dict = xmltodict.parse(strroot)#converts xml to dict
	jsonform = json.dumps(dict, indent=4)#converts dictionary to json
	file = open( n + ".json", "w+")
	file.write(jsonform)
	file.close()
	
	
