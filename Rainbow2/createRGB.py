#!/usr/bin/python

import sys,getopt
import re
from PIL import Image



def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

i=0
x=0
y=0
print (inputfile,outputfile)
im = Image.new("RGB", (7,72193))
pix = im.load()



with open(inputfile ,'r') as f:
    for line in f:
        for word in line.split():
           lst=(re.findall('..',word))
    	   #print (lst)
    	   lst.append('00')
    	   lst.append('00')
    	   for i in range(0,19,3):
    	  	 R=int(lst[i],16)
    	   	 G=int(lst[i+1],16)
    	   	 B=int(lst[i+2],16)
    		 #print R,G,B
    		 #R=0
    		 #G=0
    		 #B=0
    		 pix[x,y]=(R,G,B)
    		 #print x,y
    		 x+=1
	x=0
	i=0
	#print "-----"
	y+=1
	print y



im.save(outputfile+".png","png", optimize= True,compress_level = 9,quality = 0)


if __name__ == "__main__":
   main(sys.argv[1:])
