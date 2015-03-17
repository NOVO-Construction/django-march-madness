from django.core.urlresolvers import reverse_lazy
from django.db import models
from model_utils.models import TimeStampedModel

from users.models import User


class Region(models.Model):
    name = models.CharField(max_length=50, blank=False)
    grid = models.IntegerField(max_length=1, blank=False)

    def __unicode__(self):
        return u'%s' % (self.name)


class ScoreLink(models.Model):
    espn = models.IntegerField(max_length=11)
    cbs = models.IntegerField(max_length=11)
    ncaa = models.IntegerField(max_length=11)


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False)
    mascot = models.CharField(max_length=100, blank=False)
    abbreviation = models.CharField(max_length=4, blank=False)
    score_link = models.ForeignKey(ScoreLink, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.mascot)


class Bracket(models.Model):
    year = models.IntegerField(max_length=4, blank=False, default=2015)
    team = models.ForeignKey(Team)
    region = models.ForeignKey(Region)
    seed = models.IntegerField(max_length=2, blank=False)

    def __unicode__(self):
        return u'(%s) %s' % (self.seed, self.team.name)


class Game(models.Model):
    game_number = models.IntegerField(db_index=True)
    team_1 = models.ForeignKey(Bracket, related_name='+', null=True, blank=True)
    team_2 = models.ForeignKey(Bracket, related_name='+', null=True, blank=True)
    team_1_score = models.IntegerField(max_length=4, default=0)
    team_2_score = models.IntegerField(max_length=4, default=0)

    def __unicode__(self):
        return u'%s - %s vs %s' % (self.game_number, self.team_1, self.team_2)


class Entry(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=250, blank=False)
    tie_break = models.IntegerField(max_length=3, blank=False)

    def create_pick(self, game, pick):
        obj, created = EntryPick.objects.update_or_create(entry=self, game=game, defaults={'pick': pick})
        return obj

    def get_absolute_url(self):
        return reverse_lazy('madness:entry_picks', args=(self.pk,))


class EntryPick(TimeStampedModel):
    entry = models.ForeignKey(Entry)
    game = models.ForeignKey(Game)
    pick = models.ForeignKey(Bracket)

    def as_dict(self):
        return {
            'pk': self.pk,
            'game_pk': self.game.pk,
            'game_number': self.game.game_number,
            'pick_pk': self.pick.pk,
            'pick_team_pk': self.pick.team.pk,
            'pick_team_name': self.pick.team.name,
            'pick_team_mascot': self.pick.team.mascot,
            'pick_team_abbreviation': self.pick.team.abbreviation,
            'pick_team_seed': self.pick.seed,
            'pick_team_display': '({}) {}'.format(self.pick.seed, self.pick.team.name),
        }


class Standing(models.Model):
    # standings to be recalulated when scores are updated
    entry = models.ForeignKey(Entry)
    position = models.IntegerField(blank=False)
    prev_position = models.IntegerField(blank=True)
    points = models.IntegerField(default=0)


class Result(models.Model):
    game = models.ForeignKey(Game)
    winner = models.ForeignKey(Bracket)
