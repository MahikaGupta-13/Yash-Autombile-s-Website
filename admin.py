from django.contrib import admin
from .models import *
import csv
from django.http import HttpResponse

# Register your models here.
admin.site.register(ContactTable)
admin.site.register(TestModel)
admin.site.register(Category)

class Display(admin.ModelAdmin):
    list_display = (
        'category',
'brand',
'name',
'price',
    )
class DisplayBookings(admin.ModelAdmin):
    list_display = (
        'user',
'vecname',
'price',
    )
    actions = ['generate_csv_report']

    def generate_csv_report(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="student_report.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['id','Username', 'Vechile Name','Price'])
        
        for student in queryset:
            writer.writerow([f'STU-00{student.id}', student.user, student.vecname, student.price])  # Replace with your model fields
        
        return response

    generate_csv_report.short_description = "Generate CSV Report"

admin.site.register(VecTable, Display)
admin.site.register(Brands)
admin.site.register(BookVechicle,DisplayBookings)




