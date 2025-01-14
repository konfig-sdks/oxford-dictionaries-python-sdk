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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from oxford_dictionaries_python_sdk.pydantic.array_of_related_entries import ArrayOfRelatedEntries
from oxford_dictionaries_python_sdk.pydantic.categorized_text_list import CategorizedTextList
from oxford_dictionaries_python_sdk.pydantic.entry import Entry
from oxford_dictionaries_python_sdk.pydantic.grammatical_features_list import GrammaticalFeaturesList
from oxford_dictionaries_python_sdk.pydantic.pronunciations_list import PronunciationsList
from oxford_dictionaries_python_sdk.pydantic.variant_forms_list import VariantFormsList

class LexicalEntry(BaseModel):
    # IANA language code
    language: str = Field(alias='language')

    # A linguistic category of words (or more precisely lexical items), generally defined by the syntactic or morphological behaviour of the lexical item in question, such as noun or verb
    lexical_category: str = Field(alias='lexicalCategory')

    # A given written or spoken realisation of a an entry.
    text: str = Field(alias='text')

    derivative_of: typing.Optional[ArrayOfRelatedEntries] = Field(None, alias='derivativeOf')

    derivatives: typing.Optional[ArrayOfRelatedEntries] = Field(None, alias='derivatives')

    entries: typing.Optional[typing.List[Entry]] = Field(None, alias='entries')

    grammatical_features: typing.Optional[GrammaticalFeaturesList] = Field(None, alias='grammaticalFeatures')

    notes: typing.Optional[CategorizedTextList] = Field(None, alias='notes')

    pronunciations: typing.Optional[PronunciationsList] = Field(None, alias='pronunciations')

    variant_forms: typing.Optional[VariantFormsList] = Field(None, alias='variantForms')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
