import csv
import sys

# Branch Test

class CSVreader(object):
    """Class that incorporates varying functionalities of reading CSV files"""
    def __init__(self, file):
        self.file = file

    def read_header(self, currHeaders):
        """Get headers from given file"""
        newHeaders = []
        try:
            # Open the file, use a reader to see the headers
            with open(self.file, "r", newline='\n') as fileInput:
                reader = csv.reader(fileInput)
                headers = next(reader)
                # If a header is not currently in the header array, place it in
                for head in headers:
                    if head not in currHeaders:
                        newHeaders.append(head)
        except FileNotFoundError:
            return False
        return newHeaders

    def read_write_file(self, writer):
        """Read file and write to given file"""
        try:
            # Open new file to read and create reader
            with open(self.file, mode="r", newline='') as csv_in:
                reader = csv.DictReader(csv_in)
                # Format column name to fit with standards
                newColName = self.file.removeprefix('./fixtures/')
                newColName = newColName.removesuffix('.csv')
                # Write all content rows to new csv file
                for row in reader:
                    row["filename"] = newColName
                    writer.writerow(row)
            # Close file after finished
            csv_in.close()
        except FileNotFoundError:
            print(self.file + ' was not found')

class CSVwriter(object):
    """Object that is used to create the new file"""
    def __init__(self, file):
        self.file = file

    def write_file(self, headers):
        with open(self.file, mode="w", newline="\n") as new_csv:
            # Create writer and write first header
            writer = csv.DictWriter(new_csv, fieldnames=headers, quoting=csv.QUOTE_ALL)
            writer.writeheader()

def getHeaders(inputs):
    """Helper function that creates reader class and reads for each file"""
    headers = []
    for file in inputs:
        data = CSVreader(file)
        newHeaders = data.read_header(headers)
        if newHeaders:
            headers += newHeaders
    headers.append('filename')
    return headers

def writeFile(inputs, outFile, headers):
    """Helper function that given all information, writes the new file"""
    output = CSVwriter(outFile)
    output.write_file(headers)

    with open(outFile, mode="a", newline="\n") as new_csv:
        # Create writer and write first header
        write = csv.DictWriter(new_csv, fieldnames=headers, quoting=csv.QUOTE_ALL)
        for inFile in inputs:
            file = CSVreader(inFile)
            file.read_write_file(write)


def main():
    """This is the start of the main body of the program"""
    # Create array of file inputs and output file
    inputs = sys.argv[1:-1]
    output = sys.argv[-1]
    # Adding ./ to put it in same directory if location not given
    if not output.startswith('./') or not output.startswith('../'):
        output = './' + output
    # Get all headers
    headers = getHeaders(inputs)
    # Write to new file
    writeFile(inputs, output, headers)
    print("File has been created")

if __name__ == '__main__':
    main()

