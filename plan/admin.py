from django.contrib import admin
from plan.models import Source, Group, Section, Paragraph, FinanceSource, ItemPlanModel, PlanModel, PriorityModel


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'section', 'name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group', 'name']


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ['paragraph', 'name']


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['source', 'name']


@admin.register(FinanceSource)
class FinanceSourceAdmin(admin.ModelAdmin):
    list_display = ['section', 'group', 'paragraph', 'source']


@admin.register(PriorityModel)
class PriorityModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ItemPlanModel)
class ItemPlanModelAdmin(admin.ModelAdmin):
    list_display = ['unit', 'task', 'cost', 'create']


@admin.register(PlanModel)
class PlanModelAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'tasks_cost', 'create']
