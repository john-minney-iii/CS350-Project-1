# CS350-Project-1/play/forms.py

from django import forms

class CardRateForm(forms.Form):
    # Generate pairs such as ('1', 1)
    CHOICES = [(str(x), x) for x in range(0, 11)]
    card_rating = forms.CharField(
        label='',
        widget=forms.Select(choices=CHOICES)
    )
    