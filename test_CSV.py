import unittest
import CSVConvert
import csv

class TestMethods(unittest.TestCase):

    def test_headers(self):
        actual1 = CSVConvert.headerCheck(['./fixtures/accessories.csv'])
        expected1 = ['email_hash', 'category', 'filename']
        self.assertEqual(actual1, expected1)

        actual2 = CSVConvert.headerCheck(['./fixtures/accessories.csv', './fixtures/otherColumns.csv'])
        expected2 = ['email_hash', 'category', 'Cat', 'Dog', '12B', 'filename']
        self.assertEqual(actual2, expected2)

    def test_CSV_Create(self):
        inputFiles = ['./fixtures/small1.csv', './fixtures/small2.csv']
        outputFile = './fixtures/smallCombTest.csv'
        headers = ['abc','def','12','lmn','filename']
        CSVConvert.writeCSV(inputFiles, outputFile, headers)
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
