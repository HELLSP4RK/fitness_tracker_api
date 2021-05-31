from django.contrib import admin
from django.contrib.admin import ModelAdmin

from api.models import *


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass


@admin.register(Workout)
class WorkoutAdmin(ModelAdmin):
    pass
