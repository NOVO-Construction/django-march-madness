import logging

from braces.views import JsonRequestResponseMixin, LoginRequiredMixin, AjaxResponseMixin
from django.views.generic import DetailView, View
from django.views.generic.edit import CreateView

from . import forms, models

log = logging.getLogger(__name__)


class CreateEntryView(LoginRequiredMixin, CreateView):
    template_name = 'brackets/create.html'
    form_class = forms.EntryForm
    model = models.Entry

    def get_initial(self):
        initial = super(CreateEntryView, self).get_initial()
        initial.update(self.request.GET.dict())
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.tie_break = 0
        self.object = form.save()
        return super(CreateEntryView, self).form_valid(form)


class EnterPicksView(LoginRequiredMixin, DetailView):
    context_object_name = 'entry'
    model = models.Entry
    template_name = 'brackets/entry.html'

    def get_context_data(self, **kwargs):
        context = super(EnterPicksView, self).get_context_data(**kwargs)
        context['bracket'] = models.Bracket.objects.filter(year=2015)
        return context

    def get_queryset(self):
        return models.Entry.objects.filter(user=self.request.user)


class EnterPicksAjaxView(LoginRequiredMixin, JsonRequestResponseMixin, AjaxResponseMixin, DetailView):
    # require_json = True
    model = models.Entry

    def get_queryset(self):
        return models.Entry.objects.filter(user=self.request.user)

    def get_ajax(self, request, *args, **kwargs):
        log.debug(self.request_json)
        return self.render_json_response({'message': 'fpp'})

    def post_ajax(self, request, *args, **kwargs):
        log.debug(self.request_json)
        try:
            game = self.request_json['game']
        except KeyError:
            return self.render_bad_request_response({'message': ('Your pick has been made')})
        message = 'Created pick for user {} game {}'.format(request.user, game)
        log.debug(message)
        return self.render_json_response({'message': message})
