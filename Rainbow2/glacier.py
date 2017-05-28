#!/usr/bin/python
from createRGB import convert
import sys,getopt
import re
import argparse
from PIL import Image

import time
global inputfile
global outputfile
global trows


def loadingBar(cicles):
    sys.write.out('-')

def prefetch():

    x = 0

    with open(inputfile,'r') as f:
        for line in f:

    	    x+=1


    trows=x

    print
    print (trows)
    im = Image.new("RGB", (7,trows))









if __name__ == "__main__":


    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--inputfile',
                  required=True,
                  help="""Inputfile""")
    parser.add_argument('-o', '--outputfile',
                  required=True,
                  help="""Outputfile""")

args = parser.parse_args()
inputfile=args.inputfile
outputfile=args.outputfile

prefetch()

convert(im)
