from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Entrepreneur)
admin.site.register(Company)
admin.site.register(Review)
