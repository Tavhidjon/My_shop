from django.contrib import admin

from .models import *
admin.site.register(Person)
admin.site.register(Register)
admin.site.register(Customer)
admin.site.register(Cart)