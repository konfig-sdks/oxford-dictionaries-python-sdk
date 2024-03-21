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

from oxford_dictionaries_python_sdk.pydantic.arrayofstrings import Arrayofstrings
from oxford_dictionaries_python_sdk.pydantic.categorized_text_list import CategorizedTextList
from oxford_dictionaries_python_sdk.pydantic.cross_references_list import CrossReferencesList
from oxford_dictionaries_python_sdk.pydantic.examples_list import ExamplesList
from oxford_dictionaries_python_sdk.pydantic.pronunciations_list import PronunciationsList
from oxford_dictionaries_python_sdk.pydantic.thesaurus_link import ThesaurusLink
from oxford_dictionaries_python_sdk.pydantic.translations_list import TranslationsList
from oxford_dictionaries_python_sdk.pydantic.variant_forms_list import VariantFormsList

class Sense(BaseModel):
    cross_reference_markers: typing.Optional[Arrayofstrings] = Field(None, alias='crossReferenceMarkers')

    cross_references: typing.Optional[CrossReferencesList] = Field(None, alias='crossReferences')

    definitions: typing.Optional[Arrayofstrings] = Field(None, alias='definitions')

    domains: typing.Optional[Arrayofstrings] = Field(None, alias='domains')

    examples: typing.Optional[ExamplesList] = Field(None, alias='examples')

    # The id of the sense that is required for the delete procedure
    id: typing.Optional[str] = Field(None, alias='id')

    notes: typing.Optional[CategorizedTextList] = Field(None, alias='notes')

    pronunciations: typing.Optional[PronunciationsList] = Field(None, alias='pronunciations')

    regions: typing.Optional[Arrayofstrings] = Field(None, alias='regions')

    registers: typing.Optional[Arrayofstrings] = Field(None, alias='registers')

    short_definitions: typing.Optional[Arrayofstrings] = Field(None, alias='short_definitions')

    # Ordered list of subsenses of a sense
    subsenses: typing.Optional['typing.List["Sense"]'] = Field(None, alias='subsenses')

    # Ordered list of links to the Thesaurus Dictionary
    thesaurus_links: typing.Optional[typing.List[ThesaurusLink]] = Field(None, alias='thesaurusLinks')

    translations: typing.Optional[TranslationsList] = Field(None, alias='translations')

    variant_forms: typing.Optional[VariantFormsList] = Field(None, alias='variantForms')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
