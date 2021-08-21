from django.contrib import admin

# Register your models here.

from .models import Student_Information, Distinguish

admin.site.register(Student_Information)
admin.site.register(Distinguish)

