import pytest
from coreproductlist import ProductList


@pytest.fixture
def prod_list_init():
    prod_lst = ProductList()
    return prod_lst


@pytest.fixture
def sites_url_empty(prod_list_init):
    prod_list_init.sites_urls = dict()
    return prod_list_init


@pytest.fixture
def sites_url_bad_key(prod_list_init):
    from enum import Enum

    class SiteFake(Enum):
        badkey = "badkey"

    prod_list_init.sites_urls = {SiteFake.badkey: 'https://www.example.com/randomarticle'}
    return prod_list_init


@pytest.fixture
def sites_url_bad_url(prod_list_init):
    from sitesettings.specenum import SiteEnum
    prod_list_init.sites_urls = {SiteEnum.cybertek: 'https://sdfsqfqfsfsqfsqfdfqfqf.dsfsfs/randomarticlelist'}
    return prod_list_init


def test_load_all_sites_empty(sites_url_empty):
    sites_url_empty.load_all_sites()
    assert len(sites_url_empty.sites) == 0


def test_load_all_sites_bad_key(sites_url_bad_key):
    with pytest.raises(KeyError):
        sites_url_bad_key.load_all_sites()


def test_load_all_sites_bad_url(sites_url_bad_url):
    from urllib.error import URLError
    with pytest.raises(URLError):
        sites_url_bad_url.load_all_sites()


# def test_sites():
#     assert False
#
#
# def test_get_articles():
#     assert False
#
#
# def test_get_all_articles():
#     assert False
#
#
# def test_get_in_stock():
#     assert False
#
#
# def test_get_preorder():
#     assert False
#
#
# def test_get_not_available():
#     assert False
#
#
# def test_load_site():
#     assert False
#
#
# def test_load_all_sites_async():
#     assert False
#
#
# def test_load_articles_async():
#     assert False
