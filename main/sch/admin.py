from django.contrib import admin
from .models import Schedule
from .models import Person
from .models import Batch
from .models import KeyVal
from .models import Dicty

admin.site.register(Schedule)
admin.site.register(Person)
admin.site.register(Batch)
admin.site.register(Dicty)
admin.site.register(KeyVal)
# Register your models here.
