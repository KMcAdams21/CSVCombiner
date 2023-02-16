import csv
import sys

# Branch Test

# Method to append CSV info to output CSV
def writeCSV(inFiles, outFile, heads):
    """Given input files and desired output file, combine CSVs and output"""

    # Create new copy of file
    with open(outFile, 'w') as create_new_csv:
        print('Please wait...')
    # Return False if there are not any inputs
    if len(inFiles) == 0:
        print('There are no files to combine')
        return False
    with open(outFile, mode="w", newline="\n") as new_csv:
        # Create writer and write first header
        writer = csv.DictWriter(new_csv, fieldnames=heads, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        # Loop through each input file and use method to append it to output file
        for inp in inFiles:
        # Try to open file. If file does not exist, then continue to next file
            try:
                # Open new file to read and create reader
                with open(inp, mode="r", newline='') as csv_in:
                    reader = csv.DictReader(csv_in)
                    # Format column name to fit with standards
                    newColName = inp.removeprefix('./fixtures/')
                    newColName = newColName.removesuffix('.csv')
                    # Write all content rows to new csv file
                    for row in reader:
                        row["filename"] = newColName
                        writer.writerow(row)
                # Close file after finished
                csv_in.close()
            except FileNotFoundError:
                print(inp + ' was not found')
                continue
    return True

# Method to check the headers and determine which are used in the csv files
def headerCheck(inputFiles):
    """Given a list of input files, find and return header names"""
    headerNames = []
    # Go through each file input
    for fileName in inputFiles:
        # Try to open file, if file does not exist, skip to next one
        try:
            # Open the file, use a reader to see the headers
            with open(fileName, "r", newline='\n') as fileInput:
                reader = csv.reader(fileInput)
                headers = next(reader)
                # If a header is not currently in the header array, place it in
                for head in headers:
                    if head not in headerNames:
                        headerNames.append(head)
        except FileNotFoundError:
            continue
    # Inserting filename header in last position
    headerNames.append('filename')
    # Return the complete list of headers
    return headerNames

def main():
    """ This is the start of the main body of the program """
    # Create array of file inputs and output file
    inputs = sys.argv[1:-1]
    output = sys.argv[-1]
    # Getting headers of all files
    headers = headerCheck(inputs)
    # Adding ./ to put it in same directory if location not given
    if not output.startswith('./') or not output.startswith('../'):
        output = './' + output
    # Using method to write new CSV file from input files
    check = writeCSV(inputs, output, headers)
    # Print finish message
    if check:
        print("The new CSV file has been created!")

if __name__ == '__main__':
    main()
