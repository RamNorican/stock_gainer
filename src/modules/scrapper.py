
import bs4
from client import Client
import logging
# get from the chrome web tools console navigator.userAgent

logger = logging.getLogger(__name__)


class Scrapper():
    """
    Scrapes the yahoo finance to get the latest gainers, losers and trenders
    """
    def __init__(self, url, endpoint, count=100) -> None:
        self.url = url
        self.service_type = endpoint
        self.stock_count = count

    async def scrape(self) -> bs4.BeautifulSoup:
        client = Client(
            url=self.url, query_parameters={
                "count": self.stock_count, "offset": 0
            }
        )
        html_text = await client.connect("get")
        soup = bs4.BeautifulSoup(html_text, features='html.parser')
        return soup

    async def get_stock_list(self) -> list:
        soup_obj = await self.scrape()
        price_list = []
        if self.service_type.lower() == "gainers":
            price_list = self.get_gainers(soup_obj)
        elif self.service_type.lower() == "losers":
            price_list = self.get_losers(soup_obj)
        elif self.service_type.lower() == "trending":
            price_list = self.get_trending(soup_obj)
        else:
            logger.info("No market selected")
        return price_list

    def get_gainers(self, soup_obj) -> list:
        """
        Sample output with schema
        [
            {
                'Symbol': 'STLD',
                'Name': 'Steel Dynamics, Inc.',
                'Price (Intraday)': '100.40',
                'Change': '+3.66',
                '% Change': '+3.78%',
                'Volume': '1.537M',
                'Avg Vol (3 month)': '1.749M',
                'Market Cap': '17.627B',
                'PE Ratio (TTM)': '4.44',
                '52 Week Range': None
            }
        ]
        """
        stock_list = []
        table_class = soup_obj.find_all(
            "tr", class_="simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv2BgColor)"
        )
        for item in table_class:
            stock_details = {}
            for cols in item.find_all("td"):
                text = cols.findAll(text=True)
                if len(text) > 0:
                    stock_details[cols.get('aria-label')] = text[0]
                else:
                    stock_details[cols.get('aria-label')] = None
            stock_list.append(stock_details)
        return stock_list

    def get_losers(self, soup_obj) -> list:
        pass

    def get_trending(self, soup) -> list:
        pass
