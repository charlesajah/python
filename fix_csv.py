# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:57:19 2020
@author: Charles Ajah
"""

import argparse
import csv

#Build a Constructor from the ArgumentParser
ap=argparse.ArgumentParser()

#define the arguments for the parser
ap.add_argument("-a", "--in_delimiter", type=str, required=True)
ap.add_argument("-b", "--in_quote", type=str, required=True)
args = vars(ap.parse_args())


#print("Sum is {}".format(int(args['-a']) + int(args['-b'])))
#print("Sum is {}".format(int(args['in_delimeter']) + int(args['in_quote'])))
#print("{}".format(args['in_delimeter']))
#print (args.a)
#print (args.b)

with open(r"C:\Users\caj020\Documents\GitHome\PortableGit-2.24.0.2-64-bit.7z\bin\python\orig_csv.csv",newline='') as csvfile:
    rd = csv.reader(csvfile, delimiter="{}".format(args['in_delimiter']), quotechar= "{}".format(args['in_quote']))
    for row in rd:
        print(','.join(row))