from rest_framework import serializers
from mainapp.models import Issue, Article, CustomFlatPage, News, Category, Author, Editor, Colleague


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'id')


class SimpleArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'slug', 'title')


class IssueSerializer(serializers.ModelSerializer):
    articles = SimpleArticleSerializer(many=True)

    class Meta:
        model = Issue
        fields = ('id', 'title', 'date', 'description', 'cover_url', 'current', 'short_description',
                  'alternative_link', 'articles')


class IssueIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'title', 'date', 'description', 'cover_url', 'current', 'short_description',
                  'alternative_link')


class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'slug', 'full_name')


class SimpleIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'date', 'current', 'alternative_link')


class ArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    authors = SimpleAuthorSerializer(many=True)
    belong_to = SimpleIssueSerializer()

    class Meta:
        model = Article
        fields = ('belong_to', 'title', 'slug', 'id', 'description', 'body', 'authors',
                  'categories', 'created_at')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class AuthorSerializer(serializers.ModelSerializer):
    articles = SimpleArticleSerializer(many=True)

    class Meta:
        model = Author
        fields = ('avatar_url', 'name_prefix', 'full_name', 'slug', 'id', 'order',
                  'description', 'short_description', 'articles')


class ColleagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colleague
        fields = ('function', 'avatar_url', 'name_prefix', 'full_name', 'slug', 'id', 'order',
                  'description', 'short_description')


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = ('function', 'avatar_url', 'name_prefix', 'full_name', 'slug', 'id', 'order',
                  'description', 'short_description')


class NewsSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = News
        fields = ('title', 'slug', 'id', 'body', 'categories', 'created_at')


class CustomFlatPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFlatPage
        fields = ('link', 'id', 'name', 'title', 'body', 'order', 'visible_on_sidebar',
                  'visible_on_footer')
        lookup_field = 'link'
        extra_kwargs = {
            'url': {
                'lookup_field': 'link'
            }
        }

class SimpleCustomFlatPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFlatPage
        fields = ('id', 'name', 'link', 'visible_on_sidebar', 'visible_on_footer')

