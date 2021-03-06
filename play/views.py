# CS350-Project-1/play/views.py

import random
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect, render
from .forms import CardRateForm
from play.models import BlackCard, WhiteCard, Score

class PlayView(View):
    template_name = 'play.html'

    def get(self, request, num_cards: int, round: int, index: int, shuffle: str, bpk: int, wpks: str):
        context = {'num_cards': num_cards, 'round': round, 'index': index, 'form': CardRateForm()}

        if shuffle == 'True':
            context['black_card'] = self.getRandomBlackCard()
            context['white_cards'] = self.getRandomWhiteCards(num_cards, None)
        else:
            context['black_card'] = BlackCard.objects.get(pk=bpk)
            context['white_cards'] = self.getRandomWhiteCards(num_cards, wpks.split('_'))

        return render(request, self.template_name, context)

    def post(self, request, num_cards: int, round: int, index: int, shuffle: str, bpk: int, wpks: str):
        form = CardRateForm(request.POST)
        if form.is_valid():
            card_rating = form.cleaned_data['card_rating']
            played_white_card = WhiteCard.objects.get(
                pk=form.cleaned_data['white_card_pk']
            )
            played_black_card = BlackCard.objects.get(pk=bpk)

            # New Code 10/16/21 ----------------------------------------------------------------------------
            # Check if there is a score in the database that matches the black and white card
            if len(Score.objects.filter(BlackCard=played_black_card, WhiteCard=played_white_card)) != 0:
                # Same Code before change
                new_score = Score.objects.filter(
                    WhiteCard=played_white_card,
                    BlackCard=played_black_card
                )[0]
                new_score.add_score(int(card_rating))
                new_score.save()
            else:
                # This will create a new Score Entity in the Database
                new_score = Score(
                    BlackCard=played_black_card,
                    WhiteCard=played_white_card,
                    rating=card_rating,
                    timesAppeared=1
                )
                new_score.save()
                print('New Score', new_score.pk)
            # ----------------------------------------------------------------------------------------------
            if index == num_cards - 1: 
                index = 0
                return HttpResponseRedirect(f'/play/score/{num_cards}/{round}/{index}/{shuffle}/{bpk}/{wpks}/')
            else:
                index += 1
            return HttpResponseRedirect(f'/play/{num_cards}/{round}/{index}/{shuffle}/{bpk}/{wpks}/')
        else:
            return HttpResponse('Form Faild POST')

    def getRandomBlackCard(self) -> BlackCard:
        return random.choice(list(BlackCard.objects.all()))

    def getRandomWhiteCards(self, set_size: int, wpks: list[str]) -> list[WhiteCard]:
        cards = []
        if wpks is not None:
            for primary_key in wpks:
                cards.append(WhiteCard.objects.get(pk=primary_key))
        else:
            cards = random.sample(list(WhiteCard.objects.all()), set_size)
        return cards

class PlayAverageView(View):
    template_name = 'play-scores.html'

    def get(self, request, num_cards: int, round: int, index: int, shuffle: str, bpk: int, wpks: str):
        context = {
            'link': f'/play/{num_cards}/{round+1}/{index}/True/{bpk}/{wpks}/',
            'black_card': BlackCard.objects.get(pk=bpk)
        }
        context['white_cards'] = []
        for primary_key in wpks.split('_'):
            context['white_cards'].append(WhiteCard.objects.get(pk=primary_key))
        return render(request, self.template_name, context)
