from django.contrib import admin
from .models import *

# Register your models here.
"""class signupData(admin.ModelAdmin):
    list_display=['id','firstname','lastname','username','password','state','city','mobile']"""

admin.site.register(signmodel)