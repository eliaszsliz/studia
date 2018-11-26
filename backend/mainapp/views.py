from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import NoReverseMatch
from django.views.generic import DetailView
from mainapp.models import Issue, Category, News


class IssueDetailView(DetailView):
    model = Issue

    def get_object(self, **kwargs):
        try:
            return get_object_or_404(self.model, date=self.kwargs.get('date'))
        except NoReverseMatch:
            raise Http404


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        context['object_list'] = []
        if not self.request.GET.get('filter') == 'not_article':
            context['object_list'] += list(self.object.article_set.all())
        if not self.request.GET.get('filter') == 'not_news':
            context['object_list'] += list(self.object.news_set.all())
        context['object_list'].sort(key=lambda x: x.pk)
        return context


def index(request):
    current = Issue.get_current_issue()
    _next = current.next if current else None


    context = {
        'current': current,
        'next': _next,
        'news_list': News.objects.all()[:3]
    }

    return render(request, template_name='index.html', context=context)
