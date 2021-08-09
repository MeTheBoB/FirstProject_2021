from django.views import generic
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)



class HomeView(generic.TemplateView):
    template_name = 'index.html'
