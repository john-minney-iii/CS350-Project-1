# CS350-Project-1/start/views.py

from django.shortcuts import render
from django.views import View
from play.models import BlackCard, WhiteCard
from play.models import WhiteCard

import random


class StartTemplateView(View):
    template_name = 'index.html'

    def get(self, request):
        context = {'black_text': self.getRandomBlackCardText,
                   'white_text': self.getRandomWhiteCardsText}
        return render(request, self.template_name, context)

    """
        Get a Random Black card in the Database
        This might need to change depending on what the backend team does
        @return Black Card
    """

    def getRandomBlackCardText(self) -> str:
        return random.choice(list(BlackCard.objects.all())).CardText

    """
        Get a Set of Random White Cards from the Database
        This might need to change depending on what the backend team does
        @param set_size (int): Number of white cards to return
        @return List of White Cards
    """

    def getRandomWhiteCardsText(self) -> str:
        return random.choice(list(WhiteCard.objects.all())).CardText
