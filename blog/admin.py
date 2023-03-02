from django.contrib import admin

from blog.models import Sharing, Car, Client

admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Sharing)
