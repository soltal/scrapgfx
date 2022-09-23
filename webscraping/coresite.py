from urllib.error import URLError
from urllib.request import Request, urlopen

from aiohttp import ClientSession
from lxml import html

from corefactory import ArticleFactory
from sitesettings.specenum import SiteEnum


class Site:

    def __init__(self, site_id, url):
        self.site_id = site_id
        self._url = url
        self._html_root = ""
        self._articles = []

    @property
    def url(self):
        return self._url

    @property
    def site_id(self):
        return self._site_id

    @site_id.setter
    def site_id(self, value: SiteEnum):
        if value.value in {site_id.value for site_id in SiteEnum}:
            self._site_id = value
        else:
            raise KeyError(f"Site key '{value} ' isn't set.")


    @property
    def html_root(self):
        return self._html_root

    @property
    def articles(self):
        return self._articles

    # @articles.setter
    # def articles(self, value):
    #     self._articles = value

    @html_root.setter
    def html_root(self, value):
        self._html_root = value

    def get_root(self):
        req = Request(
            url=self.url,
            headers={'User-Agent': 'Mozilla/5.0'},
        )
        try:
            content = urlopen(req).read()
        except URLError as ex:
            raise URLError(f'bad url {self.url} :\n{ex.reason}')
        self.html_root = html.fromstring(content)

    def get_articles(self):
        elements = ArticleFactory.get_article_list(self.site_id, self.html_root)
        for element in elements:
            self.articles.append(ArticleFactory.create_article(self.site_id, element))

    async def get_root_async(self, session: ClientSession):
        resp = await session.request(method="GET", url=self.url)
        resp.raise_for_status()
        html_content = await resp.text()
        self.html_root = html.fromstring(html_content)
        await self.get_articles_async()

    async def get_articles_async(self):
        elements = await ArticleFactory.get_article_list_async(self.site_id, self.html_root)
        for element in elements:
            self.articles.append(ArticleFactory.create_article(self.site_id, element))




