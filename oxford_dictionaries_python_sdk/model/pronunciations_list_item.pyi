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


class PronunciationsListItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A grouping of pronunciation information
    """


    class MetaOapg:
        
        class properties:
            audioFile = schemas.StrSchema
        
            @staticmethod
            def dialects() -> typing.Type['Arrayofstrings']:
                return Arrayofstrings
            phoneticNotation = schemas.StrSchema
            phoneticSpelling = schemas.StrSchema
        
            @staticmethod
            def regions() -> typing.Type['Arrayofstrings']:
                return Arrayofstrings
            __annotations__ = {
                "audioFile": audioFile,
                "dialects": dialects,
                "phoneticNotation": phoneticNotation,
                "phoneticSpelling": phoneticSpelling,
                "regions": regions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audioFile"]) -> MetaOapg.properties.audioFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dialects"]) -> 'Arrayofstrings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneticNotation"]) -> MetaOapg.properties.phoneticNotation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneticSpelling"]) -> MetaOapg.properties.phoneticSpelling: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regions"]) -> 'Arrayofstrings': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["audioFile", "dialects", "phoneticNotation", "phoneticSpelling", "regions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audioFile"]) -> typing.Union[MetaOapg.properties.audioFile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dialects"]) -> typing.Union['Arrayofstrings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneticNotation"]) -> typing.Union[MetaOapg.properties.phoneticNotation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneticSpelling"]) -> typing.Union[MetaOapg.properties.phoneticSpelling, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regions"]) -> typing.Union['Arrayofstrings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["audioFile", "dialects", "phoneticNotation", "phoneticSpelling", "regions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        audioFile: typing.Union[MetaOapg.properties.audioFile, str, schemas.Unset] = schemas.unset,
        dialects: typing.Union['Arrayofstrings', schemas.Unset] = schemas.unset,
        phoneticNotation: typing.Union[MetaOapg.properties.phoneticNotation, str, schemas.Unset] = schemas.unset,
        phoneticSpelling: typing.Union[MetaOapg.properties.phoneticSpelling, str, schemas.Unset] = schemas.unset,
        regions: typing.Union['Arrayofstrings', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PronunciationsListItem':
        return super().__new__(
            cls,
            *args,
            audioFile=audioFile,
            dialects=dialects,
            phoneticNotation=phoneticNotation,
            phoneticSpelling=phoneticSpelling,
            regions=regions,
            _configuration=_configuration,
            **kwargs,
        )

from oxford_dictionaries_python_sdk.model.arrayofstrings import Arrayofstrings