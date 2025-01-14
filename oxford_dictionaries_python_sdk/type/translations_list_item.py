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

from oxford_dictionaries_python_sdk.type.arrayofstrings import Arrayofstrings
from oxford_dictionaries_python_sdk.type.categorized_text_list import CategorizedTextList
from oxford_dictionaries_python_sdk.type.grammatical_features_list import GrammaticalFeaturesList

class RequiredTranslationsListItem(TypedDict):
    # IANA language code specifying the language of the translation
    language: str

    text: str

class OptionalTranslationsListItem(TypedDict, total=False):
    domains: Arrayofstrings

    grammaticalFeatures: GrammaticalFeaturesList

    notes: CategorizedTextList

    regions: Arrayofstrings

    registers: Arrayofstrings

class TranslationsListItem(RequiredTranslationsListItem, OptionalTranslationsListItem):
    pass
