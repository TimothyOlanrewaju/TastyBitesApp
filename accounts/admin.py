from django.contrib import admin
from . models import *



admin.site.register(User)
admin.site.register(Unit)
admin.site.register(Department)
admin.site.register(Gender)
admin.site.register(UserGroup)