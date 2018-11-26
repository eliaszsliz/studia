"""studia_pigoniana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.views.generic import ListView, DetailView, TemplateView
import api.urls
from mainapp.models import Issue, Article, Author, Editor, Colleague, News, CustomFlatPage
from mainapp.views import IssueDetailView, CategoryDetailView
from django.conf import settings
from django.conf.urls.static import static
from mainapp.admin import admin_help
from mainapp.views import index

urlpatterns = [
    url(r'^admin/help$', admin_help, name='admin-help'),

    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api.urls, namespace="api")),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^artykul/(?P<slug>[-\w]+)$', DetailView.as_view(model=Article), name='article-detail'),
    url(r'^kategorie/(?P<slug>[-\w]+)$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^dodatkowe/(?P<link>[-\w]+)$',
        DetailView.as_view(model=CustomFlatPage,
                           slug_url_kwarg='link',
                           slug_field='link',
                           template_name='mainapp/flat_page.html'),
        name='flat-page'),

    url(r'^archiwum/$', ListView.as_view(queryset=Issue.objects.all(), ordering='-date'), name='issue-list'),
    url(r'^numer/(?P<date>\d+)$', IssueDetailView.as_view(), name='issue-detail'),

    url(r'^autor/(?P<slug>[-\w]+)$',
        DetailView.as_view(model=Author, template_name='mainapp/person_detail.html'), name='author-detail'),
    url(r'^autorzy/$',
        ListView.as_view(model=Author, template_name='mainapp/person_list.html'), name='author-list'),

    url(r'^redaktor/(?P<slug>[-\w]+)$',
        DetailView.as_view(model=Editor, template_name='mainapp/person_detail.html'), name='editor-detail'),
    url(r'^redaktorzy/$',
        ListView.as_view(model=Editor, template_name='mainapp/person_list.html'), name='editor-list'),

    url(r'^wspolpracownik/(?P<slug>[-\w]+)$',
        DetailView.as_view(model=Colleague, template_name='mainapp/person_detail.html'), name='colleague-detail'),
    url(r'^wspolpracownicy/$',
        ListView.as_view(model=Colleague, template_name='mainapp/person_list.html'), name='colleague-list'),

    url(r'^newsy/$',
        ListView.as_view(queryset=News.objects.all(), ordering='-created_at', paginate_by=12), name='news-list'),

    url(r'^news/(?P<slug>[-\w]+)$', DetailView.as_view(model=News), name='news-detail'),

    url(r'^$', index, name='index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [url(r'^404', TemplateView.as_view(template_name='404.html'))]
    urlpatterns += [url(r'^500', TemplateView.as_view(template_name='500.html'))]
    urlpatterns += [url(r'^403', TemplateView.as_view(template_name='403.html'))]