from django import template

register = template.Library()

"""

"""

@register.filter(name='tmmap')
def tmmap():
    returnA = []

