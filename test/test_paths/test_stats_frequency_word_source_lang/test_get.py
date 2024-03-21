# coding: utf-8

"""
    Oxford Dictionaries

    Oxford Dictionaries, part of the Oxford Language Division, is a leading authority on the English language. It offers a wide range of language resources, including dictionaries, thesauruses, grammar guides, and language learning tools. Oxford Dictionaries provides accurate and up-to-date definitions, word origins, and usage examples to support language comprehension and communication.

    The version of the OpenAPI document: 1.11.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import oxford_dictionaries_python_sdk
from oxford_dictionaries_python_sdk.paths.stats_frequency_word_source_lang import get
from oxford_dictionaries_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestStatsFrequencyWordSourceLang(ApiTestMixin, unittest.TestCase):
    """
    StatsFrequencyWordSourceLang unit test stubs
        Retrieve the frequency of a word derived from a corpus.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
