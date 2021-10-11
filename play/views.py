# CS350-Project-1/play/views.py

from play.models import BlackCard, WhiteCard, Score
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import CardRateForm

import random

# IMPORTANT!!!
# Any DB calls will need to change depending on what the backend does. These are just placeholders for now

class PlayView(View):
    template_name = 'play.html'
    """
        View to allow user to train the database
        @param round (int): the round the player is on
        @param shuffle (str): does the player need new cards
        @param bpk (int): primary key of the black card 
        @param pwks (str): string of all white card primary keys
    """
    def get(self, request, round: int, shuffle: str, bpk: int, wpks: str):
        # current_card_index is the card that will be highlighed
        context = {'round': round, 'current_card_index': round % 8, 'form': CardRateForm()}
        num_white_cards = 8 # Number of white cards that will be ranked

        # if this is the first round or we need to shuffle. Get the random cards
        # otherwise use the pk passed in the url to get the cards
        if (round == 1 or shuffle == "True"):
            context['black_card'] = self.getRandomBlackCard()
            context['white_cards'] = self.getRandomWhiteCards(num_white_cards)
        else:
            context['black_card'] = BlackCard.objects.get(pk=bpk)
            context['white_cards'] = []
            for primary_key in wpks.split('_'):
                context['white_cards'].append(WhiteCard.objects.get(pk=primary_key))

        return render(request, self.template_name, context)

    def post(self, request, round: int, shuffle: str, bpk: int, wpks: str):
        form = CardRateForm(request.POST)
        if form.is_valid():
            card_rating = form.cleaned_data['card_rating']
            # Score the Cards
            played_white_card = WhiteCard.objects.get(pk=form.cleaned_data['white_card_pk'])
            played_black_card = BlackCard.objects.get(pk=bpk)
            score = Score.objects.filter(
                WhiteCard=played_white_card,
                BlackCard=played_black_card
            )[0]
            score.add_score(int(card_rating))
            score.save()
            # Redirect back to Play
            return HttpResponseRedirect(f'/play/{round+1}/{shuffle}/{bpk}/{wpks}')

    """
        Get a Random Black card in the Database
        This might need to change depending on what the backend team does
        @return Black Card
    """
    def getRandomBlackCard(self) -> BlackCard:
        return random.choice(list(BlackCard.objects.all()))

    """
        Get a Set of Random White Cards from the Database
        This might need to change depending on what the backend team does
        @param set_size (int): Number of white cards to return
        @return List of White Cards
    """
    def getRandomWhiteCards(self, set_size: int) -> list[WhiteCard]:
        return random.sample(list(WhiteCard.objects.all()), set_size)
