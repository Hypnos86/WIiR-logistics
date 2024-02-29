import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from plan.forms import PlanModelForm
from main.views import MainModule, GroupPermission
from plan.models import Section, Group, Paragraph, Source, PlanModel, FinanceSource, PriorityModel

logger = logging.getLogger(__name__)


class PlanListView(LoginRequiredMixin, View):
    method = 'PlanListView'
    template_name = 'plan/list_plan.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        unit_group = request.user.groups.filter(name=GroupPermission.unit.value).exists()
        contract_group = request.user.groups.filter(name=GroupPermission.contract.value).exists()
        project_group = request.user.groups.filter(name=GroupPermission.project.value).exists()
        plan_group = request.user.groups.filter(name=GroupPermission.plan.value).exists()
        donation_group = request.user.groups.filter(name=GroupPermission.donation.value).exists()
        gallery_group = request.user.groups.filter(name=GroupPermission.gallery.value).exists()
        try:
            # Tworzenie obiektów do modułu
            section = Section.objects.all()
            if not section.exists():
                Section.create_sections()

            group = Group.objects.all()
            if not group.exists():
                Group.create_groups()

            paragraph = Paragraph.objects.all()
            if not paragraph.exists():
                Paragraph.create_paragraphs()

            source = Source.objects.all()
            if not source.exists():
                Source.create_sources()

            priority = PriorityModel.objects.all()
            if not priority.exists():
                PriorityModel.create_priority()

            # ----------KONIEC------------
            plans = PlanModel.objects.all()
            planQuantity = len(plans)

            context = {'title': MainModule.plan.value, 'unit_group': unit_group, 'contract_group': contract_group,
                       'project_group': project_group, 'plan_group': plan_group, 'donation_group': donation_group,
                       'gallery_group': gallery_group, 'plans': plans, 'planQuantity': planQuantity}
            return render(request, self.template_name, context)
        except Exception as e:
            context = {'error_message': e, 'method': self.method}
            return render(request, self.template_error, context)


class DetailsPlanView(LoginRequiredMixin, View):
    method = 'DetailsPlanView'
    template_name = 'plan/details_plan.html'
    template_error = 'main/error_site.html'

    def get(self, request, planId):
        unit_group = request.user.groups.filter(name=GroupPermission.unit.value).exists()
        contract_group = request.user.groups.filter(name=GroupPermission.contract.value).exists()
        project_group = request.user.groups.filter(name=GroupPermission.project.value).exists()
        plan_group = request.user.groups.filter(name=GroupPermission.plan.value).exists()
        donation_group = request.user.groups.filter(name=GroupPermission.donation.value).exists()
        gallery_group = request.user.groups.filter(name=GroupPermission.gallery.value).exists()
        try:

            plans = PlanModel.objects.all()
            planQuantity = len(plans)
            plan = get_object_or_404(PlanModel, pk=planId)

            context = {'title': MainModule.plan.value, 'unit_group': unit_group, 'contract_group': contract_group,
                       'project_group': project_group, 'plan_group': plan_group, 'donation_group': donation_group,
                       'gallery_group': gallery_group, 'plan': plan, 'planQuantity': planQuantity}
            return render(request, self.template_name, context)
        except Exception as e:
            context = {'error_message': e, 'method': self.method}
            return render(request, self.template_error, context)


class ModalAddPlanView(LoginRequiredMixin, View):
    method = 'ModalPlanView'
    template_name = 'plan/modal_form_plan.html'
    template_error = 'main/error_site.html'
    from_class = PlanModelForm

    def get(self, request):
        try:
            form = self.from_class()
            context = {'form': form, 'new': True}
            return render(request, self.template_name, context)
        except Exception as e:
            logger.error("Wystąpił błąd: %s", e)
            context = {'error_message': e, 'method': self.method}
            return render(request, self.template_error, context)

    def post(self, request):
        try:
            form = self.from_class(request.POST or None)
            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.author = request.user
                    instance.save()
                    return redirect('plan:planList')

            context = {'form': form, 'new': True}
            return render(request, self.template_name, context)
        except Exception as e:
            logger.error("Wystąpił błąd: %s", e)
            context = {'error_message': e, 'method': self.method}
            return render(request, self.template_error, context)


class ChangesPlanView(LoginRequiredMixin, View):
    method = 'ChangesPlanView'
    template_name = 'plan/modal_plan_changes.html'
    template_error = 'main/error_site.html'

    def get(self, request, plan_id):
        try:
            plan = PlanModel.objects.get(pk=plan_id)
            changes = plan.history.all()  # Pobierz historię zmian

            for x in changes:
                print(vars(x))

            context = {'plan': plan, 'changes': changes}
            return render(request, self.template_name, context)

        except Exception as e:
            logger.error("Wystąpił błąd: %s", e)
            context = {'error_message': e, 'method': self.method}
            return render(request, self.template_error, context)
