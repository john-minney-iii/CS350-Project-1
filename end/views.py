# CS350-Project-1/end/views.py

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from play.models import BlackCard, WhiteCard, Score
from play.models import WhiteCard

class EndTemplateView(View):
    template_name = 'end.html'

    def get(self, request):

        dataBlkCards = BlackCard.objects.all()
        dataWhiteCards = WhiteCard.objects.all()
        context = {'black_cards': dataBlkCards,
                   'white_cards': dataWhiteCards}
        return render(request, self.template_name, context)
