# CSV File Combiner
A program for combining multiple CSV files into a single file.

## Features
- Combines multiple CSV files into a single file.
- Supports header conservation and combination.
- Written in Python using minimal extra modules.

## How to use
This is a command line program, so it can be run in the command line along with CSV files to combine them.
The format goes:
##### python CSVConvert.py inputfile inputfile inputfile outputfile
You must use the input file location in the name and you can use as many input files as you want.
However, the last one must be the output file and please only give it the file name in the format name.csv
To use the unit testing program, you must type:
##### python -m unittest test_CSV.py
This runs through various tests, including creating headers from different combinations of files to creating combined CSV files from various combinations of input files. 
