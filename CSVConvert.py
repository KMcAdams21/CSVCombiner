import csv
import sys

# If there are no files to combine, exit program with message
if len(sys.argv) == 1:
    print("There is no files to combine.")
    exit()


# Method to append CSV info to output CSV
def appendCSV(fileName, num):
    # Open new file to read and create reader
    with open(fileName, mode="r") as csv_file:
        reader = csv.reader(csv_file)

        # If first document, then write headers. Else skip headers so we don't repeat headers
        if num == 1:
            headers = next(reader)
            headers.append('filename')
            writer.writerow(headers)
        else:
            next(reader)

        # Format column name to fit with standards
        newColName = fileName.removeprefix('./fixtures/')
        newColName = newColName.removesuffix('.csv')

        # Write all content rows to new csv file
        for row in reader:
            row.append(newColName)
            writer.writerow(row)
    # Close file after finished
    csv_file.close()


# Create new file based on requested output file name
newFile = './fixtures/' + sys.argv[-1]

# Create new copy of file
with open(newFile, 'w') as create_new_csv:
    print('hello')

# Reopen file in order to append data to it and create a writer
with open(newFile, mode="a") as new_csv:
    writer = csv.writer(new_csv, lineterminator='\n', quoting=csv.QUOTE_ALL)
    # Loop through each input file and use method to append it to output file
    for i in range(1, len(sys.argv) - 1):
        appendCSV(sys.argv[i], i)
