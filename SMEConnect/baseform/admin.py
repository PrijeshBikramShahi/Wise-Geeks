from django.contrib import admin
from .models import *

# Register your models here.
class InvestorAdmin(admin.ModelAdmin):
    list_fields = ("investor", "email", "linkedin","bio", "reg_Date" )

class startupAdmin(admin.ModelAdmin):
    list_fields = ("startup_name", "email", "des","reg_no", "reg_Date" )


admin.site.register(investor, InvestorAdmin)
admin.site.register(startup, startupAdmin)