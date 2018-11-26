from django import template
from django.urls import reverse, resolve
from urllib.parse import urlparse  # for python 3

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_previous_url(context):
    try:
        request = context['request']
        assert request.META.get('HTTP_REFERER', False)
        previous_url = urlparse(request.META.get('HTTP_REFERER')).path
        previous_url_resolve = resolve(previous_url)
        return previous_url_resolve
    except (KeyError, AssertionError):
        return None


@register.simple_tag(takes_context=True)
def assert_previous_url(context, url_to_compare):
    try:
        request = context['request']
        previous_url_name = resolve(request.META.get('HTTP_REFERER'))
        assert previous_url_name == url_to_compare
        return True
    except (AssertionError, KeyError):
        return False
