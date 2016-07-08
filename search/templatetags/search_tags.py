from django import template
from search.forms import SearchForm
import urllib

register = template.Library()


@register.inclusion_tag("tags/search_box.html")
def search_box(request):
    q = request.GET.get('q', '')
    form = SearchForm({'q': q})
    return {'form': form}


@register.inclusion_tag('tags/pagination_links.html')
def pagination_links(request, paginator):
    raw_params = request.GET.copy()
    page = raw_params.get('page', 1)
    p = paginator.page(page)
    try:
        del raw_params['page']
    except KeyError:
        pass
    # Here solved some problem with urllib.urlencode not working with unicode
    raw_params_str = {}
    for k, v in raw_params.iteritems():
        raw_params_str[k] = unicode(v).encode('utf-8')
    params = urllib.urlencode(raw_params_str)
    return {'request': request, 'paginator': paginator, 'p': p, 'params': params}
