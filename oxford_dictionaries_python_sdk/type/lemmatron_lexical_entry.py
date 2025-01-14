# coding: utf-8

"""
    Oxford Dictionaries

    Oxford Dictionaries, part of the Oxford Language Division, is a leading authority on the English language. It offers a wide range of language resources, including dictionaries, thesauruses, grammar guides, and language learning tools. Oxford Dictionaries provides accurate and up-to-date definitions, word origins, and usage examples to support language comprehension and communication.

    The version of the OpenAPI document: 1.11.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from oxford_dictionaries_python_sdk.type.grammatical_features_list import GrammaticalFeaturesList
from oxford_dictionaries_python_sdk.type.inflections_list import InflectionsList

class RequiredLemmatronLexicalEntry(TypedDict):
    inflectionOf: InflectionsList

    # IANA language code
    language: str

    # A linguistic category of words (or more precisely lexical items), generally defined by the syntactic or morphological behaviour of the lexical item in question, such as noun or verb
    lexicalCategory: str

    # A given written or spoken realisation of a an entry.
    text: str

class OptionalLemmatronLexicalEntry(TypedDict, total=False):
    grammaticalFeatures: GrammaticalFeaturesList

class LemmatronLexicalEntry(RequiredLemmatronLexicalEntry, OptionalLemmatronLexicalEntry):
    pass
