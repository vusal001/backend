from django.contrib import admin
from .models import *

class ImageInline(admin.TabularInline):
    model = Images
    extra = 0

    
class PersonAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Post, PersonAdmin)
admin.site.register(Images)
# Register your models here.
