import csv
import argparse

parser=argparse.ArgumentParser(description='Accept Command line arguments and parse them accordingly')
parser.add_argument('a', type=str, help= 'Input for the File Delimeter')
parser.add_argument('b', type=str, help= 'Input for the Quote Character')

args=parser.parse_args()

print ('The First Argument is '+ args.a)

with open(r"C:\Users\caj020\Documents\GitHome\PortableGit-2.24.0.2-64-bit.7z\bin\python\orig_csv.csv",newline='') as csvfile:
    rd=csv.reader(csvfile, delimiter=args.a, quotechar=args.b)
    for row in rd:
        print(','.join(row))
        with open(r"C:\Users\caj020\Documents\GitHome\PortableGit-2.24.0.2-64-bit.7z\bin\python\fixed_csv.csv",'w',newline='') as csvfile:
            wrt=csv.writer(csvfile, delimiter=",", quotechar=args.b, quoting=csv.QUOTE_MINIMAL)
            wrt.writerow(row)