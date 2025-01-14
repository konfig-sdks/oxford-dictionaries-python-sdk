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

from oxford_dictionaries_python_sdk.model.utility_labels import UtilityLabels as UtilityLabelsSchema

from oxford_dictionaries_python_sdk.type.utility_labels import UtilityLabels

from ...api_client import Dictionary
from oxford_dictionaries_python_sdk.pydantic.utility_labels import UtilityLabels as UtilityLabelsPydantic

from . import path

# Path params


class SourceDomainsLanguageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "en": "EN",
            "es": "ES",
            "nso": "NSO",
            "zu": "ZU",
            "ur": "UR",
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
    def NSO(cls):
        return cls("nso")
    
    @schemas.classproperty
    def ZU(cls):
        return cls("zu")
    
    @schemas.classproperty
    def UR(cls):
        return cls("ur")
    
    @schemas.classproperty
    def DE(cls):
        return cls("de")
    
    @schemas.classproperty
    def PT(cls):
        return cls("pt")


class TargetDomainsLanguageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "es": "ES",
            "nso": "NSO",
            "zu": "ZU",
            "ms": "MS",
            "id": "ID",
            "tn": "TN",
            "ro": "RO",
            "de": "DE",
            "pt": "PT",
        }
    
    @schemas.classproperty
    def ES(cls):
        return cls("es")
    
    @schemas.classproperty
    def NSO(cls):
        return cls("nso")
    
    @schemas.classproperty
    def ZU(cls):
        return cls("zu")
    
    @schemas.classproperty
    def MS(cls):
        return cls("ms")
    
    @schemas.classproperty
    def ID(cls):
        return cls("id")
    
    @schemas.classproperty
    def TN(cls):
        return cls("tn")
    
    @schemas.classproperty
    def RO(cls):
        return cls("ro")
    
    @schemas.classproperty
    def DE(cls):
        return cls("de")
    
    @schemas.classproperty
    def PT(cls):
        return cls("pt")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'source_domains_language': typing.Union[SourceDomainsLanguageSchema, str, ],
        'target_domains_language': typing.Union[TargetDomainsLanguageSchema, str, ],
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


request_path_source_domains_language = api_client.PathParameter(
    name="source_domains_language",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SourceDomainsLanguageSchema,
    required=True,
)
request_path_target_domains_language = api_client.PathParameter(
    name="target_domains_language",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TargetDomainsLanguageSchema,
    required=True,
)
_auth = [
    'appId',
    'appKey',
]
SchemaFor200ResponseBodyApplicationJson = UtilityLabelsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UtilityLabels


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UtilityLabels


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_available_domains_mapped_args(
        self,
        source_domains_language: str,
        target_domains_language: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if source_domains_language is not None:
            _path_params["source_domains_language"] = source_domains_language
        if target_domains_language is not None:
            _path_params["target_domains_language"] = target_domains_language
        args.path = _path_params
        return args

    async def _alist_available_domains_oapg(
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
        Lists available domains in a bilingual dataset
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_source_domains_language,
            request_path_target_domains_language,
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
            path_template='/domains/{source_domains_language}/{target_domains_language}',
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


    def _list_available_domains_oapg(
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
        Lists available domains in a bilingual dataset
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_source_domains_language,
            request_path_target_domains_language,
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
            path_template='/domains/{source_domains_language}/{target_domains_language}',
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


class ListAvailableDomainsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_available_domains(
        self,
        source_domains_language: str,
        target_domains_language: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_available_domains_mapped_args(
            source_domains_language=source_domains_language,
            target_domains_language=target_domains_language,
        )
        return await self._alist_available_domains_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def list_available_domains(
        self,
        source_domains_language: str,
        target_domains_language: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_available_domains_mapped_args(
            source_domains_language=source_domains_language,
            target_domains_language=target_domains_language,
        )
        return self._list_available_domains_oapg(
            path_params=args.path,
        )

class ListAvailableDomains(BaseApi):

    async def alist_available_domains(
        self,
        source_domains_language: str,
        target_domains_language: str,
        validate: bool = False,
        **kwargs,
    ) -> UtilityLabelsPydantic:
        raw_response = await self.raw.alist_available_domains(
            source_domains_language=source_domains_language,
            target_domains_language=target_domains_language,
            **kwargs,
        )
        if validate:
            return UtilityLabelsPydantic(**raw_response.body)
        return api_client.construct_model_instance(UtilityLabelsPydantic, raw_response.body)
    
    
    def list_available_domains(
        self,
        source_domains_language: str,
        target_domains_language: str,
        validate: bool = False,
    ) -> UtilityLabelsPydantic:
        raw_response = self.raw.list_available_domains(
            source_domains_language=source_domains_language,
            target_domains_language=target_domains_language,
        )
        if validate:
            return UtilityLabelsPydantic(**raw_response.body)
        return api_client.construct_model_instance(UtilityLabelsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        source_domains_language: str,
        target_domains_language: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_available_domains_mapped_args(
            source_domains_language=source_domains_language,
            target_domains_language=target_domains_language,
        )
        return await self._alist_available_domains_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        source_domains_language: str,
        target_domains_language: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_available_domains_mapped_args(
            source_domains_language=source_domains_language,
            target_domains_language=target_domains_language,
        )
        return self._list_available_domains_oapg(
            path_params=args.path,
        )

