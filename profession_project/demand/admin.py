from django.contrib import admin
from .models import DynamicSalaryAll, DynamicCountAll, DynamicSalaryProf, DynamicCountProf
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class DynamicSalaryAllResource(resources.ModelResource):
    class Meta:
        model = DynamicSalaryAll


class DynamicSalaryAllAdmin(ImportExportModelAdmin):
    resource_classes = [DynamicSalaryAllResource]


class DynamicCountAllResource(resources.ModelResource):
    class Meta:
        model = DynamicCountAll


class DynamicCountAllAdmin(ImportExportModelAdmin):
    resource_classes = [DynamicCountAllResource]


class DynamicSalaryProfResource(resources.ModelResource):
    class Meta:
        model = DynamicSalaryProf


class DynamicSalaryProfAdmin(ImportExportModelAdmin):
    resource_classes = [DynamicSalaryProfResource]


class DynamicCountProfResource(resources.ModelResource):
    class Meta:
        model = DynamicCountProf


class DynamicCountProfAdmin(ImportExportModelAdmin):
    resource_classes = [DynamicCountProfResource]


admin.site.register(DynamicSalaryAll, DynamicSalaryAllAdmin)
admin.site.register(DynamicSalaryProf, DynamicSalaryProfAdmin)
admin.site.register(DynamicCountAll, DynamicCountAllAdmin)
admin.site.register(DynamicCountProf, DynamicCountProfAdmin)
