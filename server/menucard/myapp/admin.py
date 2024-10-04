from django.contrib import admin
from .models import *
from django.utils.html import format_html

class Menu_itemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'prize', 'offer', 'image_thumbnail','hide')

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height:50px;" />'.format(obj.image.url))
        return ""
    image_thumbnail.short_description = 'Image Thumbnail'

admin.site.register(Menu_items, Menu_itemsAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'prize', 'quantity','result','tablenumber')
admin.site.register(Order, OrderAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category_name', 'Category_image')
admin.site.register(Category, CategoryAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
admin.site.register(Login, LoginAdmin)