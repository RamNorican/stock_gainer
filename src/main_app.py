from modules.scrapper import Scrapper
import asyncio
from modules.helpers import special_str_to_int, update_keys
from modules.models import ApiResponse

obj = Scrapper("https://finance.yahoo.com/gainers", endpoint="gainers")
stock_list = asyncio.run(obj.get_stock_list())


def normalise_response(stock_list: list) -> ApiResponse:
    if stock_list and len(stock_list) > 0:
        result_list = [update_keys(resp) for resp in stock_list]
        filtered_list = [special_str_to_int(resp) for resp in result_list]
        return ApiResponse(filtered_list)

print(sink_list)
