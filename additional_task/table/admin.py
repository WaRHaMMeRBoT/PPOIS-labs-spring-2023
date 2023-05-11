from django.contrib import admin

from .models import *


class StudentsAdmin(admin.ModelAdmin):
    '''Отображает информацию о модели Student в админ панели.'''
    
    list_display = (
        'id',
        'student_name',
        'student_course',
        'student_group',
        'student_general_works',
        'student_done_works',
        'student_programming_lang')
    search_fields = ('id', 'student_name')
    list_display_links = ('student_name', 'id')


admin.site.register(Student, StudentsAdmin)
