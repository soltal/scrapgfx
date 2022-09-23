from sitesettings import SITES_URLS
from abc import ABC, abstractmethod
from decimal import Decimal
from urllib.parse import urljoin


class BaseArticle(ABC):

    def __init__(self, element, site_id):
        self.element = element
        self._title = ""
        self._stock = None
        self._price = Decimal(0.0)
        self._site_id = site_id
        self._link = ""
        self.fill_data()

    def __str__(self):
        return f"{self.site_id.value} | {self.stock.value} | {self.price} | {self.title} | {self.link}"

    @property
    def site_id(self):
        return self._site_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = self._set_title(value)

    @abstractmethod
    def _set_title(self, value):
        raise NotImplementedError

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = self._set_stock(value)

    @abstractmethod
    def _set_stock(self, value):
        raise NotImplementedError

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = self._set_price(value)

    @abstractmethod
    def _set_price(self, value):
        raise NotImplementedError

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        relative = self._set_link(value)
        try:
            self._link = urljoin(SITES_URLS[self.site_id], relative)
        except KeyError:
            raise KeyError("Can't join base url with relative link article.")

    @staticmethod
    @abstractmethod
    def get_article_list(html_root):
        raise NotImplementedError

    def fill_data(self):
        self.title = self.element
        self.stock = self.element
        self.price = self.element
        self.link = self.element
