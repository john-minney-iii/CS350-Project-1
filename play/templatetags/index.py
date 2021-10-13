
from django import template
from play.models import WhiteCard, BlackCard, Score

register = template.Library()

"""
    This will return the item at index i-1.
    This is used in the play.html template to get the card that is currently being ranked
"""
@register.filter
def index(indexable, i):
    return indexable[i-1]

@register.filter
def getPK(indexable, i):
    return indexable[i-1].pk

@register.simple_tag
def get_card_text_by_index(index, cards) -> str:
    return cards[index].CardText

@register.simple_tag
def index_card_match_boder (index, card, cards) -> str:
    if index == cards.index(card):
        return 'cah-current-border'
    return 'cah-other-border'

"""
    Get the Average Rating for a Black Card and White Card
"""
@register.simple_tag
def get_score_average(obj, black_card):
    print('White Card:', obj)
    print('Black Card:', black_card)
    return round(obj.findScoreAverage(black_card), 2)
