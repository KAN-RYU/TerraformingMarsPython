from django.contrib import admin
from TM.models import TM

# Register your models here.

class TMAdmin(admin.ModelAdmin):
    list_display = ('content', 'last_modified')

admin.site.register(TM, TMAdmin)
