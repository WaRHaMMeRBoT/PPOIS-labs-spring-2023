from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

# from .views import list_students
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'', StudentViewSet)



urlpatterns = [
    path('', include(router.urls)),
    #path('students/', list_students),  
    path('admin/', admin.site.urls),
]