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


class GrammaticalFeaturesList(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The different forms are correlated with meanings or functions which we text as 'features'
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['GrammaticalFeaturesListItem']:
            return GrammaticalFeaturesListItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['GrammaticalFeaturesListItem'], typing.List['GrammaticalFeaturesListItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'GrammaticalFeaturesList':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'GrammaticalFeaturesListItem':
        return super().__getitem__(i)

from oxford_dictionaries_python_sdk.model.grammatical_features_list_item import GrammaticalFeaturesListItem
