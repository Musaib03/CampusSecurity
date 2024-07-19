from django.contrib import admin

# Register your models here.
from .models import Block, Shift, Employee, Assignment, Attendance, Leave

# Register each model with the admin site
admin.site.register(Block)
admin.site.register(Shift)
admin.site.register(Employee)
admin.site.register(Assignment)
admin.site.register(Attendance)
admin.site.register(Leave)
