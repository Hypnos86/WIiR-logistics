import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
<<<<<<< HEAD

from main.views import MainModule, GroupPermission

logger = logging.getLogger(__name__)


# Create your views here.
class GalleryListView(LoginRequiredMixin, View):
    template = "gallery/list_gallery.html"
=======

from main.views import MainModule, GroupPermission

logger = logging.getLogger(__name__)


class GalleryListView(LoginRequiredMixin, View):
    method = "GalleryListView"
    template_name = "gallery/list_gallery.html"
>>>>>>> 17099ceb532e315c9c8d4063c785f67955ad4583
    template_error = 'main/error_site.html'

    def get(self, request):
        unit_group = request.user.groups.filter(name=GroupPermission.unit.value).exists()
        contract_group = request.user.groups.filter(name=GroupPermission.contract.value).exists()
        project_group = request.user.groups.filter(name=GroupPermission.project.value).exists()
        plan_group = request.user.groups.filter(name=GroupPermission.plan.value).exists()
        donation_group = request.user.groups.filter(name=GroupPermission.donation.value).exists()
        gallery_group = request.user.groups.filter(name=GroupPermission.gallery.value).exists()
        try:
<<<<<<< HEAD
            # galleries = Gallery.objects.all()
            # gallery_count = len(galleries)
            # context = {'galleries': galleries,
            #            'gallery_count': gallery_count}
            # return render(request, self.template, context)
            context = {'title': MainModule.gallery.value, 'unit_group': unit_group, 'contract_group': contract_group,
                       'project_group': project_group, 'plan_group': plan_group, 'donation_group': donation_group,
                       'gallery_group': gallery_group}

            return render(request, self.template, context)
        except Exception as e:
            logger.error("Error: %s", e)
            context = {'error_message': f"Wystąpił błąd {e}"}
=======

            context = {'title': MainModule.gallery.value, 'unit_group': unit_group, 'contract_group': contract_group,
                       'project_group': project_group, 'plan_group': plan_group, 'donation_group': donation_group,
                       'gallery_group': gallery_group}
            return render(request, self.template_name, context)
        except Exception as e:
            context = {'error_message': e, 'method': self.method}
>>>>>>> 17099ceb532e315c9c8d4063c785f67955ad4583
            return render(request, self.template_error, context)
