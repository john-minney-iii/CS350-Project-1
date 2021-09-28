
from django import template
register = template.Library()

"""
    This will return the item at index i-1.
    This is used in the play.html template to get the card that is currently being ranked
"""
@register.filter
def index(indexable, i):
    return indexable[i-1]