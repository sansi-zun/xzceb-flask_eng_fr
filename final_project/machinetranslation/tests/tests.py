import unittest

from translator import english_to_french, french_to_english

class Tests(unittest.TestCase):
    
    def test_null(self):
        self.assertEqual(english_to_french(None), None, 
            "null input should result in null output")
        self.assertEqual(french_to_english(None), None, 
            "null input should result in null output")

    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour", 
            "english input should result in correct french output")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello", 
            "french input should result in correct english output")

unittest.main()
