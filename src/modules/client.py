import httpx
import logging

logger = logging.getLogger(__name__)


class Client(object):
    def __init__(self, **kwargs) -> None:
        self.url = kwargs.get("url")
        self.query_parameters = kwargs.get("query_parameters")

    async def get_request(self):
        header = {
            'User-Agent': 'my-app/0.0.1'
        }

        try:
            async with httpx.AsyncClient() as session:
                # await until the response is received
                params = self.query_parameters
                response = await session.get(
                    self.url, headers=header, params=params
                )
                if response.status_code == 200:
                    return response.text
        except httpx.ConnectError as e:
            logger.error("Received the following Connection Error", str(e))
        except Exception as e:
            logger.error(f"Received the following error during api call {e}")

    async def connect(self, request_type):
        if request_type.lower() == "get":
            return await self.get_request()
