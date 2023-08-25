from django.contrib import admin
from .models import Advertisements

class AdvertisementsAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Advertisements,AdvertisementsAdmin)
