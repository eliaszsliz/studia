from django import template

register = template.Library()


def paginator(context, adjacent_pages=2):
    page_obj = context['page_obj']
    context['page'] = page_obj.number
    context['pages'] = context['paginator'].num_pages

    startPage = max(context['page'] - adjacent_pages, 1)
    if startPage <= 3:
        startPage = 1

    endPage = context['page'] + adjacent_pages + 1

    if endPage >= context['pages'] - 1:
        endPage = context['pages'] + 1
    page_numbers = [n for n in range(startPage, endPage) if 0 < n <= context['pages']]

    return {
        'page_obj': context['page_obj'],
        'paginator': context['paginator'],
        'pages': context['pages'],
        'page_numbers': page_numbers,
        'show_first': 1 not in page_numbers,
        'show_last': context['pages'] not in page_numbers,
    }

register.inclusion_tag('paginator.html', takes_context=True)(paginator)