from django.contrib import admin
from unit.models import County, TypeUnit, Unit


# Register your models here.

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_order')
    list_display_links = ('name',)


@admin.register(TypeUnit)
class TypeUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_short', 'type_full', 'id_order')
    list_display_links = ('type_full',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'county', 'type', 'address', 'city', 'author', 'create')
    list_display_links = ('county', 'type', 'address', 'city')
    search_fields = ['type', 'address', 'city']
    list_filter = ['county']

