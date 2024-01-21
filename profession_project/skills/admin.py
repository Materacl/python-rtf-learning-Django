from django.contrib import admin
from .models import TopSkillsAll, TopSkillsProf
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class TopSkillsAllResource(resources.ModelResource):
    class Meta:
        model = TopSkillsAll


class TopSkillsAllAdmin(ImportExportModelAdmin):
    resource_class = TopSkillsAllResource


class TopSkillsProfResource(resources.ModelResource):
    class Meta:
        model = TopSkillsProf


class TopSkillsProfAdmin(ImportExportModelAdmin):
    resource_class = TopSkillsProf


@admin.register(TopSkillsAll)
class TopSkillsAllAdmin(ImportExportModelAdmin):
    pass


@admin.register(TopSkillsProf)
class TopSkillsProfAdmin(ImportExportModelAdmin):
    pass


# admin.site.register(TopSkillsAll, TopSkillsAllAdmin)
# admin.site.register(TopSkillsProf, TopSkillsProfAdmin)
