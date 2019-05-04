from django.contrib import admin

# Register your models here.

from produktet.models import Produkte, Kategorite, AddToCart, Commentsection

admin.site.register(Produkte)
admin.site.register(Kategorite)
admin.site.register(AddToCart)
admin.site.register(Commentsection)