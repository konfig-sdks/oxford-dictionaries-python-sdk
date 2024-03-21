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


class WordlistResultsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Description of found word
    """


    class MetaOapg:
        required = {
            "id",
            "word",
        }
        
        class properties:
            id = schemas.StrSchema
            word = schemas.StrSchema
            
            
            class matchString(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matchString':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            matchType = schemas.StrSchema
            region = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "word": word,
                "matchString": matchString,
                "matchType": matchType,
                "region": region,
            }
        additional_properties = schemas.AnyTypeSchema
    
    id: MetaOapg.properties.id
    word: MetaOapg.properties.word
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["word"]) -> MetaOapg.properties.word: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchString"]) -> MetaOapg.properties.matchString: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchType"]) -> MetaOapg.properties.matchType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["word"], typing_extensions.Literal["matchString"], typing_extensions.Literal["matchType"], typing_extensions.Literal["region"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["word"]) -> MetaOapg.properties.word: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchString"]) -> typing.Union[MetaOapg.properties.matchString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchType"]) -> typing.Union[MetaOapg.properties.matchType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["word"], typing_extensions.Literal["matchString"], typing_extensions.Literal["matchType"], typing_extensions.Literal["region"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        word: typing.Union[MetaOapg.properties.word, str, ],
        matchString: typing.Union[MetaOapg.properties.matchString, None, str, schemas.Unset] = schemas.unset,
        matchType: typing.Union[MetaOapg.properties.matchType, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'WordlistResultsItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            word=word,
            matchString=matchString,
            matchType=matchType,
            region=region,
            _configuration=_configuration,
            **kwargs,
        )