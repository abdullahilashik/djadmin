from django.contrib import admin
from .models import JobCategory, Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    actions = ['delete_category']

    def delete_category(self, request, queryset):
        queryset.delete()
        return queryset
    
    delete_category.short_description = 'Delete Categories'