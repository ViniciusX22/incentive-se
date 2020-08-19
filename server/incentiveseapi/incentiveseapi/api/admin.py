from django.contrib import admin
from .models import Incentive, Request

# Register your models here.


@admin.register(Incentive)
class IncentiveAdmin(admin.ModelAdmin):
    pass


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    pass
