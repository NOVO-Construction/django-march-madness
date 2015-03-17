import logging

from braces.views import JsonRequestResponseMixin, LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .models import Bracket
from .forms import EntryForm

log = logging.getLogger(__name__)


class CreateEntryView(LoginRequiredMixin, FormView):
	template_name = 'brackets/create.html'
	form_class = EntryForm

	def get_context_data(self, **kwargs):
		context = super(CreateEntryView, self).get_context_data(**kwargs)
		return context


class EnterPicksView(LoginRequiredMixin, JsonRequestResponseMixin, TemplateView):
    template_name = 'brackets/entry.html'

    def get_context_data(self, pk, **kwargs):
        context = super(EnterPicksView, self).get_context_data(**kwargs)
        context['bracket'] = Bracket.objects.filter(year=2015)
        return context

    def post(self, request, *args, **kwargs):
        log.debug(self.request_json)
        try:
            game = self.request_json['game']
        except KeyError:
            return self.render_bad_request_response({'message': ('Your pick has been made')})
        message = 'Created pick for user {} game {}'.format(request.user, game)
        log.debug(message)
        return self.render_json_response({'message': message})


class RulesView(TemplateView):
    template_name = 'pages/rules.html'

    def get_context_data(self, **kwargs):
        context = super(RulesView, self).get_context_data(**kwargs)
        return context