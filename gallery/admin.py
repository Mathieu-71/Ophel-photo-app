from django.contrib import admin
from .models import *

class ImageAdmin(admin.ModelAdmin):
    list_display   = ('picture', 'category', 'date_created',)
    list_filter    = ('picture', 'category', 'date_created',)
    date_hierarchy = 'date_created'
    ordering       = ('date_created',)
    search_fields  = ('picture', 'category')

admin.site.register(Category)
admin.site.register(Image, ImageAdmin)