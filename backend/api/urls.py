from django.conf.urls import url, include
from rest_framework import routers
from api.views import AuthorViewSet, get_site_stuff, CategoryViewSet, NewsViewsSet, IssueViewSet, EditorViewSet, \
    ColleagueViewSet, FlatPageViewSet, ArticleViewSet, index

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'authors', AuthorViewSet)
router.register(r'colleagues', ColleagueViewSet)
router.register(r'editors', EditorViewSet)

router.register(r'articles', ArticleViewSet)

router.register(r'issues', IssueViewSet)
router.register(r'news', NewsViewsSet)
router.register(r'categories', CategoryViewSet)
router.register(r'flatpages', FlatPageViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^index', index),
    url(r'^site', get_site_stuff),
]

