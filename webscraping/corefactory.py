from sitesettings.cybertek import ArticleCybertek
from sitesettings.rueducommerce import ArticleRueDuCommerce
from sitesettings.specenum import SiteEnum
from sitesettings.topachat import ArticleTopAchat


class ArticleFactory:

    @staticmethod
    def create_article(site_id, element):
        if site_id == SiteEnum.topachat:
            return ArticleTopAchat(element, site_id)
        elif site_id == SiteEnum.rueducommerce:
            return ArticleRueDuCommerce(element, site_id)
        elif site_id == SiteEnum.cybertek:
            return ArticleCybertek(element, site_id)
        else:
            raise TypeError(f"article type {site_id} doesn't exists")

    @staticmethod
    def get_article_list(site_id, html_root):
        if site_id == SiteEnum.topachat:
            return ArticleTopAchat.get_article_list(html_root)
        elif site_id == SiteEnum.rueducommerce:
            return ArticleRueDuCommerce.get_article_list(html_root)
        elif site_id == SiteEnum.cybertek:
            return ArticleCybertek.get_article_list(html_root)
        else:
            raise TypeError(f"article type {site_id.value} doesn't exists")

    @staticmethod
    async def get_article_list_async(site_id, html_root):
        if site_id == SiteEnum.topachat:
            return await ArticleTopAchat.get_article_list_async(html_root)
        elif site_id == SiteEnum.rueducommerce:
            return await ArticleRueDuCommerce.get_article_list_async(html_root)
        elif site_id == SiteEnum.cybertek:
            return await ArticleCybertek.get_article_list_async(html_root)
        else:
            raise TypeError(f"article type {site_id.value} doesn't exists")



