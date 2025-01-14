# coding: utf-8

"""
    Oxford Dictionaries

    Oxford Dictionaries, part of the Oxford Language Division, is a leading authority on the English language. It offers a wide range of language resources, including dictionaries, thesauruses, grammar guides, and language learning tools. Oxford Dictionaries provides accurate and up-to-date definitions, word origins, and usage examples to support language comprehension and communication.

    The version of the OpenAPI document: 1.11.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from oxford_dictionaries_python_sdk import schemas  # noqa: F401


class StatsWordResultListResultsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Statistical information about a word
    """


    class MetaOapg:
        required = {
            "normalizedFrequency",
            "wordform",
            "lexicalCategory",
            "lemma",
            "trueCase",
            "frequency",
        }
        
        class properties:
            frequency = schemas.IntSchema
            lemma = schemas.StrSchema
            lexicalCategory = schemas.StrSchema
            normalizedFrequency = schemas.IntSchema
            trueCase = schemas.StrSchema
            wordform = schemas.StrSchema
            __annotations__ = {
                "frequency": frequency,
                "lemma": lemma,
                "lexicalCategory": lexicalCategory,
                "normalizedFrequency": normalizedFrequency,
                "trueCase": trueCase,
                "wordform": wordform,
            }
        additional_properties = schemas.AnyTypeSchema
    
    normalizedFrequency: MetaOapg.properties.normalizedFrequency
    wordform: MetaOapg.properties.wordform
    lexicalCategory: MetaOapg.properties.lexicalCategory
    lemma: MetaOapg.properties.lemma
    trueCase: MetaOapg.properties.trueCase
    frequency: MetaOapg.properties.frequency
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedFrequency"]) -> MetaOapg.properties.normalizedFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wordform"]) -> MetaOapg.properties.wordform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lexicalCategory"]) -> MetaOapg.properties.lexicalCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lemma"]) -> MetaOapg.properties.lemma: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trueCase"]) -> MetaOapg.properties.trueCase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["normalizedFrequency"], typing_extensions.Literal["wordform"], typing_extensions.Literal["lexicalCategory"], typing_extensions.Literal["lemma"], typing_extensions.Literal["trueCase"], typing_extensions.Literal["frequency"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedFrequency"]) -> MetaOapg.properties.normalizedFrequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wordform"]) -> MetaOapg.properties.wordform: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lexicalCategory"]) -> MetaOapg.properties.lexicalCategory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lemma"]) -> MetaOapg.properties.lemma: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trueCase"]) -> MetaOapg.properties.trueCase: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["normalizedFrequency"], typing_extensions.Literal["wordform"], typing_extensions.Literal["lexicalCategory"], typing_extensions.Literal["lemma"], typing_extensions.Literal["trueCase"], typing_extensions.Literal["frequency"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        normalizedFrequency: typing.Union[MetaOapg.properties.normalizedFrequency, decimal.Decimal, int, ],
        wordform: typing.Union[MetaOapg.properties.wordform, str, ],
        lexicalCategory: typing.Union[MetaOapg.properties.lexicalCategory, str, ],
        lemma: typing.Union[MetaOapg.properties.lemma, str, ],
        trueCase: typing.Union[MetaOapg.properties.trueCase, str, ],
        frequency: typing.Union[MetaOapg.properties.frequency, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'StatsWordResultListResultsItem':
        return super().__new__(
            cls,
            *args,
            normalizedFrequency=normalizedFrequency,
            wordform=wordform,
            lexicalCategory=lexicalCategory,
            lemma=lemma,
            trueCase=trueCase,
            frequency=frequency,
            _configuration=_configuration,
            **kwargs,
        )
