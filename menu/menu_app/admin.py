from django.contrib import admin
from menu_app.models import Menu, MenuItem
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class MenuItemAdmin(TreeAdmin):
    form = movenodeform_factory(MenuItem)
    list_display = ['name', 'menu_name']

class MenuItemInline(admin.TabularInline):
    model = MenuItem

class MenuAdmin(admin.ModelAdmin):
    model = Menu
    inlines = [
        MenuItemInline,
    ]

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
