from braces.views import LoginRequiredMixin
from django.views.generic.base import TemplateView

from .models import Bracket


class EnterPicksView(LoginRequiredMixin, TemplateView):
    template_name = 'brackets/entry.html'

    def get_context_data(self, **kwargs):
        context = super(EnterPicksView, self).get_context_data(**kwargs)
        context['bracket'] = Bracket.objects.filter(year=2015)
        return context
