
import bs4
import asyncio


from client import Client
# get from the chrome web tools console navigator.userAgent


class Scrapper():
    """
    Scrapes the yahoo finance to get the latest gainers, losers and trenders
    """
    def __init__(self, url, endpoint) -> None:
        self.url = url
        self.service_type = endpoint

    async def scrape(self) -> bs4.BeautifulSoup:
        client = Client(self.url)
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
            print("No market selected")
        return price_list

    def get_gainers(self, soup_obj) -> list:
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


obj = Scrapper("https://finance.yahoo.com/gainers", endpoint="gainers")
stock_list = asyncio.run(obj.get_stock_list())
print(stock_list)
