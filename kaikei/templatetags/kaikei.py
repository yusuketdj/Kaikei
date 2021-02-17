from django import template
from kaikei.forms import CustomerSearchForm

register = template.Library()

@register.inclusion_tag('kaikei/search_form.html')
def create_search_form(request):
    form = CustomerSearchForm(request.GET or None)
    return {'form': form}

