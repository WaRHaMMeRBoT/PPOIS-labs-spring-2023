from typing import Any, Dict
from django.views import generic

from .models import *
from .forms import AddNewStudent
from .filters import Filter as FilterStudent

class HomeView(generic.ListView):
    '''Отображает главную страницу со списком последних постов.'''
    
    model = Student
    template_name = 'table/home.html'
    context_object_name = 'table'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        '''Формирует контекст для передачи его шаблону.'''
        
        context = super().get_context_data(**kwargs)
        context['home'] = True
        return context
    
class AddNewRecord(generic.CreateView):
    '''Отображает страницу с добавлением новой записи в таблицу.'''
    
    form_class = AddNewStudent
    template_name = 'table/addstudent.html'
    success_url = '/'
    
class DeleteRecord(generic.DeleteView):
    '''Удаляет запись таблицы.'''
    model = Student
    success_url = '/'
    
    
class Filter(generic.ListView):
    model=Student
    template_name = 'table/filter_student.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['filter'] = FilterStudent(self.request.GET, queryset = self.get_queryset())
        context['home'] = False
        return context