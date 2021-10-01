# CS350-Project-1/play/forms.py

from django import forms

class CardRateForm(forms.Form):
    # Generate pairs such as ('1', 1)
    CHOICES = [(str(x), x) for x in range(1, 11)]
    card_rating = forms.CharField(
        label='Rate the White Card from 1-10',
        widget=forms.Select(choices=CHOICES)
    )