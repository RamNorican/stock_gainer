from scrapper import Scrapper
import asyncio
from helpers import special_str_to_int, update_keys
from models import ApiResponse

obj = Scrapper("https://finance.yahoo.com/gainers", endpoint="gainers")
stock_list = asyncio.run(obj.get_stock_list())
if stock_list and len(stock_list) > 0:
    result_list = [update_keys(resp) for resp in stock_list]
    filtered_list = [special_str_to_int(resp) for resp in result_list]
    sink_list = ApiResponse(filtered_list)

print(sink_list)
