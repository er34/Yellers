from django.contrib import admin
from accounts.models import Account, Interest, UInterest, Country, Kladr 
from messages.models import Message

admin.site.register(Account)
admin.site.register(Interest)
admin.site.register(UInterest)
admin.site.register(Country)
admin.site.register(Kladr)
admin.site.register(Message)