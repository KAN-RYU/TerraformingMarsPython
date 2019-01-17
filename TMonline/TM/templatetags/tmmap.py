from django import template

register = template.Library()

"""
0 0 1 1 1 1 1
0 0 1 1 1 1 1 1
0 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
"""

@register.simple_tag(name='tmmap')
def tmmap():
    returnA = [[0,0,1,1,1,1,1],
               [0,0,1,1,1,1,1,1],
               [0,1,1,1,1,1,1,1],
               [0,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1],
               [0,1,1,1,1,1,1,1,1],
               [0,1,1,1,1,1,1,1],
               [0,0,1,1,1,1,1,1],
               [0,0,1,1,1,1,1]]
    return returnA


