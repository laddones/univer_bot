from typing import Optional, List

from modules.api.async_client import HTTPClient
from modules.api.errors import StatusCodeErrorException
from modules.models.api_links import MethodEnum
from modules.models.schema import CreateClientSchema, ClientSchema, UpdateClientSchema, GetLinkSchema, CreateLinkSchema, \
    LinkSchema, CreateLinkClientSchema, LinkClientSchema


class HTTPRequestsMethods:
    POST = 'POST'
    GET = 'GET'
    PUT = 'PUT'
    DELETE = 'DELETE'


class ApiStorage:
    def __init__(self, api_host: str):
        self.api_host = api_host
        self.__http_client = HTTPClient()

    async def __make_request(self, url: str, method: str, **kwargs) -> dict:
        if method == 'POST':
            resp = await self.__http_client.post(url, **kwargs)
        elif method == 'GET':
            resp = await self.__http_client.get(url, **kwargs)
        elif method == 'PUT':
            resp = await self.__http_client.put(url, **kwargs)

        return resp

    async def create_client(self, client_schema: CreateClientSchema) -> ClientSchema:
        url = self.api_host + MethodEnum.USER
        try:
            response_json = await self.__make_request(
                url,
                HTTPRequestsMethods.POST,
                json=client_schema.dict()
            )
        except StatusCodeErrorException:
            Exception("Bad request")
        except Exception as e:
            print(e)
        else:
            return ClientSchema.parse_obj(response_json)

    async def update_client(self, user_schema: CreateClientSchema | UpdateClientSchema) -> ClientSchema:
        url = self.api_host + MethodEnum.USER + str(user_schema.user_id) + '/'
        try:
            response_json = await self.__make_request(
                url,
                HTTPRequestsMethods.PUT,
                json=user_schema.dict()
            )
        except StatusCodeErrorException:
            Exception("Bad request")
        except Exception as e:
            print(e)
        else:
            return ClientSchema.parse_obj(response_json)

    async def get_link(self, user_id: int) -> GetLinkSchema:
        url = self.api_host + MethodEnum.GET_LINK + str(user_id) + '/'
        try:
            response_json = await self.__make_request(
                url,
                HTTPRequestsMethods.GET
            )
        except StatusCodeErrorException:
            Exception("Bad request")
        except Exception as e:
            print(e)
        else:
            return GetLinkSchema.parse_obj(response_json)

    async def create_link(self, link: CreateLinkSchema) -> LinkSchema:
        url = self.api_host + MethodEnum.LINKS
        try:
            response_json = await self.__make_request(
                url,
                HTTPRequestsMethods.POST,
                json=link.dict()
            )
        except StatusCodeErrorException:
            Exception("Bad request")
        except Exception as e:
            print(e)
        else:
            return LinkSchema.parse_obj(response_json)

    async def update_link(self, schema: CreateLinkClientSchema) -> LinkClientSchema:
        url = self.api_host + MethodEnum.LINKS_CLIENT
        try:
            response_json = await self.__make_request(
                url,
                HTTPRequestsMethods.POST,
                json=schema.dict()
            )
        except StatusCodeErrorException:
            Exception("Bad request")
        except Exception as e:
            print(e)
        else:
            return LinkClientSchema.parse_obj(response_json)