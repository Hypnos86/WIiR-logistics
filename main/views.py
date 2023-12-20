import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

logger = logging.getLogger(__name__)


# Create your views here.
class HomeView(LoginRequiredMixin, View):
    template = 'main/home.html'
    template_error = 'main/error_site.html'

    def get(self, request):
        try:
            context = {}
            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
            return render(request, self.template_error, context)
