# CS350-Project-1/end/views.py

from typing import _SpecialForm
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.db.models import Max

from play.models import BlackCard, WhiteCard, Score
from play.models import WhiteCard

class EndTemplateView(View):
    template_name = 'end.html'

    def get(self, request):

        dataBlkCards = BlackCard.objects.all()
        dataWhiteCards = WhiteCard.objects.all()

        highest_scores = []

        for card in dataBlkCards:
            score = Score.objects.filter(BlackCard=card).order_by('rating')[0]
            highest_scores.append((card, score.WhiteCard))

        context = {'black_cards': dataBlkCards,
                   'white_cards': dataWhiteCards,
                   'highest_scores': highest_scores
                   }
        return render(request, self.template_name, context)
