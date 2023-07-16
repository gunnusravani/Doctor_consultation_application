from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Doctors)
admin.site.register(Blood)
admin.site.register(Appointment)
