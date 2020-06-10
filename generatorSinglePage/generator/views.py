from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin




class CreatePage(LoginRequiredMixin, TemplateView):
    template_name = 'create_page.html'