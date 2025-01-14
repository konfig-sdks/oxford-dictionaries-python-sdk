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


class HeadwordLemmatron(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Description of an inflected form of a word
    """


    class MetaOapg:
        required = {
            "lexicalEntries",
            "language",
            "id",
            "word",
        }
        
        class properties:
            id = schemas.StrSchema
            language = schemas.StrSchema
            
            
            class lexicalEntries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LemmatronLexicalEntry']:
                        return LemmatronLexicalEntry
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['LemmatronLexicalEntry'], typing.List['LemmatronLexicalEntry']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lexicalEntries':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LemmatronLexicalEntry':
                    return super().__getitem__(i)
            word = schemas.StrSchema
            type = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "language": language,
                "lexicalEntries": lexicalEntries,
                "word": word,
                "type": type,
            }
    
    lexicalEntries: MetaOapg.properties.lexicalEntries
    language: MetaOapg.properties.language
    id: MetaOapg.properties.id
    word: MetaOapg.properties.word
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lexicalEntries"]) -> MetaOapg.properties.lexicalEntries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["word"]) -> MetaOapg.properties.word: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "language", "lexicalEntries", "word", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lexicalEntries"]) -> MetaOapg.properties.lexicalEntries: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["word"]) -> MetaOapg.properties.word: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "language", "lexicalEntries", "word", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lexicalEntries: typing.Union[MetaOapg.properties.lexicalEntries, list, tuple, ],
        language: typing.Union[MetaOapg.properties.language, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        word: typing.Union[MetaOapg.properties.word, str, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'HeadwordLemmatron':
        return super().__new__(
            cls,
            *args,
            lexicalEntries=lexicalEntries,
            language=language,
            id=id,
            word=word,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from oxford_dictionaries_python_sdk.model.lemmatron_lexical_entry import LemmatronLexicalEntry
