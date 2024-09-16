from django.contrib import admin
from .models import *

# Register your models here.
class MangaAdmin(admin.ModelAdmin):
    list_display = ['name','typee','aounther','reviews','date']
    search_fields = ['name']
    list_editable = ['reviews','date']
    

class ChapterAdmin(admin.ModelAdmin):
    list_display = ['namemanga','numberchapter']
    list_editable = ['numberchapter']
    search_fields = ['numberchapter','namemanga']

class ImageChapterAdmin(admin.ModelAdmin):
    list_display = ['id','chapters']
    search_fields = ['chapters']


class CartitemAdmin(admin.ModelAdmin):
    list_display = ['id','cartmanga']

    

admin.site.register(Manga,MangaAdmin)
admin.site.register(Chapter,ChapterAdmin)
admin.site.register(ImageChapter,ImageChapterAdmin)
admin.site.register(Cartitem,CartitemAdmin)


