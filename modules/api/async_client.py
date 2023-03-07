import aiohttp

from modules.api.errors import StatusCodeErrorException
from modules.api.singleton import Singleton


class HTTPClient(metaclass=Singleton):

	@staticmethod
	async def get(url: str, **kwargs) -> dict:
		async with aiohttp.ClientSession() as session:
			async with session.get(url, **kwargs) as resp:
				if resp.status != 200:
					raise StatusCodeErrorException
				return await resp.json()

	@staticmethod
	async def post(url: str, **kwargs) -> dict:
		async with aiohttp.ClientSession() as session:
			async with session.post(url, **kwargs) as resp:
				if resp.status != 201:
					raise StatusCodeErrorException
				return await resp.json()

	@staticmethod
	async def put(url: str, **kwargs) -> dict:
		async with aiohttp.ClientSession() as session:
			async with session.put(url, **kwargs) as resp:
				if resp.status != 200:
					raise StatusCodeErrorException
				return await resp.json()

