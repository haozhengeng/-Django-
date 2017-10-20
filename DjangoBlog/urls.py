"""DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from DjangoBlog.sitemap import StaticViewSitemap, ArticleSiteMap, CategorySiteMap, TagSiteMap, UserSiteMap
from DjangoBlog.feeds import DjangoBlogFeed
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {

    'blog': ArticleSiteMap,
    'Category': CategorySiteMap,
    'Tag': TagSiteMap,
    'User': UserSiteMap,
    'static': StaticViewSitemap
}

urlpatterns = [
                  url(r'^admin/', admin.site.urls),  # 管理员
                  url(r'', include('blog.urls', namespace='blog', app_name='blog')),   # 博客模块

                  url(r'', include('comments.urls', namespace='comment', app_name='comments')),  # 评论模块
                  url(r'', include('accounts.urls', namespace='account', app_name='accounts')),  # 账号模块
                  url(r'', include('oauth.urls', namespace='oauth', app_name='oauth')),  # 用户注册模块
                  url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                      name='django.contrib.sitemaps.views.sitemap'),    # 站点地图
                  url(r'^feed/$', DjangoBlogFeed()),
                  url(r'^search', include('haystack.urls'), name='search'),
                  url(r'', include('servermanager.urls', namespace='servermanager', app_name='servermanagers'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
