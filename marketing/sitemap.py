from app.models import News, Countries
# from django.contrib.flatpages.models import FlatPage
from django.contrib.sitemaps import Sitemap


class NewsSitemap(Sitemap):
    def items(self):
        return News.objects.all()


class CountrySitemap(Sitemap):
    def items(self):
        return Countries.objects.all()


SITEMAPS = {'categories': NewsSitemap, 'products': CountrySitemap}
