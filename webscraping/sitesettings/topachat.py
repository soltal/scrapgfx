from decimal import Decimal

from webscraping.corearticle import BaseArticle

from webscraping.coreenum import StockEnum


class ArticleTopAchat(BaseArticle):

    @staticmethod
    def get_article_list(root):
        return (element for element in root.find_class('grille-produit'))

    @staticmethod
    async def get_article_list_async(root):
        return (element for element in root.find_class('grille-produit'))

    def _set_title(self, value):
        return value.findtext("*//div[@class='libelle']*/h3")

    def _set_link(self, value):
        return value.find("*//div[@class='libelle']/a").get('href')

    def _set_stock(self, value):
        avail = value.find('section').get('class')
        if avail == "en-rupture":
            return StockEnum.RUPTURE
        elif avail in ["en-stock", "en-stock-limite"]:
            return StockEnum.STOCK
        elif avail.startswith("dispo-"):
            return StockEnum.PRECO
        else:
            return StockEnum.UNKNOWN

    def _set_price(self, value):
        return Decimal(value.find_class("prod_px_euro")[0].get("content"))
