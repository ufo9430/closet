from django import template

register = template.Library()

@register.filter
def ranges(value):
    return range(1,value)