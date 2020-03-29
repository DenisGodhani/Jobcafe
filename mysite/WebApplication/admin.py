from django.contrib import admin
from .models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# Register your models here.

admin.site.register(User)