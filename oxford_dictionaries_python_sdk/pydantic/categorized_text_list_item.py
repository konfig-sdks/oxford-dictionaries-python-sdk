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


class CategorizedTextListItem(BaseModel):
    # A note text
    text: str = Field(alias='text')

    # The descriptive category of the text
    type: str = Field(alias='type')

    # The identifier of the word
    id: typing.Optional[str] = Field(None, alias='id')
    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )