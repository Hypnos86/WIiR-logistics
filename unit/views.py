import logging
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from unit.models import County, TypeUnit, Unit

from main.views import MainModule, GroupPermission

logger = logging.getLogger(__name__)


# Create your views here.
class CountyListView(LoginRequiredMixin, View):
    method = 'CountyListView'
    template_name = 'unit/list_county.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        unit_group = request.user.groups.filter(name=GroupPermission.unit.value).exists()
        contract_group = request.user.groups.filter(name=GroupPermission.contract.value).exists()
        project_group = request.user.groups.filter(name=GroupPermission.project.value).exists()
        plan_group = request.user.groups.filter(name=GroupPermission.plan.value).exists()
        donation_group = request.user.groups.filter(name=GroupPermission.donation.value).exists()
        gallery_group = request.user.groups.filter(name=GroupPermission.gallery.value).exists()
        try:
            counties = County.objects.all()
            if not counties.exists():
                County.create_county()

            typesUnit = TypeUnit.objects.all()
            if not typesUnit.exists():
                TypeUnit.create_type_unit()

            units = Unit.objects.all().filter(status=True)
            unit_count = len(units)

            kmp_units = len(units.filter(type__type_short='KMP'))
            kpp_units = len(units.filter(type__type_short='KPP'))
            kp_units = len(units.filter(type__type_short='KP'))
            pp_units = len(units.filter(type__type_short='PP'))
            rd_units = len(units.filter(type__type_short='RD'))

            context = {'title': MainModule.unit.value, 'counties': counties, 'unit_count': unit_count,
                       'kmp_units': kmp_units, 'kpp_units': kpp_units, 'pp_units': pp_units, 'kp_units': kp_units,
                       'rd_units': rd_units,
                       'unit_group': unit_group, 'contract_group': contract_group, 'project_group': project_group,
                       'plan_group': plan_group, 'donation_group': donation_group, 'gallery_group': gallery_group}
            return render(request, self.template_name, context)
        except Exception as e:
            context = {'error_message': e, 'method': self.method}
            return render(request, self.template_error, context)


class UnitList(LoginRequiredMixin, View):
    method = 'UnitListView'
    template_name = 'unit/list_unit.html'
    template_error = 'main/error_site.html'

    def get(self, request, county_slug):
        unit_group = request.user.groups.filter(name=GroupPermission.unit.value).exists()
        contract_group = request.user.groups.filter(name=GroupPermission.contract.value).exists()
        project_group = request.user.groups.filter(name=GroupPermission.project.value).exists()
        plan_group = request.user.groups.filter(name=GroupPermission.plan.value).exists()
        donation_group = request.user.groups.filter(name=GroupPermission.donation.value).exists()
        gallery_group = request.user.groups.filter(name=GroupPermission.gallery.value).exists()
        try:
            county = County.objects.get(slug=county_slug)
            units = Unit.objects.all().filter(status=True).filter(county__slug=county_slug)
            unit_count = len(units)

            kmp_units = len(units.filter(type__type_short='KMP'))
            kpp_units = len(units.filter(type__type_short='KPP'))
            kp_units = len(units.filter(type__type_short='KP'))
            pp_units = len(units.filter(type__type_short='PP'))
            rd_units = len(units.filter(type__type_short='RD'))

            context = {'title': county, 'unit_count': unit_count, 'units': units,
                       'kmp_units': kmp_units, 'kpp_units': kpp_units, 'pp_units': pp_units, 'kp_units': kp_units,
                       'rd_units': rd_units,
                       'unit_group': unit_group, 'contract_group': contract_group, 'project_group': project_group,
                       'plan_group': plan_group, 'donation_group': donation_group, 'gallery_group': gallery_group}
            return render(request, self.template_name, context)
        except Exception as e:
            context = {'error_message': e, 'method': self.method}
            return render(request, self.template_error, context)
