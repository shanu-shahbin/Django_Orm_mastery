from django.contrib import admin
from .models import Students, Marks, Students_details

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'year_in_school', 'created_at')
    search_fields = ('name', 'roll_no')
    list_filter = ('year_in_school', 'created_at')
    ordering = ('roll_no',)
    readonly_fields = ('created_at',)

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'maths', 'physics', 'chemistry', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('student__name',)

@admin.register(Students_details)
class StudentsDetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name')
    search_fields = ('first_name', 'second_name')
