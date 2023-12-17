from django.contrib import admin
from work_tracker.models import Category, WorkInstance

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(WorkInstance)
class WorkInstanceModelAdmin(admin.ModelAdmin):
    list_display = ["user", "shift_start", "category", "shift_end"]