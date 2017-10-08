from django.contrib import admin
from .models import Schedule
from .models import Person
from .models import Batch

admin.site.register(Schedule)
admin.site.register(Person)
admin.site.register(Batch)
# Register your models here.
