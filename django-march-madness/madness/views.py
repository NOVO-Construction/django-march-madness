import logging

from braces.views import JsonRequestResponseMixin, LoginRequiredMixin
from django.conf import settings
from django.views.generic import DetailView, TemplateView
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
        context['locked'] = settings.LOCK_BRACKETS
        return context

    def get_queryset(self):
        if settings.LOCK_BRACKETS:
            return models.Entry.objects.filter()
        else:
            return models.Entry.objects.filter(user=self.request.user)


class EnterPicksAjaxView(LoginRequiredMixin, JsonRequestResponseMixin, DetailView):
    model = models.Entry

    def get_queryset(self):
        if settings.LOCK_BRACKETS:
            return models.Entry.objects.filter()
        else:
            return models.Entry.objects.filter(user=self.request.user)

    def get_picks(self):
        entry = self.object
        picks = entry.entrypick_set.select_related('game', 'pick')
        return [pick.as_dict() for pick in picks]

    def get(self, request, *args, **kwargs):
        super(EnterPicksAjaxView, self).get(request, *args, **kwargs)
        return self.render_json_response(self.get_picks())

    def post(self, request, *args, **kwargs):
        if settings.LOCK_BRACKETS:
            return self.render_bad_request_response({'message': ('brackets are locked.')})
        self.object = self.get_object()
        tie_break = self.request_json.get('tie_break')
        if tie_break:
            self.object.tie_break = int(tie_break)
            self.object.save()
            return self.render_json_response({'tie_break': tie_break})
        try:
            game = self.request_json['game']
            pick = self.request_json['pick']
        except KeyError:
            return self.render_bad_request_response({'message': ('must supply game and pick')})
        pick = self.object.create_pick(models.Game.objects.get(pk=game), models.Bracket.objects.get(pk=pick))
        return self.render_json_response(pick.as_dict())


class StandingsView(LoginRequiredMixin, TemplateView):
    template_name = 'brackets/standings.html'
    model = models.Entry

    def get_context_data(self, **kwargs):
        context = super(StandingsView, self).get_context_data(**kwargs)
        context['entries'] = models.Entry.objects.all().order_by('-points', '-possible', 'pk')
        context['locked'] = settings.LOCK_BRACKETS
        return context
