from django.contrib import admin

# Register your models here.
from .models import Querry
from .models import customers
admin.site.register(Querry)
admin.site.register(customers)