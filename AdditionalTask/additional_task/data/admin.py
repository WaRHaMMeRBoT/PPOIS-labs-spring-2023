from django.contrib import admin
from .models import Medicine


class AdminMedicine(admin.ModelAdmin):
    fields = ("name", "address", "date_of_birth", "date_of_visit", "name_of_doctor", "conclusion")


admin.site.register(Medicine, AdminMedicine)
