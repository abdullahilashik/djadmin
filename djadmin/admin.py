from django.contrib import admin
from .models import JobCategory, Job
from django.http import HttpResponse
import csv

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    actions = ['delete_category','export_as_csv']

    def delete_category(self, request, queryset):
        queryset.delete()
        return queryset
    
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        fieldnames = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        self.message_user = 'CSV exported!'

        return response

    
    export_as_csv.short_description = 'Export Selected'
    delete_category.short_description = 'Delete Categories'