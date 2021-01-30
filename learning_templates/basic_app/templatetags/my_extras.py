from django import template

register = template.Library()
@register.filter(name='cut')

def Cut(value,arg):
    """
    this cut out all value of arg from string
    """
    return value.replace(arg,"")
#this is another way of register filter
#register.filter('cut':Cut)
