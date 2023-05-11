import django_filters

from .models import *

class Filter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {'student_name':['icontains'],
                'student_course':['icontains'],
                'student_group':['icontains'],
                'student_general_works':['icontains'],
                'student_done_works':['icontains'],
                'student_programming_lang':['icontains']}