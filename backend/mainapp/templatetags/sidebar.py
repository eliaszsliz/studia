from django import template
from mainapp.models import CustomFlatPage, Issue

register = template.Library()


@register.assignment_tag(name='get_current_issue')
def get_current_issue():
    return Issue.get_current_issue()


@register.assignment_tag(name='get_flat_pages_sidebar')
def get_flat_pages_sidebar():
    return CustomFlatPage.objects.filter(visible_on_sidebar=True)


@register.assignment_tag(name='get_flat_pages_footer')
def get_flat_pages_footer():
    return CustomFlatPage.objects.filter(visible_on_footer=True)
