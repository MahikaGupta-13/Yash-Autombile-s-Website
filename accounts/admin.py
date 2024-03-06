from django.contrib import admin
from django.contrib.auth.models import User
import csv
from django.http import HttpResponse

admin.site.unregister(User) 

# Register your models here.
class StudentTec(admin.ModelAdmin):
    list_display= ('username', 'first_name', 'last_name', 'email', )
    list_filter = ["is_staff" ]

    actions = ['generate_csv_report']

    def generate_csv_report(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="student_report.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['id','username', 'First Name','Last Name', 'email'])
        
        for student in queryset:
            writer.writerow([f'STU-00{student.id}', student.username, student.first_name, student.last_name,  student.email])  # Replace with your model fields
        
        return response

    generate_csv_report.short_description = "Generate CSV Report"



admin.site.register(User, StudentTec)