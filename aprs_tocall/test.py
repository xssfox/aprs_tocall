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
    def test_wild(self):
        self.assertEqual(self.aprs_tocall.lookup("APTTAA"), 
                            {
                                'tocall': 'APTT*',
                                'vendor': 'Byonics',
                                'model': 'TinyTrak',
                                'class': 'tracker'
                            }
                        )        
    def test_n(self):
        self.assertEqual(self.aprs_tocall.lookup("APCCCD"), 
                            {
                                'tocall': 'APC???',
                                'vendor': 'Rob Wittner, KZ5RW',
                                'model': 'APRS/CE',
                                'class': 'app'
                            }
                        )   
    def test_n2(self):
        self.assertEqual(self.aprs_tocall.lookup("AP123U"), 
                            {
                                'tocall': 'APnnnU',
                                'vendor': 'Painter Engineering',
                                'model': 'uSmartDigi Digipeater',
                                'class': 'digi'
                            }
                        )     
    def test_n3(self):
        self.assertEqual(self.aprs_tocall.lookup("AP123D"), 
                            {
                                'tocall': 'APnnnD',
                                'vendor': 'Painter Engineering',
                                'model': 'uSmartDigi D-Gate',
                                'class': 'dstar'
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