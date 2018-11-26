from django import template
from django.db.models import QuerySet

register = template.Library()


@register.filter
def class_name(value):
    if isinstance(value, QuerySet):
        return value.model.__name__
    else:
        return value.__class__.__name__


@register.filter
def plural_name(value):
    if isinstance(value, QuerySet):
        return value.model._meta.verbose_name_plural.title()
    else:
        return value.__class__._meta.verbose_name_plural.title()
