from apps.login_reg.models import User as U
from django.contrib import admin

class UAdmin(admin.ModelAdmin):
    pass
admin.site.register(U, UAdmin)