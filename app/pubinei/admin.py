from django.contrib import admin
from .models import Pubinei

# Register your models here.
@admin.register(Pubinei)
class PubineiAdmin(admin.ModelAdmin):
    list_display = ('key', 'value') 