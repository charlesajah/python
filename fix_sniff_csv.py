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
#-a,-b represents short forms of the arguments while '--' represents its long form
ap.add_argument("-a", "--in_delimiter", type=str)
ap.add_argument("-b", "--in_quote", type=str)

args = vars(ap.parse_args())

if args['in_delimiter']:
    delimiter=args['in_delimiter']
if args['in_quote']:
    quote=args['in_quote']

#print("Sum is {}".format(int(args['-a']) + int(args['-b'])))
#print("Sum is {}".format(int(args['in_delimeter']) + int(args['in_quote'])))
#print("{}".format(args['in_delimeter']))
#print (args.a)
#print (args.b)

with open(r"C:\Users\caj020\Documents\GitHome\PortableGit-2.24.0.2-64-bit.7z\bin\python\orig_csv.csv",newline='') as csvfile:
    ##if the arguments are not supplied we should be able to sniff around inside the file to deduce the format. How Great, don't we love Python
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    #After sniffing around inside the file , let's go back to the start of the file and get bloody ready to read again
    csvfile.seek(0)
    #rd=csv.reader(csvfile, delimiter=delimiter, quotechar=quote)
    rd = csv.reader(csvfile, dialect)
    #rd = csv.reader(csvfile, delimiter="{}".format(args['in_delimiter']), quotechar= "{}".format(args['in_quote']))
    for row in rd:
        print(','.join(row))
        #append each row under iteration into the file
        #Using the 'w' would overwrite the file for each row so 'a' is preferred
        with open(r"C:\Users\caj020\Documents\GitHome\PortableGit-2.24.0.2-64-bit.7z\bin\python\fixed_csv.csv",'a',newline='') as csvfile:
            wrt=csv.writer(csvfile, delimiter="," , quotechar="'", quoting=csv.QUOTE_MINIMAL)
            wrt.writerow(row)
            