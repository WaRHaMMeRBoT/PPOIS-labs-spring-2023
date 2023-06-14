from django.urls import path
from .views import main_page, filtering, creating, deleting

urlpatterns = [
    path('main/', main_page, name="main_page"),
    path("filter/", filtering, name="filtering"),
    path("create/", creating, name="creating"),
    path("delete/", deleting, name="deleting")
]
