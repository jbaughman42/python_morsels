"""
fix_csv
Created November 12, 2019 by Jennifer Baughman

Description: This week we're going to normalize CSV files by writing a program, fix_csv.py,
that turns a pipe-delimited file into a comma-delimited file. I'll explain how it should work by
example.

Your original file will look like this:

Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
You'll then run your script by typing this at the command line:

$ python fix_csv.py cars-original.csv cars.csv
Note : "$" is not typed; that is simply the beginning of the prompt.

Your fixed file should then look like this:

Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
"""

import csv
import argparse


def parse():
    parser = argparse.ArgumentParser(description="Input and output file for CSV processing.")
    parser.add_argument("in_file", type=str, help="Input file requiring fixing.")
    parser.add_argument("out_file", type=str, help="Output corrected file.")
    parser.add_argument("--in-delimiter", type=str, help="Define input delimiter.",
                        dest="delimiter", required=False)
    parser.add_argument("--in-quote", type=str, help="Define input quote character.",
                        dest="quote", required=False, default='"')
    args = parser.parse_args()
    return args


def main():
    args = parse()
    data = []
    delimiter = args.delimiter if args.delimiter else "|"
    with open(args.in_file, newline='') as in_file:
        reader = csv.reader(in_file, delimiter=delimiter, quotechar=args.quote)
        data = [line for line in reader]
    with open(args.out_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file, quoting=csv.QUOTE_MINIMAL, quotechar=args.quote)
        writer.writerows(data)


if __name__ == "__main__":
    main()
