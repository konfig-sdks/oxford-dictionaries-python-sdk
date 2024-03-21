# coding: utf-8

"""
    Oxford Dictionaries

    Oxford Dictionaries, part of the Oxford Language Division, is a leading authority on the English language. It offers a wide range of language resources, including dictionaries, thesauruses, grammar guides, and language learning tools. Oxford Dictionaries provides accurate and up-to-date definitions, word origins, and usage examples to support language comprehension and communication.

    The version of the OpenAPI document: 1.11.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from oxford_dictionaries_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from oxford_dictionaries_python_sdk.api_response import AsyncGeneratorResponse
from oxford_dictionaries_python_sdk import api_client, exceptions
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

from oxford_dictionaries_python_sdk.model.stats_word_result_list import StatsWordResultList as StatsWordResultListSchema

from oxford_dictionaries_python_sdk.type.stats_word_result_list import StatsWordResultList

from ...api_client import Dictionary
from oxford_dictionaries_python_sdk.pydantic.stats_word_result_list import StatsWordResultList as StatsWordResultListPydantic

from . import path

# Query params
CorpusSchema = schemas.StrSchema
WordformSchema = schemas.StrSchema
TrueCaseSchema = schemas.StrSchema
LemmaSchema = schemas.StrSchema
LexicalCategorySchema = schemas.StrSchema
GrammaticalFeaturesSchema = schemas.StrSchema
SortSchema = schemas.StrSchema
CollateSchema = schemas.StrSchema
MinFrequencySchema = schemas.Int64Schema
MaxFrequencySchema = schemas.Int64Schema
MinNormalizedFrequencySchema = schemas.Float32Schema
MaxNormalizedFrequencySchema = schemas.Float32Schema
OffsetSchema = schemas.Int64Schema
LimitSchema = schemas.Int64Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'corpus': typing.Union[CorpusSchema, str, ],
        'wordform': typing.Union[WordformSchema, str, ],
        'trueCase': typing.Union[TrueCaseSchema, str, ],
        'lemma': typing.Union[LemmaSchema, str, ],
        'lexicalCategory': typing.Union[LexicalCategorySchema, str, ],
        'grammaticalFeatures': typing.Union[GrammaticalFeaturesSchema, str, ],
        'sort': typing.Union[SortSchema, str, ],
        'collate': typing.Union[CollateSchema, str, ],
        'minFrequency': typing.Union[MinFrequencySchema, decimal.Decimal, int, ],
        'maxFrequency': typing.Union[MaxFrequencySchema, decimal.Decimal, int, ],
        'minNormalizedFrequency': typing.Union[MinNormalizedFrequencySchema, decimal.Decimal, int, float, ],
        'maxNormalizedFrequency': typing.Union[MaxNormalizedFrequencySchema, decimal.Decimal, int, float, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_corpus = api_client.QueryParameter(
    name="corpus",
    style=api_client.ParameterStyle.FORM,
    schema=CorpusSchema,
    explode=True,
)
request_query_wordform = api_client.QueryParameter(
    name="wordform",
    style=api_client.ParameterStyle.FORM,
    schema=WordformSchema,
    explode=True,
)
request_query_true_case = api_client.QueryParameter(
    name="trueCase",
    style=api_client.ParameterStyle.FORM,
    schema=TrueCaseSchema,
    explode=True,
)
request_query_lemma = api_client.QueryParameter(
    name="lemma",
    style=api_client.ParameterStyle.FORM,
    schema=LemmaSchema,
    explode=True,
)
request_query_lexical_category = api_client.QueryParameter(
    name="lexicalCategory",
    style=api_client.ParameterStyle.FORM,
    schema=LexicalCategorySchema,
    explode=True,
)
request_query_grammatical_features = api_client.QueryParameter(
    name="grammaticalFeatures",
    style=api_client.ParameterStyle.FORM,
    schema=GrammaticalFeaturesSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_collate = api_client.QueryParameter(
    name="collate",
    style=api_client.ParameterStyle.FORM,
    schema=CollateSchema,
    explode=True,
)
request_query_min_frequency = api_client.QueryParameter(
    name="minFrequency",
    style=api_client.ParameterStyle.FORM,
    schema=MinFrequencySchema,
    explode=True,
)
request_query_max_frequency = api_client.QueryParameter(
    name="maxFrequency",
    style=api_client.ParameterStyle.FORM,
    schema=MaxFrequencySchema,
    explode=True,
)
request_query_min_normalized_frequency = api_client.QueryParameter(
    name="minNormalizedFrequency",
    style=api_client.ParameterStyle.FORM,
    schema=MinNormalizedFrequencySchema,
    explode=True,
)
request_query_max_normalized_frequency = api_client.QueryParameter(
    name="maxNormalizedFrequency",
    style=api_client.ParameterStyle.FORM,
    schema=MaxNormalizedFrequencySchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
# Path params
SourceLangSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'source_lang': typing.Union[SourceLangSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_source_lang = api_client.PathParameter(
    name="source_lang",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SourceLangSchema,
    required=True,
)
_auth = [
    'appId',
    'appKey',
]
SchemaFor200ResponseBodyApplicationJson = StatsWordResultListSchema
SchemaFor200ResponseBodyTextCsv = StatsWordResultListSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: StatsWordResultList


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: StatsWordResultList


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/csv': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextCsv),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'text/csv',
)


class BaseApi(api_client.Api):

    def _get_word_frequencies_mapped_args(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        grammatical_features: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        collate: typing.Optional[str] = None,
        min_frequency: typing.Optional[int] = None,
        max_frequency: typing.Optional[int] = None,
        min_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        max_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if corpus is not None:
            _query_params["corpus"] = corpus
        if wordform is not None:
            _query_params["wordform"] = wordform
        if true_case is not None:
            _query_params["trueCase"] = true_case
        if lemma is not None:
            _query_params["lemma"] = lemma
        if lexical_category is not None:
            _query_params["lexicalCategory"] = lexical_category
        if grammatical_features is not None:
            _query_params["grammaticalFeatures"] = grammatical_features
        if sort is not None:
            _query_params["sort"] = sort
        if collate is not None:
            _query_params["collate"] = collate
        if min_frequency is not None:
            _query_params["minFrequency"] = min_frequency
        if max_frequency is not None:
            _query_params["maxFrequency"] = max_frequency
        if min_normalized_frequency is not None:
            _query_params["minNormalizedFrequency"] = min_normalized_frequency
        if max_normalized_frequency is not None:
            _query_params["maxNormalizedFrequency"] = max_normalized_frequency
        if offset is not None:
            _query_params["offset"] = offset
        if limit is not None:
            _query_params["limit"] = limit
        if source_lang is not None:
            _path_params["source_lang"] = source_lang
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_word_frequencies_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve a list of frequencies of a word/words derived from a corpus.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_source_lang,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_corpus,
            request_query_wordform,
            request_query_true_case,
            request_query_lemma,
            request_query_lexical_category,
            request_query_grammatical_features,
            request_query_sort,
            request_query_collate,
            request_query_min_frequency,
            request_query_max_frequency,
            request_query_min_normalized_frequency,
            request_query_max_normalized_frequency,
            request_query_offset,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/stats/frequency/words/{source_lang}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_word_frequencies_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve a list of frequencies of a word/words derived from a corpus.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_source_lang,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_corpus,
            request_query_wordform,
            request_query_true_case,
            request_query_lemma,
            request_query_lexical_category,
            request_query_grammatical_features,
            request_query_sort,
            request_query_collate,
            request_query_min_frequency,
            request_query_max_frequency,
            request_query_min_normalized_frequency,
            request_query_max_normalized_frequency,
            request_query_offset,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/stats/frequency/words/{source_lang}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetWordFrequenciesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_word_frequencies(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        grammatical_features: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        collate: typing.Optional[str] = None,
        min_frequency: typing.Optional[int] = None,
        max_frequency: typing.Optional[int] = None,
        min_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        max_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_word_frequencies_mapped_args(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
            grammatical_features=grammatical_features,
            sort=sort,
            collate=collate,
            min_frequency=min_frequency,
            max_frequency=max_frequency,
            min_normalized_frequency=min_normalized_frequency,
            max_normalized_frequency=max_normalized_frequency,
            offset=offset,
            limit=limit,
        )
        return await self._aget_word_frequencies_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_word_frequencies(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        grammatical_features: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        collate: typing.Optional[str] = None,
        min_frequency: typing.Optional[int] = None,
        max_frequency: typing.Optional[int] = None,
        min_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        max_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_word_frequencies_mapped_args(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
            grammatical_features=grammatical_features,
            sort=sort,
            collate=collate,
            min_frequency=min_frequency,
            max_frequency=max_frequency,
            min_normalized_frequency=min_normalized_frequency,
            max_normalized_frequency=max_normalized_frequency,
            offset=offset,
            limit=limit,
        )
        return self._get_word_frequencies_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetWordFrequencies(BaseApi):

    async def aget_word_frequencies(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        grammatical_features: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        collate: typing.Optional[str] = None,
        min_frequency: typing.Optional[int] = None,
        max_frequency: typing.Optional[int] = None,
        min_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        max_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> StatsWordResultListPydantic:
        raw_response = await self.raw.aget_word_frequencies(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
            grammatical_features=grammatical_features,
            sort=sort,
            collate=collate,
            min_frequency=min_frequency,
            max_frequency=max_frequency,
            min_normalized_frequency=min_normalized_frequency,
            max_normalized_frequency=max_normalized_frequency,
            offset=offset,
            limit=limit,
            **kwargs,
        )
        if validate:
            return StatsWordResultListPydantic(**raw_response.body)
        return api_client.construct_model_instance(StatsWordResultListPydantic, raw_response.body)
    
    
    def get_word_frequencies(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        grammatical_features: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        collate: typing.Optional[str] = None,
        min_frequency: typing.Optional[int] = None,
        max_frequency: typing.Optional[int] = None,
        min_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        max_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> StatsWordResultListPydantic:
        raw_response = self.raw.get_word_frequencies(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
            grammatical_features=grammatical_features,
            sort=sort,
            collate=collate,
            min_frequency=min_frequency,
            max_frequency=max_frequency,
            min_normalized_frequency=min_normalized_frequency,
            max_normalized_frequency=max_normalized_frequency,
            offset=offset,
            limit=limit,
        )
        if validate:
            return StatsWordResultListPydantic(**raw_response.body)
        return api_client.construct_model_instance(StatsWordResultListPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        grammatical_features: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        collate: typing.Optional[str] = None,
        min_frequency: typing.Optional[int] = None,
        max_frequency: typing.Optional[int] = None,
        min_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        max_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_word_frequencies_mapped_args(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
            grammatical_features=grammatical_features,
            sort=sort,
            collate=collate,
            min_frequency=min_frequency,
            max_frequency=max_frequency,
            min_normalized_frequency=min_normalized_frequency,
            max_normalized_frequency=max_normalized_frequency,
            offset=offset,
            limit=limit,
        )
        return await self._aget_word_frequencies_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        grammatical_features: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        collate: typing.Optional[str] = None,
        min_frequency: typing.Optional[int] = None,
        max_frequency: typing.Optional[int] = None,
        min_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        max_normalized_frequency: typing.Optional[typing.Union[int, float]] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_word_frequencies_mapped_args(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
            grammatical_features=grammatical_features,
            sort=sort,
            collate=collate,
            min_frequency=min_frequency,
            max_frequency=max_frequency,
            min_normalized_frequency=min_normalized_frequency,
            max_normalized_frequency=max_normalized_frequency,
            offset=offset,
            limit=limit,
        )
        return self._get_word_frequencies_oapg(
            query_params=args.query,
            path_params=args.path,
        )

