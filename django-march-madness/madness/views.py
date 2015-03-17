import logging

from braces.views import JsonRequestResponseMixin, LoginRequiredMixin
from django.views.generic.base import TemplateView

from .models import Bracket

log = logging.getLogger(__name__)


class EnterPicksView(LoginRequiredMixin, JsonRequestResponseMixin, TemplateView):
    template_name = 'brackets/entry.html'

    def get_context_data(self, **kwargs):
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
