import unittest
import CSVConvert
import csv

class TestMethods(unittest.TestCase):


    def test_headers(self):
        """Test the ability for program to get headers from CSV files"""
        # Testing header obtainment from CSVs with same columns
        actual1 = CSVConvert.headerCheck(['./fixtures/accessories.csv',
                                          './fixtures/household_cleaners.csv'])
        expected1 = ['email_hash', 'category', 'filename']
        self.assertEqual(actual1, expected1)

        # Testing header obtainment from CSVs with different columns
        actual2 = CSVConvert.headerCheck(['./fixtures/accessories.csv',
                                          './fixtures/otherColumns.csv'])
        expected2 = ['email_hash', 'category', 'Cat', 'Dog', '12B', 'filename']
        self.assertEqual(actual2, expected2)


    def test_CSV_Create(self):
        """Test the ability for program to create file from
        given input, output, and headers"""
        # Setting up input and output files for readability
        inputFiles = ['./fixtures/small1.csv', './fixtures/small2.csv']
        outputFile = './fixtures/smallCombTest.csv'
        headers = ['abc','def','12','lmn','filename']
        # Running writeCSV method to create output file from normal inputs
        CSVConvert.writeCSV(inputFiles, outputFile, headers)
        # Saving results of created and test file
        data1 = []
        with open('./fixtures/smallComb.csv', 'r') as file1:
            file1read = csv.reader(file1)
            for row in file1read:
                data1.append(row)
        data2 = []
        with open('./fixtures/smallCombTest.csv', 'r') as file2:
            file2read = csv.reader(file2)
            for row in file2read:
                data2.append(row)
        self.assertEqual(data1, data2)

        # Testing program handling of empty input
        emptyInput = []
        emptyOutput = './fixtures/empty.csv'
        CSVConvert.writeCSV(emptyInput, emptyOutput, headers)
        empty1 = []
        with open('./fixtures/empty.csv', 'r') as file1:
            empty1read = csv.reader(file1)
            for row in empty1read:
                data1.append(row)
        empty2 = []
        with open('./fixtures/emptyTest.csv', 'r') as file2:
            empty2read = csv.reader(file2)
            for row in empty2read:
                data2.append(row)
        self.assertEqual(empty1, empty2)
