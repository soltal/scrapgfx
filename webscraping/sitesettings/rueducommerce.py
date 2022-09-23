from decimal import Decimal, InvalidOperation

from corearticle import BaseArticle
from coreenum import StockEnum


class ArticleRueDuCommerce(BaseArticle):

    @staticmethod
    def get_article_list(root):
        return (element for element in root.findall("*//div[@id='listing-infinite']/article"))

    @staticmethod
    async def get_article_list_async(root):
        return (element for element in root.findall("*//div[@id='listing-infinite']/article"))

    def _set_title(self, value):
        return value.find("*/h2[@class='item__title']/a").get('title')

    def _set_link(self, value):
        return value.find("*/h2[@class='item__title']/a").get('href')

    def _set_stock(self, value):
        return StockEnum.STOCK

    def _set_price(self, value):
        price = -1
        try:
            price = Decimal(value.find("*//p[@class='item__price']/span/meta").get('content').replace(' ', ''))
        except AttributeError:
            try:
                price = Decimal(value.find("*/p[@class='item__price']/meta").get('content').replace(' ', ''))
            except AttributeError:
                price = -1
        except InvalidOperation:
            price = -1
        finally:
            return price
