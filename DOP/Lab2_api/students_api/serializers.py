from rest_framework import serializers

from .models import Student, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'mark')


class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(many=True)
    class Meta:
        model = Student
        fields = ['id','student_id', 'first_name', 'last_name', 'group', 'courses']
    
