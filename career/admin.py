from django.contrib import admin
from career.models import Job, JobCategory, City

__author__ = 'beam'


class JobAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city',
        'employer',
        'status',
    )
    list_filter = (
        'name',
        'city',
        'employer',
        'status',
    )
    ordering = (
        'name',
        'city',
        'employer',
        'status',
    )
    search_fields = (
        'name',
        'city',
        'employer',
        'status',
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class JobCategoryAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Job, JobAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(City, CityAdmin)