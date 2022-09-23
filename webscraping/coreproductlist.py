import asyncio

from aiohttp import ClientSession

from coreenum import StockEnum
from coresite import Site
from sitesettings import SITES_URLS


class ProductList:
    def __init__(self):
        self._sites = []
        self._sites_urls = SITES_URLS

    @property
    def sites(self):
        return self._sites

    @property
    def sites_urls(self):
        return self._sites_urls

    @sites_urls.setter
    def sites_urls(self, value):
        self._sites_urls = value

    def get_articles(self, sort_key=None, avail=None):
        articles = []
        for site in self.sites:
            if avail is None:
                articles.extend(site.articles)
            else:
                articles.extend([art for art in site.articles if art.stock == avail])
        if sort_key is None:
            return articles
        else:
            return sorted(articles, key=sort_key)

    def get_all_articles(self, sort_key=None):
        """
        Get all loaded articles
        :param sort_key: like key parameter from sorted function
        :return: list of articles
        """
        return self.get_articles(sort_key=sort_key)

    def get_in_stock(self, sort_key=None):
        return self.get_articles(sort_key=sort_key, avail=StockEnum.STOCK)

    def get_preorder(self, sort_key=None):
        return self.get_articles(sort_key=sort_key, avail=StockEnum.PRECO)

    def get_not_available(self, sort_key=None):
        return self.get_articles(sort_key=sort_key, avail=StockEnum.RUPTURE)

    def load_all_sites(self):
        for (_site_id, _url) in self.sites_urls.items():
            self.load_site(Site(_site_id, _url))

    def load_site(self, site):
        self.sites.append(site)
        site.get_root()
        site.get_articles()

    async def load_all_sites_async(self):
        tasks = []
        async with ClientSession(headers={'User-Agent': 'Mozilla/5.0'}) as session:
            for (_site_id, _url) in SITES_URLS.items():
                tasks.append(self.load_articles_async(Site(_site_id, _url), session))
            await asyncio.gather(*tasks)

    async def load_articles_async(self, site, session):
        self.sites.append(site)
        await site.get_root_async(session)


if __name__ == '__main__':
    pass
