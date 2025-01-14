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

from oxford_dictionaries_python_sdk.pydantic.languages_results_item_source_language import LanguagesResultsItemSourceLanguage
from oxford_dictionaries_python_sdk.pydantic.languages_results_item_target_language import LanguagesResultsItemTargetLanguage

class LanguagesResultsItem(BaseModel):
    # Name of region.
    region: typing.Optional[str] = Field(None, alias='region')

    # Name of source dictionary.
    source: typing.Optional[str] = Field(None, alias='source')

    source_language: typing.Optional[LanguagesResultsItemSourceLanguage] = Field(None, alias='sourceLanguage')

    target_language: typing.Optional[LanguagesResultsItemTargetLanguage] = Field(None, alias='targetLanguage')

    # whether monolingual or bilingual.
    type: typing.Optional[Literal["monolingual", "bilingual"]] = Field(None, alias='type')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
