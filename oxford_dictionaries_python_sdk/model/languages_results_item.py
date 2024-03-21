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


class LanguagesResultsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            region = schemas.StrSchema
            source = schemas.StrSchema
        
            @staticmethod
            def sourceLanguage() -> typing.Type['LanguagesResultsItemSourceLanguage']:
                return LanguagesResultsItemSourceLanguage
        
            @staticmethod
            def targetLanguage() -> typing.Type['LanguagesResultsItemTargetLanguage']:
                return LanguagesResultsItemTargetLanguage
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "monolingual": "MONOLINGUAL",
                        "bilingual": "BILINGUAL",
                    }
                
                @schemas.classproperty
                def MONOLINGUAL(cls):
                    return cls("monolingual")
                
                @schemas.classproperty
                def BILINGUAL(cls):
                    return cls("bilingual")
            __annotations__ = {
                "region": region,
                "source": source,
                "sourceLanguage": sourceLanguage,
                "targetLanguage": targetLanguage,
                "type": type,
            }
        min_properties = 1
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceLanguage"]) -> 'LanguagesResultsItemSourceLanguage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetLanguage"]) -> 'LanguagesResultsItemTargetLanguage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["region", "source", "sourceLanguage", "targetLanguage", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceLanguage"]) -> typing.Union['LanguagesResultsItemSourceLanguage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetLanguage"]) -> typing.Union['LanguagesResultsItemTargetLanguage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["region", "source", "sourceLanguage", "targetLanguage", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        sourceLanguage: typing.Union['LanguagesResultsItemSourceLanguage', schemas.Unset] = schemas.unset,
        targetLanguage: typing.Union['LanguagesResultsItemTargetLanguage', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LanguagesResultsItem':
        return super().__new__(
            cls,
            *args,
            region=region,
            source=source,
            sourceLanguage=sourceLanguage,
            targetLanguage=targetLanguage,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from oxford_dictionaries_python_sdk.model.languages_results_item_source_language import LanguagesResultsItemSourceLanguage
from oxford_dictionaries_python_sdk.model.languages_results_item_target_language import LanguagesResultsItemTargetLanguage
