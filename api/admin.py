from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Content)
admin.site.register(Subject)
admin.site.register(Tag)