from django.contrib import admin
from .models import AreaSalaryAll, AreaCountAll, AreaSalaryProf, AreaCountProf
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AreaSalaryAllResource(resources.ModelResource):
    class Meta:
        model = AreaSalaryAll


class AreaSalaryAllAdmin(ImportExportModelAdmin):
    resource_class = AreaSalaryAllResource


class AreaCountAllResource(resources.ModelResource):
    class Meta:
        model = AreaCountAll


class AreaCountAllAdmin(ImportExportModelAdmin):
    resource_class = AreaCountAllResource


class AreaSalaryProfResource(resources.ModelResource):
    class Meta:
        model = AreaSalaryProf


class AreaSalaryProfAdmin(ImportExportModelAdmin):
    resource_class = AreaSalaryProfResource


class AreaCountProfResource(resources.ModelResource):
    class Meta:
        model = AreaCountProf


class AreaCountProfAdmin(ImportExportModelAdmin):
    resource_class = AreaCountProfResource


admin.site.register(AreaSalaryAll, AreaSalaryAllAdmin)
admin.site.register(AreaCountAll, AreaCountAllAdmin)
admin.site.register(AreaSalaryProf, AreaSalaryProfAdmin)
admin.site.register(AreaCountProf, AreaCountProfAdmin)
