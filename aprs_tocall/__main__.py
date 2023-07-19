from . import Parser


import unittest

class TestLookupsMethods(unittest.TestCase):
    def setUp(self):
        self.aprs_tocall = Parser()
    def test_specific(self):
        self.assertEqual(self.aprs_tocall.lookup("APWEEA"), 
                            {
                                'tocall': 'APWEE?',
                                'vendor': 'Tom Keffer and Matthew Wall',
                                'model': 'WeeWX Weather Software',
                                'class': 'software',
                                'os': 'Linux/Unix'
                            }
                        )
    def test_exact(self):
        self.assertEqual(self.aprs_tocall.lookup("APRARX"), 
                            {
                                'tocall': 'APRARX',
                                'vendor': 'Open Source',
                                'model': 'radiosonde_auto_rx',
                                'class': 'software',
                                'os': 'Linux/Unix'
                            }
                        )
    def test_lower(self):
        self.assertEqual(self.aprs_tocall.lookup("aprarx"), 
                            {
                                'tocall': 'APRARX',
                                'vendor': 'Open Source',
                                'model': 'radiosonde_auto_rx',
                                'class': 'software',
                                'os': 'Linux/Unix'
                            }
                        )
        
class TestLookupsOnlineMethods(unittest.TestCase):
    def setUp(self):
        self.aprs_tocall = Parser(offline=False)
    def test_specific(self):
        self.assertEqual(self.aprs_tocall.lookup("APWEEA"), 
                            {
                                'tocall': 'APWEE?',
                                'vendor': 'Tom Keffer and Matthew Wall',
                                'model': 'WeeWX Weather Software',
                                'class': 'software',
                                'os': 'Linux/Unix'
                            }
                        )
    def test_exact(self):
        self.assertEqual(self.aprs_tocall.lookup("APRARX"), 
                            {
                                'tocall': 'APRARX',
                                'vendor': 'Open Source',
                                'model': 'radiosonde_auto_rx',
                                'class': 'software',
                                'os': 'Linux/Unix'
                            }
                        )
    def test_lower(self):
        self.assertEqual(self.aprs_tocall.lookup("aprarx"), 
                            {
                                'tocall': 'APRARX',
                                'vendor': 'Open Source',
                                'model': 'radiosonde_auto_rx',
                                'class': 'software',
                                'os': 'Linux/Unix'
                            }
                        )
if __name__ == '__main__':
    unittest.main()