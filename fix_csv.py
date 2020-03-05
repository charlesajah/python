# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:57:19 2020

@author: Charles Ajah
"""

import argparse

#Build a Constructor from the ArgumentParser
ap=argparse.ArgumentParser()

#define the arguments for the parser
ap.add_argument("-a", "--in-delimeter", required=True)
ap.add_argument("-b", "--in-quote", required=True, help="You ,ust supply Second operand")
args = vars(ap.parse_args())


#print("Sum is {}".format(int(args['-a']) + int(args['-b'])))
print("Sum is {}".format(int(args['in-delimeter']) + int(args['in-quote'])))
