# coding: utf-8
"""
    Oxford Dictionaries

    Oxford Dictionaries, part of the Oxford Language Division, is a leading authority on the English language. It offers a wide range of language resources, including dictionaries, thesauruses, grammar guides, and language learning tools. Oxford Dictionaries provides accurate and up-to-date definitions, word origins, and usage examples to support language comprehension and communication.

    The version of the OpenAPI document: 1.11.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from oxford_dictionaries_python_sdk.client_custom import ClientCustom
from oxford_dictionaries_python_sdk.configuration import Configuration
from oxford_dictionaries_python_sdk.api_client import ApiClient
from oxford_dictionaries_python_sdk.type_util import copy_signature
from oxford_dictionaries_python_sdk.apis.tags.dictionary_entries_api import DictionaryEntriesApi
from oxford_dictionaries_python_sdk.apis.tags.lemmatron_api import LemmatronApi
from oxford_dictionaries_python_sdk.apis.tags.lexi_stats_api import LexiStatsApi
from oxford_dictionaries_python_sdk.apis.tags.search_api import SearchApi
from oxford_dictionaries_python_sdk.apis.tags.the_sentence_dictionary_api import TheSentenceDictionaryApi
from oxford_dictionaries_python_sdk.apis.tags.thesaurus_api import ThesaurusApi
from oxford_dictionaries_python_sdk.apis.tags.translation_api import TranslationApi
from oxford_dictionaries_python_sdk.apis.tags.utility_api import UtilityApi
from oxford_dictionaries_python_sdk.apis.tags.wordlist_api import WordlistApi



class OxfordDictionaries(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.dictionary_entries: DictionaryEntriesApi = DictionaryEntriesApi(api_client)
        self.lemmatron: LemmatronApi = LemmatronApi(api_client)
        self.lexi_stats: LexiStatsApi = LexiStatsApi(api_client)
        self.search: SearchApi = SearchApi(api_client)
        self.the_sentence_dictionary: TheSentenceDictionaryApi = TheSentenceDictionaryApi(api_client)
        self.thesaurus: ThesaurusApi = ThesaurusApi(api_client)
        self.translation: TranslationApi = TranslationApi(api_client)
        self.utility: UtilityApi = UtilityApi(api_client)
        self.wordlist: WordlistApi = WordlistApi(api_client)