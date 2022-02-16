from django.contrib import admin
# from .models import related models
from .models import *

# Register your models here.

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 3

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display=['make','model','style','year','dealerId']


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display=('name','description')
    list_filter=['name']
    search_fields=['name','description']


# CarMakeAdmin class with CarModelInline
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)


