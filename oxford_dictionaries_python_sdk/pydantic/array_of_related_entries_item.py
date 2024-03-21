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

class ArrayOfRelatedEntriesItem(BaseModel):
    # The identifier of the word
    id: str = Field(alias='id')

    text: str = Field(alias='text')

    domains: typing.Optional[Arrayofstrings] = Field(None, alias='domains')

    # IANA language code specifying the language of the word
    language: typing.Optional[str] = Field(None, alias='language')

    regions: typing.Optional[Arrayofstrings] = Field(None, alias='regions')

    registers: typing.Optional[Arrayofstrings] = Field(None, alias='registers')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
