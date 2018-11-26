from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from mainapp.filters import null_filter
from mainapp.forms import IssueForm
from mainapp.models import Issue, Article, Author, Person, Editor, Colleague, Category, News, CustomFlatPage
from django.contrib import messages

admin.site.site_header = 'Panel administracyjny'
admin.site.index_title = ''


@user_passes_test(lambda u: u.is_superuser)
def admin_help(request):
    return render(request, template_name='admin/help.html')


class PersonAdmin(admin.ModelAdmin):
    model = Person
    fields = ('name_prefix', 'full_name', 'avatar', 'order', 'description', 'short_description')
    list_display = ('full_name', 'order', 'has_avatar', 'has_description', 'has_short_description')
    ordering = ['order']

    def has_avatar(self, obj):
        return True if obj.avatar else False
    has_avatar.boolean = True
    has_avatar.short_description = 'Posiada zdjęcie'

    def has_description(self, obj):
        return True if obj.description else False
    has_description.boolean = True
    has_description.short_description = 'Posiada opis'

    def has_short_description(self, obj):
        return True if obj.short_description else False
    has_short_description.boolean = True
    has_short_description.short_description = 'Posiada krótki opis'


@admin.register(Author)
class AuthorAdmin(PersonAdmin):
    model = Author


@admin.register(Editor)
class EditorAdmin(PersonAdmin):
    model = Editor
    fields = ('function', 'name_prefix', 'full_name', 'avatar', 'order', 'description', 'short_description')


@admin.register(Colleague)
class ColleagueAdmin(PersonAdmin):
    model = Colleague
    fields = ('function', 'name_prefix', 'full_name', 'avatar', 'order', 'description', 'short_description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    form = IssueForm
    list_display = ('date', 'has_cover', 'has_alternative_link', 'current',
                    'has_short_description')
    list_filter = (null_filter('cover', 'okładkę'),
                   null_filter('alternative_link', 'alternatywny link'),
                   null_filter('short_description', 'krótki opis'))
    fieldsets = (
      (None, {
          'fields': ('date', 'title', 'cover', 'description', 'articles')
      }),
      ('Aktualny numer', {
          'fields': ('current', 'short_description', 'alternative_link')
      })
    )
    search_fields = ['date', 'title', 'description', 'articles__title']
    actions = ['make_current', 'remove_alternative_link', 'remove_short_description']

    def has_cover(self, obj):
        return True if obj.cover else False
    has_cover.boolean = True
    has_cover.short_description = 'Posiada okładkę'

    def has_alternative_link(self, obj):
        return True if obj.alternative_link else False
    has_alternative_link.boolean = True
    has_alternative_link.short_description = 'Posiada alternatywny link'

    def has_short_description(self, obj):
        return True if obj.short_description else False
    has_short_description.boolean = True
    has_short_description.short_description = 'Posiada krótki opis'

    def make_current(self, request, queryset):
        if queryset.count() == 1:
            obj = queryset[0]
            obj.current = True
            obj.save()
        else:
            messages.error(request, 'Musi być zaznaczony tylko jeden numer.')
    make_current.short_description = "Ustaw jako aktualny"

    def remove_alternative_link(self, request, queryset):
        queryset.update(alternative_link=None)
    remove_alternative_link.short_description = "Usuń alternatywne link"

    def remove_short_description(self, request, queryset):
        queryset.update(short_description=None)
    remove_short_description.short_description = "Usuń krótkie opisy"



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    fields = ('belong_to', 'title', 'body', 'description', 'authors', 'categories', 'published')
    filter_horizontal = ('authors', 'categories')
    list_display = ('title', 'belong_to', 'published')
    search_fields = ['title', 'description', 'authors__full_name']
    ordering = ('-belong_to__date',)
    list_filter = ('belong_to__date', 'published')
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(published=True)
    make_published.short_description = "Oznacz jako opublikowane"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    model = News
    fields = ('title', 'body', 'categories')
    filter_horizontal = ('categories',)
    list_display = ('title', 'created_at')
    ordering = ('created_at',)


@admin.register(CustomFlatPage)
class CustomFlatPageAdmin(admin.ModelAdmin):
    model = CustomFlatPage
    fieldsets = (
      (None, {
          'fields': ('name', 'title', 'body')
      }),
      ('Wyświetlanie', {
          'fields': ('order', 'visible_on_sidebar', 'visible_on_footer')
      })
    )
    list_display = ('title', 'order', 'list_display_link', 'visible_on_sidebar', 'visible_on_footer')

    def list_display_link(self, obj):
        return '/dodatkowe/%s' % obj.link