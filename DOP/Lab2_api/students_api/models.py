from django.db import models



class Student(models.Model):
    student_id = models.IntegerField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=64, null=True, blank=False)
    last_name = models.CharField(max_length=64, null=True, blank=False)
    group = models.IntegerField(null=False, blank=False)    
    

class Course(models.Model):
    name = models.CharField(max_length=16, null=False)
    mark = models.IntegerField(null=False, blank=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,  related_name='courses', default=None)
   
    def __str__(self):
        return f'{self.name}: {self.mark}' 
    
