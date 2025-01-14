# coding: utf-8

"""
    Oxford Dictionaries

    Oxford Dictionaries, part of the Oxford Language Division, is a leading authority on the English language. It offers a wide range of language resources, including dictionaries, thesauruses, grammar guides, and language learning tools. Oxford Dictionaries provides accurate and up-to-date definitions, word origins, and usage examples to support language comprehension and communication.

    The version of the OpenAPI document: 1.11.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from oxford_dictionaries_python_sdk import OxfordDictionaries

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        oxforddictionaries = OxfordDictionaries(
        
                        app_id = 'YOUR_API_KEY',
        
                        app_key = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(oxforddictionaries)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
