from decimal import Decimal

from corearticle import BaseArticle
from coreenum import StockEnum


class ArticleCybertek(BaseArticle):

    @staticmethod
    def get_article_list(root):
        return (element for element in next(iter(root.find_class("lst_grid")), None).findall('div'))

    @staticmethod
    async def get_article_list_async(root):
        return (element for element in next(iter(root.find_class("lst_grid")), None).findall('div'))

    def _set_title(self, value):
        return value.find("*//h2").text_content()

    def _set_link(self, value):
        return value.find("*//div/a").get('href')

    def _set_stock(self, value):
        avail = StockEnum.STOCK if len(value.find_class("prodfiche_dispo")) > 0 else StockEnum.RUPTURE
        return avail

    def _set_price(self, value):
        price_str = value.find(
            "*//div[@class='grb__liste-produit__liste__produit__achat__prix']/span").text_content()
        price = price_str.replace('€', '.')
        return Decimal(price)
