import win32com.client, sys, os, codecs, re

def GetAllText():
	path = os.getcwd() + "\\" + raw_input("Input File:")
	filename = re.findall(r'\\(\w+)',path)[-1]
	Application = win32com.client.Dispatch("Powerpoint.Application")
	#opens power point application in windows in background
	Presentation = Application.Presentations.Open(Path)
	#opens the specific file in the given path
	Presentation = Application.ActivePresentation
	#Makes the opened presentation as the active presentation
	with open(filename + ".txt","wb") as f:
		res_ar = []
		for slide in Presentation.Slides:#Takes each slide in ppt
			f.write("\r\n")
			slide_ar = []
			for slide in slide.Shapes:#Takes each shape in a slide
				f.write("\r\n")
				if shape.HasTextFrame:#Checks if it has textframe
					if shape.TextFrame.HasText:#checks if it has text
						text = shape.TextFrame.TextRange.Text
						slide_ar.append(text)
						f.write(text.replace("\r","\r\n").encode("UTF-8") + "\n")
			res_ar.append(slide_ar)
	Application.Quit()
	#Closes the powerpoint application in the background
	print res_ar

GetAllText() 