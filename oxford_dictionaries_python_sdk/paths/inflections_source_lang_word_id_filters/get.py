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

from oxford_dictionaries_python_sdk.model.lemmatron import Lemmatron as LemmatronSchema

from oxford_dictionaries_python_sdk.type.lemmatron import Lemmatron

from ...api_client import Dictionary
from oxford_dictionaries_python_sdk.pydantic.lemmatron import Lemmatron as LemmatronPydantic

from . import path

# Path params


class SourceLangSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "en": "EN",
            "es": "ES",
            "hi": "HI",
            "nso": "NSO",
            "tn": "TN",
            "zu": "ZU",
            "de": "DE",
            "pt": "PT",
        }
    
    @schemas.classproperty
    def EN(cls):
        return cls("en")
    
    @schemas.classproperty
    def ES(cls):
        return cls("es")
    
    @schemas.classproperty
    def HI(cls):
        return cls("hi")
    
    @schemas.classproperty
    def NSO(cls):
        return cls("nso")
    
    @schemas.classproperty
    def TN(cls):
        return cls("tn")
    
    @schemas.classproperty
    def ZU(cls):
        return cls("zu")
    
    @schemas.classproperty
    def DE(cls):
        return cls("de")
    
    @schemas.classproperty
    def PT(cls):
        return cls("pt")


class FiltersSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                regex=[{
                    'pattern': r'(lexicalCategory|grammaticalFeatures)=.+',
                }]

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FiltersSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
WordIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'source_lang': typing.Union[SourceLangSchema, str, ],
        'filters': typing.Union[FiltersSchema, list, tuple, ],
        'word_id': typing.Union[WordIdSchema, str, ],
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
request_path_filters = api_client.PathParameter(
    name="filters",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FiltersSchema,
    required=True,
)
request_path_word_id = api_client.PathParameter(
    name="word_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WordIdSchema,
    required=True,
)
_auth = [
    'appId',
    'appKey',
]
SchemaFor200ResponseBodyApplicationJson = LemmatronSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Lemmatron


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Lemmatron


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
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
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _check_and_retrieve_root_form_mapped_args(
        self,
        source_lang: str,
        filters: typing.List[str],
        word_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if source_lang is not None:
            _path_params["source_lang"] = source_lang
        if filters is not None:
            _path_params["filters"] = filters
        if word_id is not None:
            _path_params["word_id"] = word_id
        args.path = _path_params
        return args

    async def _acheck_and_retrieve_root_form_oapg(
        self,
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
        Check a word exists in the dictionary and retrieve its root form
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_source_lang,
            request_path_filters,
            request_path_word_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/inflections/{source_lang}/{word_id}/{filters}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


    def _check_and_retrieve_root_form_oapg(
        self,
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
        Check a word exists in the dictionary and retrieve its root form
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_source_lang,
            request_path_filters,
            request_path_word_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/inflections/{source_lang}/{word_id}/{filters}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


class CheckAndRetrieveRootFormRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acheck_and_retrieve_root_form(
        self,
        source_lang: str,
        filters: typing.List[str],
        word_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._check_and_retrieve_root_form_mapped_args(
            source_lang=source_lang,
            filters=filters,
            word_id=word_id,
        )
        return await self._acheck_and_retrieve_root_form_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def check_and_retrieve_root_form(
        self,
        source_lang: str,
        filters: typing.List[str],
        word_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._check_and_retrieve_root_form_mapped_args(
            source_lang=source_lang,
            filters=filters,
            word_id=word_id,
        )
        return self._check_and_retrieve_root_form_oapg(
            path_params=args.path,
        )

class CheckAndRetrieveRootForm(BaseApi):

    async def acheck_and_retrieve_root_form(
        self,
        source_lang: str,
        filters: typing.List[str],
        word_id: str,
        validate: bool = False,
        **kwargs,
    ) -> LemmatronPydantic:
        raw_response = await self.raw.acheck_and_retrieve_root_form(
            source_lang=source_lang,
            filters=filters,
            word_id=word_id,
            **kwargs,
        )
        if validate:
            return LemmatronPydantic(**raw_response.body)
        return api_client.construct_model_instance(LemmatronPydantic, raw_response.body)
    
    
    def check_and_retrieve_root_form(
        self,
        source_lang: str,
        filters: typing.List[str],
        word_id: str,
        validate: bool = False,
    ) -> LemmatronPydantic:
        raw_response = self.raw.check_and_retrieve_root_form(
            source_lang=source_lang,
            filters=filters,
            word_id=word_id,
        )
        if validate:
            return LemmatronPydantic(**raw_response.body)
        return api_client.construct_model_instance(LemmatronPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        source_lang: str,
        filters: typing.List[str],
        word_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._check_and_retrieve_root_form_mapped_args(
            source_lang=source_lang,
            filters=filters,
            word_id=word_id,
        )
        return await self._acheck_and_retrieve_root_form_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        source_lang: str,
        filters: typing.List[str],
        word_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._check_and_retrieve_root_form_mapped_args(
            source_lang=source_lang,
            filters=filters,
            word_id=word_id,
        )
        return self._check_and_retrieve_root_form_oapg(
            path_params=args.path,
        )
