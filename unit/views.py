import logging
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from unit.models import County, TypeUnit, Unit

from main.views import MainModule

logger = logging.getLogger(__name__)
# Create your views here.
class UnitListView(LoginRequiredMixin, ListView):
    method = 'UnitListView'
    template_name = 'unit/list_unit.html' 
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            county = County.objects.all()
            

            context = {'title':MainModule.unit.value}
            return render(request, self.template_name, context)
        except Exception as e:
            context = {'error_message':e, 'method':self.method}
            return render(request, self.template_error, context)

    # def get(self, request):
    #     try:
    #         units_active = Unit.objects.filter(status=1).order_by("county")

    #         county = County.objects.all().order_by("id_order")
    #         type_unit = TypeUnit.objects.all()

    #         try:
    #             last_date = Unit.objects.values("change").latest("change")
    #         except Unit.DoesNotExist:
    #             last_date = None

    #         query = "Wyczyść"
    #         search = "Szukaj"
    #         unit_sum = len(units_active)

    #         r = request.GET.get("r")
    #         p = request.GET.get("p")
    #         intP = None
    #         intR = None

    #         if p and r:
    #             units_active = units_active.filter(county__exact=p, type__exact=r)
    #             intR = int(r)
    #             intP = int(p)

    #             # print(units_active.type)
    #             unit_sum_search = len(units_active)
    #             context = {"units": units_active, "county": county, "type_unit": type_unit, "unit_sum": unit_sum,
    #                        "query": query, "unit_sum_search": unit_sum_search, "last_date": last_date, "p": intP,
    #                        "r": intR,
    #                        "actual_units": True}
    #             return render(request, self.template, context)
    #         elif p and not r:
    #             units_active = units_active.filter(county__exact=p)
    #             intP = int(p)


    #             unit_sum_search = len(units_active)
    #             context = {"units": units_active, "county": county, "type_unit": type_unit, "unit_sum": unit_sum,
    #                        "query": query, "unit_sum_search": unit_sum_search, "last_date": last_date, "p": intP,
    #                        "actual_units": True}
    #             return render(request, self.template, context)
    #         elif r and not p:
    #             units_active = units_active.filter(type__exact=r)
    #             intR = int(r)

    #             unit_sum_search = len(units_active)
    #             context = {"units": units_active, "county": county, "type_unit": type_unit, "unit_sum": unit_sum,
    #                        "query": query, "unit_sum_search": unit_sum_search, "last_date": last_date, "r": intR,
    #                        "actual_units": True}
    #             return render(request, self.template, context)

    #         else:
    #             context = {"units": units_active, "county": county, "type_unit": type_unit, "unit_sum": unit_sum,
    #                        "search": search, "last_date": last_date, "actual_units": True}
    #         return render(request, self.template, context)

    #     except Exception as e:
    #         logger.error("Error: %s", e)
    #         context = {'error_message': f"Wystąpił błąd {e}"}
    #         return render(request, self.template_error, context)
        
# class AddUnitView(LoginRequiredMixin, View):
#     template = "units/unit_form.html"
#     template_error = 'main/error_site.html'
#     form_class = UnitForm

#     def get(self, request):
#         try:
#             form = self.form_class()
#             context = {"unit_form": form, "new": True}
#             return render(request, self.template, context)
#         except Exception as e:
#             logger.error("Error: %s", e)
#             context = {'error_message': f"Wystąpił błąd {e}"}
#             return render(request, self.template_error, context)

#     def post(self, request):
#         try:
#             form = self.form_class(request.POST or None)

#             if request.method == "POST":
#                 if form.is_valid():
#                     instance = form.save(commit=False)
#                     instance.author = request.user
#                     form.save()
#                     return redirect("units:create_units_list_editable")
#             return render(request, self.template, {"unit_form": form, "new": True})
#         except Exception as e:
#             logger.error("Error: %s", e)
#             context = {'error_message': f"Wystąpił błąd {e}"}
#             return render(request, self.template_error, context)