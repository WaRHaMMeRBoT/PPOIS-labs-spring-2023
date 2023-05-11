from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import F
from django.contrib.auth.models import User

class Student(models.Model):
    '''Модель для реализации каждой строки таблицы.'''
    student_name = models.CharField(max_length=200, verbose_name='Имя студента')
    student_course = models.PositiveIntegerField(verbose_name='Курс')
    student_group = models.PositiveIntegerField(verbose_name='Группа')
    student_general_works = models.PositiveIntegerField(verbose_name='Общее число работ')
    student_done_works = models.PositiveIntegerField(verbose_name='Количество выполненных работ')
    student_programming_lang = models.CharField(max_length=20 ,verbose_name='Язык программирования')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        
    def get_absolute_url(self):
        return reverse('home', kwargs={'id': self.pk})