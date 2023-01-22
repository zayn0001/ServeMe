from django.contrib import admin
from .models import Diner, Manager, Layout, Menu, FoodItem

class DinerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Diner, DinerAdmin)

class ManagerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Manager, ManagerAdmin)

class LayoutAdmin(admin.ModelAdmin):
    pass
admin.site.register(Layout, LayoutAdmin)

class MenuAdmin(admin.ModelAdmin):
    pass
admin.site.register(Menu, MenuAdmin)

class FoodItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(FoodItem, FoodItemAdmin)