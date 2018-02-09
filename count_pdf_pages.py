#Simpe Script for Counting the Pages of all PDF files in Directory 
#Coded by @wir3GhOst
import sys,fnmatch,os,glob
from PyPDF2 import PdfFileReader
def count_pages():
   input = sys.argv[1]
   path = input+'/*.pdf'
#def count_pages():
   number =  len(fnmatch.filter(os.listdir(input), '*.pdf'))
   print path   
   total = 0
   files=glob.glob(path)   
   for file in files:     
      f=open(file, 'r')
      pdf_c = PdfFileReader(open(file,'rb'))
      num1 = pdf_c.getNumPages()
      total =  total + num1
      print file +" ==> %d " % num1
      f.readlines()   
      f.close()
   print "Number of PFD Files : %d" % number
   print "Number of Pages is PFD Files : %d" % total


if len(sys.argv) not in [2]:
   print "Dir PATH ???"
   exit()
else: 
    count_pages()
