from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('new_record/', cache_page(3600)(views.AddNewRecord.as_view()), name='add_student'),
    path('delete/<int:pk>', cache_page(3600)(views.DeleteRecord.as_view()), name='delete_line'),
    path('filter/', views.Filter.as_view(), name='filter'),
]