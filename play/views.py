# CS350-Project-1/play/views.py

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import CardRateForm

class PlayView(View):
    template_name = 'play.html'
    
    def get(self, request, round):
        # current_card_index is the card that will be highlighed
        context = {'round': round, 'current_card_index': round % 8, 'form': CardRateForm()}
        return render(request, self.template_name, context)

    def post(self, request, round):
        form = CardRateForm(request.POST)
        if form.is_valid():
            card_rating = form.cleaned_data['card_rating']
            print('Card Rating:', card_rating)
            # Redirect back to Play
            return HttpResponseRedirect(f'/play/{round+1}/')
