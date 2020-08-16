from django.template import Library
register = Library()
@register.filter
def running_total(role_total):
     return sum( [d.get('total') for d in role_total] )