from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from django.shortcuts import render


__all__ = ['render_paginate']


def render_paginate(request, template, objects, per_page, extra_context={}):
    """
    Paginated list of objects.
    """
    paginator = Paginator(objects, per_page)
    page = request.GET.get('page', 1)
    get_params = '&'.join(['%s=%s' % (k, request.GET[k])
                           for k in request.GET if k != 'page'])

    try:
        page_number = int(page)
    except ValueError:
        if page == 'last':
            page_number = paginator.num_pages
        else:
            raise Http404

    try:
        page_obj = paginator.page(page_number)
    except InvalidPage:
        raise Http404

    context = {
        'object_list': page_obj.object_list,
        'paginator': paginator,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'get_params': get_params
    }

    context.update(extra_context)

    return render(request, template, context)
