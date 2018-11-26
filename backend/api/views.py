from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from api.serializers import AuthorSerializer, ColleagueSerializer, EditorSerializer, IssueSerializer, NewsSerializer, \
    CategorySerializer, SimpleCustomFlatPageSerializer, CustomFlatPageSerializer, ArticleSerializer, \
    SimpleIssueSerializer, IssueIndexSerializer
from mainapp.models import Issue, Article, CustomFlatPage, News, Category,\
    Author, Editor, Colleague


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ColleagueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Colleague.objects.all()
    serializer_class = ColleagueSerializer


class EditorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer
    lookup_field = 'slug'


class IssueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class NewsPaginator(PageNumberPagination):
    page_size = 2
    # page_size_query_param = 'page_size'
    # max_page_size = 10000


class NewsViewsSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    pagination_class = NewsPaginator

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')

        if category:
            queryset = queryset.filter(categories__slug=category)

        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FlatPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomFlatPage.objects.all()
    serializer_class = CustomFlatPageSerializer
    lookup_field = 'link'

    def get_queryset(self):
        if not self.kwargs.get('link'):
            return self.queryset.filter(Q(visible_on_footer=True) | Q(visible_on_sidebar=True))
        return self.queryset


@api_view(['GET'])
@permission_classes([AllowAny, ])
def get_site_stuff(request):
    current = Issue.get_current_issue()
    _next = current.next

    data = {
        'issues': {
            'current': SimpleIssueSerializer(current).data,
            'next': SimpleIssueSerializer(_next).data
        }
    }

    queryset = CustomFlatPage.objects.filter(Q(visible_on_footer=True) | Q(visible_on_sidebar=True))
    data['flatpages'] = SimpleCustomFlatPageSerializer(queryset, many=True).data
    return JsonResponse(data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def index(request):
    current = Issue.get_current_issue()
    _next = current.next

    news_list = News.objects.all()[:3]

    data = {
        'issues': {
            'current': IssueIndexSerializer(current).data,
            'next': IssueIndexSerializer(_next).data
        },
        'news': NewsSerializer(news_list, many=True).data
    }

    return JsonResponse(data, safe=False)

