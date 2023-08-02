from django import template

register = template.Library()

@register.filter
def comma(value):
    ret = format(int(value),",d")
    return ret