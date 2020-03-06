# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:57:19 2020
@author: Charles Ajah
"""

import argparse

#Build a Constructor from the ArgumentParser
ap=argparse.ArgumentParser()

#define the arguments for the parser
ap.add_argument("-a", "--in_delimeter", required=True)
ap.add_argument("-b", "--in_quote", required=True)
args = vars(ap.parse_args())


#print("Sum is {}".format(int(args['-a']) + int(args['-b'])))
print("Sum is {}".format(int(args['in_delimeter']) + int(args['in_quote'])))