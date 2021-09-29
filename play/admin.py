from django.contrib import admin
from .models import BlackCard, WhiteCard, Score

# Register your models here.

admin.site.register(BlackCard)
admin.site.register(WhiteCard)
admin.site.register(Score)
