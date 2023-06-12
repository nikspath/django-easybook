from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Subject)
class StudentMarksAdmin(admin.ModelAdmin):
	list_display=['student','subject','marks']
admin.site.register(StudentMarks,StudentMarksAdmin)