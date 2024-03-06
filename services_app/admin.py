from django.contrib import admin
from .models import *
# Register your models here.

class Display(admin.ModelAdmin):
    list_display = (
'bikeName',
'model_no',
'problem',
'time',
    )

    
admin.site.register(ServiceBooking,Display)
admin.site.register(SendMessage)
admin.site.register(Question)
admin.site.register(Answer)