# CSV File Combiner
This program combines multiple CSV files into one output file. The output file will contain all the columns from each of the input files, and an additional column "filename" to indicate the source of each row.

## Features
- Combines multiple CSV files into a single file.
- Supports header conservation and combination.
- Written in Python using minimal extra modules.

## How to use
This is a command line program, so it can be run in the command line along with CSV files to combine them. You put input file locations in the command line program call along with the name or location of the output file. If you give the location, the program will use that location as long as it is uses relative pathing. The program is currently incapable of using absolute pathing but that will be fixed soon. If you do not give a location and just give a file name, the program will place it in the same directory as the program.
The format goes:
#### python CSVConvert.py inputfile outputfile
You must use the input file location in the name and you can use as many input files as you want.
For example, if you had three input files you would type:
#### python CSVConvert.py inputFileLocation inputFileLocation inputFileLocation outputFileLocation
However, the last one must be the output file and please only give it the file name in the format name.csv.
To use the unit testing program, you must type:
#### python -m unittest test_CSV.py
This runs through various tests, including creating headers from different combinations of files to creating combined CSV files from various combinations of input files. 

## Example
To combine two input files named file1.csv and file2.csv in the fixtures file and save it as output.csv in the fixtures file, you must type:
#### python CSVConvert.py ./fixtures/file1.csv ./fixtures/file2.csv ./fixtures/output.csv
This will combine file1.csv and file2.csv into a new file named output.csv in the fixtures directory. If I instead just wrote output.csv at the end it would have placed it in the same directory as CSVConvert.py.
