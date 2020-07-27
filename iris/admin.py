from django.contrib import admin
from .models import IrisResult

# Register your models here.
class IrisAdmin(admin.ModelAdmin):
    list_display = ('classification', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width')

admin.site.register(IrisResult, IrisAdmin)