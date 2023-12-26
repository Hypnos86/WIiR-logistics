from enum import Enum
import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

logger = logging.getLogger(__name__)

class MenuButton(Enum):
    unit = 'Jednostki'
    contract = 'Umowy'
    project = 'Inwestycje'
    plan = 'Planu'
    donation = 'Darowizny'
    gallery = 'Galeria'

# Create your views here.
class HomeView(LoginRequiredMixin, View):
    template = 'main/home.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            context = {'unit':MenuButton.unit.value, 'contract':MenuButton.contract.value, 'project':MenuButton.contract.value, 'plan':MenuButton.plan.value, 'donation':MenuButton.donation.value, 'gallery':MenuButton.gallery.value}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)
