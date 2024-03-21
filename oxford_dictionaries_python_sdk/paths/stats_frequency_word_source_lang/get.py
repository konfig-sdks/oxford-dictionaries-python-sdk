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

from oxford_dictionaries_python_sdk.model.stats_word_result import StatsWordResult as StatsWordResultSchema

from oxford_dictionaries_python_sdk.type.stats_word_result import StatsWordResult

from ...api_client import Dictionary
from oxford_dictionaries_python_sdk.pydantic.stats_word_result import StatsWordResult as StatsWordResultPydantic

from . import path

# Query params
CorpusSchema = schemas.StrSchema
WordformSchema = schemas.StrSchema
TrueCaseSchema = schemas.StrSchema
LemmaSchema = schemas.StrSchema
LexicalCategorySchema = schemas.StrSchema
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
SchemaFor200ResponseBodyApplicationJson = StatsWordResultSchema
SchemaFor200ResponseBodyTextCsv = StatsWordResultSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: StatsWordResult


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: StatsWordResult


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

    def _get_word_frequency_mapped_args(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
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
        if source_lang is not None:
            _path_params["source_lang"] = source_lang
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_word_frequency_oapg(
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
        Retrieve the frequency of a word derived from a corpus.
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
            path_template='/stats/frequency/word/{source_lang}',
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


    def _get_word_frequency_oapg(
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
        Retrieve the frequency of a word derived from a corpus.
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
            path_template='/stats/frequency/word/{source_lang}',
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


class GetWordFrequencyRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_word_frequency(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_word_frequency_mapped_args(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
        )
        return await self._aget_word_frequency_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_word_frequency(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_word_frequency_mapped_args(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
        )
        return self._get_word_frequency_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetWordFrequency(BaseApi):

    async def aget_word_frequency(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> StatsWordResultPydantic:
        raw_response = await self.raw.aget_word_frequency(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
            **kwargs,
        )
        if validate:
            return StatsWordResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(StatsWordResultPydantic, raw_response.body)
    
    
    def get_word_frequency(
        self,
        source_lang: str,
        corpus: typing.Optional[str] = None,
        wordform: typing.Optional[str] = None,
        true_case: typing.Optional[str] = None,
        lemma: typing.Optional[str] = None,
        lexical_category: typing.Optional[str] = None,
        validate: bool = False,
    ) -> StatsWordResultPydantic:
        raw_response = self.raw.get_word_frequency(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
        )
        if validate:
            return StatsWordResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(StatsWordResultPydantic, raw_response.body)


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
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_word_frequency_mapped_args(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
        )
        return await self._aget_word_frequency_oapg(
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
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_word_frequency_mapped_args(
            source_lang=source_lang,
            corpus=corpus,
            wordform=wordform,
            true_case=true_case,
            lemma=lemma,
            lexical_category=lexical_category,
        )
        return self._get_word_frequency_oapg(
            query_params=args.query,
            path_params=args.path,
        )
