from django import forms 

from .models import Student

class AddNewStudent(forms.ModelForm):
    '''Форма для слздания новых записей в таблице.'''
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Student
        fields = ['student_name',
                'student_course',
                'student_group',
                'student_general_works',
                'student_done_works',
                'student_programming_lang']
        widgets = {
            'student_name': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'ФИО студента'}),
            'student_course': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Курс'}),
            'student_group': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Группа'}),
            'student_general_works': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Общее число работ'}),
            'student_done_works': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Количество выпол. работ'}),
            'student_programming_lang': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Язык программирования'}),
        }