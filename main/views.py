from enum import Enum
import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views import View

logger = logging.getLogger(__name__)

class MainModule(Enum):
    unit = 'Jednostki'
    contract = 'Umowy'
    project = 'Inwestycje'
    plan = 'Plany'
    donation = 'Darowizny'
    gallery = 'Galeria'

class GroupPermission(Enum):
    unit = 'Unit'
    unit_edit = 'Unit Edit'
    contract = 'Contract'
    contract_edit = 'Contract Edit'
    project = 'Project'
    project_edit = 'Project Edit'
    plan = 'Plan'
    plan_edit = 'Plan Edit'
    donation = 'Donation'
    donation_edit = 'Donation Edit'
    gallery = 'Gallery'
    gallery_edit = 'Gallery Edit'



# Create your views here.
class HomeView(LoginRequiredMixin, View):
    template = 'main/home.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            unit, create = Group.objects.get_or_create(name=GroupPermission.unit.value)
            unit_edit_group, create = Group.objects.get_or_create(name=GroupPermission.unit_edit.value)
            contract, create = Group.objects.get_or_create(name=GroupPermission.contract.value)
            contract_edit_group, create = Group.objects.get_or_create(name=GroupPermission.contract_edit.value)
            project, create = Group.objects.get_or_create(name=GroupPermission.project.value)
            project_edit_group, create = Group.objects.get_or_create(name=GroupPermission.project_edit.value)
            plan, create = Group.objects.get_or_create(name=GroupPermission.plan.value)
            plan_edit_group, create = Group.objects.get_or_create(name=GroupPermission.plan_edit.value)
            donation, create = Group.objects.get_or_create(name=GroupPermission.donation.value)
            donation_edit_group, create = Group.objects.get_or_create(name=GroupPermission.donation_edit.value)
            gallery, create = Group.objects.get_or_create(name=GroupPermission.gallery.value)
            gallery_edit_group, create = Group.objects.get_or_create(name=GroupPermission.gallery_edit.value)

            unit_group = request.user.groups.filter(name=GroupPermission.unit.value).exists()
            contract_group = request.user.groups.filter(name=GroupPermission.contract.value).exists()
            project_group = request.user.groups.filter(name=GroupPermission.project.value).exists()
            plan_group = request.user.groups.filter(name=GroupPermission.plan.value).exists()
            donation_group = request.user.groups.filter(name=GroupPermission.donation.value).exists()
            gallery_group = request.user.groups.filter(name=GroupPermission.gallery.value).exists()

            context = {'unit':MainModule.unit.value, 'contract':MainModule.contract.value, 'project':MainModule.contract.value, 'plan':MainModule.plan.value, 'donation':MainModule.donation.value, 'gallery':MainModule.gallery.value, 'unit_group':unit_group, 'contract_group':contract_group, 'project_group':project_group, 'plan_group':plan_group, 'donation_group':donation_group, 'gallery_group':gallery_group}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)
