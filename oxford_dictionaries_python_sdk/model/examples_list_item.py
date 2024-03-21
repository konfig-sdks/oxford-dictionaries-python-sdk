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


class ExamplesListItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "text",
        }
        
        class properties:
            text = schemas.StrSchema
        
            @staticmethod
            def definitions() -> typing.Type['Arrayofstrings']:
                return Arrayofstrings
        
            @staticmethod
            def domains() -> typing.Type['Arrayofstrings']:
                return Arrayofstrings
        
            @staticmethod
            def notes() -> typing.Type['CategorizedTextList']:
                return CategorizedTextList
        
            @staticmethod
            def regions() -> typing.Type['Arrayofstrings']:
                return Arrayofstrings
        
            @staticmethod
            def registers() -> typing.Type['Arrayofstrings']:
                return Arrayofstrings
        
            @staticmethod
            def senseIds() -> typing.Type['Arrayofstrings']:
                return Arrayofstrings
        
            @staticmethod
            def translations() -> typing.Type['TranslationsList']:
                return TranslationsList
            __annotations__ = {
                "text": text,
                "definitions": definitions,
                "domains": domains,
                "notes": notes,
                "regions": regions,
                "registers": registers,
                "senseIds": senseIds,
                "translations": translations,
            }
    
    text: MetaOapg.properties.text
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["definitions"]) -> 'Arrayofstrings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domains"]) -> 'Arrayofstrings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> 'CategorizedTextList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regions"]) -> 'Arrayofstrings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registers"]) -> 'Arrayofstrings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["senseIds"]) -> 'Arrayofstrings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["translations"]) -> 'TranslationsList': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["text", "definitions", "domains", "notes", "regions", "registers", "senseIds", "translations", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["definitions"]) -> typing.Union['Arrayofstrings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domains"]) -> typing.Union['Arrayofstrings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union['CategorizedTextList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regions"]) -> typing.Union['Arrayofstrings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registers"]) -> typing.Union['Arrayofstrings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["senseIds"]) -> typing.Union['Arrayofstrings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["translations"]) -> typing.Union['TranslationsList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["text", "definitions", "domains", "notes", "regions", "registers", "senseIds", "translations", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        text: typing.Union[MetaOapg.properties.text, str, ],
        definitions: typing.Union['Arrayofstrings', schemas.Unset] = schemas.unset,
        domains: typing.Union['Arrayofstrings', schemas.Unset] = schemas.unset,
        notes: typing.Union['CategorizedTextList', schemas.Unset] = schemas.unset,
        regions: typing.Union['Arrayofstrings', schemas.Unset] = schemas.unset,
        registers: typing.Union['Arrayofstrings', schemas.Unset] = schemas.unset,
        senseIds: typing.Union['Arrayofstrings', schemas.Unset] = schemas.unset,
        translations: typing.Union['TranslationsList', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExamplesListItem':
        return super().__new__(
            cls,
            *args,
            text=text,
            definitions=definitions,
            domains=domains,
            notes=notes,
            regions=regions,
            registers=registers,
            senseIds=senseIds,
            translations=translations,
            _configuration=_configuration,
            **kwargs,
        )

from oxford_dictionaries_python_sdk.model.arrayofstrings import Arrayofstrings
from oxford_dictionaries_python_sdk.model.categorized_text_list import CategorizedTextList
from oxford_dictionaries_python_sdk.model.translations_list import TranslationsList