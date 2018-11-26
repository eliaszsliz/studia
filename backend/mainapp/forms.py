from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models import Q
from mainapp.models import Issue, Article


class IssueForm(forms.ModelForm):
    articles = forms.ModelMultipleChoiceField(
        queryset=Article.objects.all(),
        widget=FilteredSelectMultiple(verbose_name="Artykuły", is_stacked=False),
        required=False,
        label='Artykuły',
    )

    class Meta:
        model = Issue
        fields = ('title', 'date', 'cover', 'description', 'articles', 'current',
                  'short_description', 'alternative_link')
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 40em'}),
            'title': forms.TextInput(attrs={'style': 'width: 40em'})
        }

    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['articles'].queryset = Article.objects.filter(
            Q(belong_to__isnull=True) | Q(belong_to=kwargs.get('instance')))
        if kwargs.get('instance'):
            self.fields['articles'].initial = Article.objects.filter(belong_to=kwargs['instance'])

    def save(self, commit=True):
        instance = super(IssueForm, self).save(commit=True)
        instance.article_set.all().update(belong_to=None)
        self.cleaned_data.get('articles').update(belong_to=instance)
        return super(IssueForm, self).save(commit=commit)

