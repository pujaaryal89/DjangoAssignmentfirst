from django.contrib import admin
from django.views.generic import *
from .models import Blog,Author

# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
