from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(StudentDetails)
admin.site.register(TrainerDetails)
admin.site.register(Courses)
admin.site.register(StudentEnroled)