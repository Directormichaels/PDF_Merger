import PyPDF2 #...........
import sys #.............:.....Import these
import os #..............:

merger = PyPDF2.PdfMerger()
for file in os.listdir(os.curdir): #.................loop through files in current directory
    if file.endswith(".pdf"): #......................check if the file has a '.pdf' extension(i.e. if the file is a pdf)
        merger.append(file) #.......................add the file to the merger variable

merger.write("new.pdf") #...................write the combined file to a file "new.pdf"