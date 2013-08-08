from django.contrib import admin
import reversion
from career.models import Job, JobCategory, City

__author__ = 'beam'


class JobAdmin(reversion.VersionAdmin):
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


class JobCategoryAdmin(reversion.VersionAdmin):
    pass


class CityAdmin(reversion.VersionAdmin):
    pass


admin.site.register(Job, JobAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(City, CityAdmin)