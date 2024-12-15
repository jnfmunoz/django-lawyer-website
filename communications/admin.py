from django.contrib import admin
from .models import SocialNetwork, Address, ContactInfo

# Register your models here.
admin.site.register(SocialNetwork)
admin.site.register(Address)
admin.site.register(ContactInfo)