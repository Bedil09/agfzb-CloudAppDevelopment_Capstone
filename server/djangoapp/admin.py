from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display=['make','model_name','style','year','dealer_id']


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]


# CarMakeAdmin class with CarModelInline
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)