from django import template

from django.apps import apps


register = template.Library()


@register.assignment_tag
def find_by_slug(model, slug):
    model = apps.get_model('mainapp', model)

    try:
        return model.objects.get(slug=slug)
    except model.DoesNotExists:
        return None
