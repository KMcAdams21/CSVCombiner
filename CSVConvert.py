import csv
import sys

# If there are no files to combine, exit program with message
if len(sys.argv) == 1:
    print("There is no files to combine.")
    exit()


# Method to append CSV info to output CSV
def appendCSV(fileName):
    # Open new file to read and create reader
    with open(fileName, mode="r", newline='') as csv_in:
        reader = csv.DictReader(csv_in)

        # Format column name to fit with standards
        newColName = fileName.removeprefix('./fixtures/')
        newColName = newColName.removesuffix('.csv')

        # Write all content rows to new csv file
        for row in reader:
            row["filename"] = newColName
            writer.writerow(row)
    # Close file after finished
    csv_in.close()

# Method to check the headers and determine which are used in the csv files
def headerCheck(inputFiles):
    headerNames = []
    # Go through each file input
    for fileName in inputFiles:
        # Open the file, use a reader to see the headers
        with open(fileName, "r", newline='\n') as fileInput:
            reader = csv.reader(fileInput)
            headers = next(reader)
            # If a header is not currently in the header array, place it in
            for head in headers:
                if head not in headerNames:
                    headerNames.append(head)
    # Return the complete list of headers
    return headerNames

# Create array of file inputs
inputs = sys.argv[1:-1]
output = sys.argv[-1]
print(inputs)

# Getting headers of all files
headers = headerCheck(inputs)

# Inserting filename header in third position
headers.insert(2, 'filename')
print(headers)

# Create new file based on requested output file name
newFile = './fixtures/' + output

# Create new copy of file
with open(newFile, 'w') as create_new_csv:
    print('New File created')
print(headers)
# Reopen file in order to append data to it and create a writer
with open(newFile, mode="w", newline="") as new_csv:
    # Create writer and write first header
    writer = csv.DictWriter(new_csv, fieldnames=headers, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    # Loop through each input file and use method to append it to output file
    for inp in inputs:
        appendCSV(inp)
