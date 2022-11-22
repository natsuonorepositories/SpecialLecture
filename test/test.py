import unittest
import sys
sys.path.append('../')
from speciallecture.sample import CSVPrinter

class TESTCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter('sample.csv')
        l = printer.read()
        # len(l) = 3
        self.assertEqual(3,len(l))
        
    def test_read2(self):
        printer = CSVPrinter('sample.csv')
        line = printer.read()
        self.assertEqual('value2B', line[1][1])
        
    def test_read3(self):
        try:
           printer = CSVPrinter('sample2.csv')
           printer.read()
           unittest.TestCase.fail("This line not should be invoked.")
        except:
            print('File name error') 
        

        