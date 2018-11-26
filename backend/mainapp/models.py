from abc import abstractmethod
import os
from django.core.validators import RegexValidator
from django.db import models
from autoslug import AutoSlugField
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse
from tinymce.models import HTMLField


class Person(models.Model):
    avatar = None
    name_prefix = models.CharField(max_length=20, verbose_name='Tytuł', null=True, blank=True)
    full_name = models.CharField(max_length=80, verbose_name='Imię i nazwisko')
    slug = AutoSlugField(populate_from='full_name', unique=True, always_update=True)
    order = models.DecimalField(max_digits=3, decimal_places=0,
                                verbose_name='W kolejności', default=999)
    description = HTMLField(verbose_name='Opis', blank=True, null=True)
    short_description = models.TextField(verbose_name='Krótki opis', blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s %s' % (self.name_prefix or '', self.full_name)

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return static('images/no-avatar.png')


class Author(Person):
    avatar = models.ImageField(upload_to='avatars/author/',
                               verbose_name='Zdjęcie',
                               blank=True, null=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autorzy'

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'slug': self.slug})

    @property
    def articles(self):
        return self.article_set.filter(published=True)

    def list_url(self):
        return reverse('author-list')


class Editor(Person):
    function = models.CharField(max_length=40, verbose_name='Stanowisko',
                                blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/editor/',
                               verbose_name='Zdjęcie',
                               blank=True, null=True)

    class Meta:
        verbose_name = 'Redaktor'
        verbose_name_plural = 'Redaktorzy'

    def list_url(self):
        return reverse('editor-list')

    def get_absolute_url(self):
        return reverse('editor-detail', kwargs={'slug': self.slug})


class Colleague(Person):
    function = models.CharField(max_length=40, verbose_name='Stanowisko',
                                blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/colleague/',
                               verbose_name='Zdjęcie',
                               blank=True, null=True)

    class Meta:
        verbose_name = 'Współpracownik'
        verbose_name_plural = 'Współpracownicy'

    def list_url(self):
        return reverse('colleague-list')

    def get_absolute_url(self):
        return reverse('colleague-detail', kwargs={'slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nazwa')
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

    def article_and_news_list(self):
        n = list(self.news_set.all()) + list(self.article_set.all())
        return n


class Issue(models.Model):
    title = models.CharField(max_length=100, verbose_name='Tytuł', blank=True, null=True)
    date = models.IntegerField(verbose_name='Rocznik', validators=[RegexValidator(regex='^20\d{2}$')], unique=True)
    description = HTMLField(verbose_name='Opis', blank=True, null=True)
    cover = models.ImageField(upload_to='issues/', verbose_name='Okładka', blank=True, null=True)
    current = models.BooleanField(default=False, verbose_name='To jest aktualny numer')
    short_description = models.TextField(verbose_name='Krótki opis',
                                                    blank=True, null=True,
                                                    help_text='Wyświetlany jeśli nie ma żadnych artykułów.')

    alternative_link = models.CharField(max_length=200, verbose_name='Alternatywny link', blank=True, null=True)

    class Meta:
        verbose_name = 'Numer'
        verbose_name_plural = 'Numery'
        ordering = ('-date',)

    def __str__(self):
        return '%s' % self.date

    def get_absolute_url(self):
        if self.alternative_link:
            return '%s' % self.alternative_link
        else:
            return reverse('issue-detail', kwargs={'date': self.date})

    @property
    def cover_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url
        else:
            return static('images/no-img.png')

    @property
    def articles(self):
        return self.article_set.filter(published=True)

    @classmethod
    def get_current_issue(cls):
        try:
            return cls.objects.get(current=True)
        except cls.DoesNotExist:
            return None
        except cls.MultipleObjectsReturned:
            result = cls.objects.filter(current=True)[0]
            cls.objects.exclude(pk=result.pk).update(current=False)
            return result

    @property
    def slug(self):
        return self.date

    @property
    def next(self):
        try:
            return Issue.objects.filter(date__gt=self.date).order_by('date')[0]
        except (IndexError, AttributeError):
            return None

    @property
    def prev(self):
        try:
            return Issue.objects.filter(date__lt=self.date).order_by('-date')[0]
        except (IndexError, AttributeError):
            return None

    def save(self, *args, **kw):
        # only one number may be current
        old = Issue.objects.get(pk=self.pk) if self.pk else None
        super(Issue, self).save(*args, **kw)
        if old and self.current:
            Issue.objects.exclude(pk=self.pk).update(current=False)


class Article(models.Model):
    belong_to = models.ForeignKey(Issue, verbose_name='Numer', blank=True, null=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=120, verbose_name='Tytuł')
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)

    description = models.TextField(verbose_name='Opis', null=True, blank=True)
    body = HTMLField(verbose_name='Tekst')

    authors = models.ManyToManyField(Author, verbose_name='Autorzy', blank=True)
    categories = models.ManyToManyField(Category, verbose_name='Kategorie', blank=True)

    created_at = models.DateField(auto_now_add=True, verbose_name='Stworzony dnia')
    published = models.BooleanField(default=False, verbose_name='Opublikowany')

    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'

    def __str__(self):
        if self.published:
            return '%s' % self.title
        else:
            return '[!NIEOPUBLIKOWANY!]%s' % self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})

    @property
    def date(self):
        return self.belong_to.date


class News(models.Model):
    title = models.CharField(max_length=120, verbose_name='Tytuł')
    slug = AutoSlugField(populate_from='title', unique=True)
    body = HTMLField(verbose_name='Tekst')
    categories = models.ManyToManyField(Category, verbose_name='Kategorie', blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Stworzony dnia')

    class Meta:
        ordering = ('pk',)
        verbose_name = 'News'
        verbose_name_plural = 'Newsy'

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.slug})

    @property
    def created_at_formated(self):
        try:
            return '%s %s %s' % (self.created_at.day,
                                 ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia',
                                  'września', 'października', 'listopada', 'grudnia'][self.created_at.month-1],
                                 self.created_at.year)
        except AttributeError:
            return None

    @property
    def date(self):
        return self.created_at_formated


class CustomFlatPage(models.Model):
    link = AutoSlugField(populate_from='name', unique=True,
                         always_update=True, verbose_name='Link')
    name = models.CharField(max_length=30, verbose_name='Nazwa linku',
                            help_text='Używana w menu po lewej stronie np. Kontakt')

    title = models.CharField(max_length=70, verbose_name='Tytuł',
                             help_text='Używany na górze strony')
    body = HTMLField(verbose_name='Tekst')

    order = models.DecimalField(max_digits=2, decimal_places=0, blank=True,
                                null=True, default=99, verbose_name='Kolejność w menu')

    visible_on_sidebar = models.BooleanField(default=True, verbose_name='Pokazuj w menu')
    visible_on_footer = models.BooleanField(default=True, verbose_name='Pokazuj w stópce')

    class Meta:
        ordering = ('order', )
        verbose_name = 'Dodatkowa strona'
        verbose_name_plural = 'Dodatkowe strony'

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('flat-page', kwargs={'link': self.link})




