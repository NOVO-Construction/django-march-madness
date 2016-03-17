from django.core.urlresolvers import reverse_lazy
from django.db import models
from model_utils.models import TimeStampedModel

from users.models import User


class Region(models.Model):
    name = models.CharField(max_length=50, blank=False)
    grid = models.IntegerField(max_length=1, blank=False)

    def __unicode__(self):
        return u'%s' % (self.name)


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False)
    mascot = models.CharField(max_length=100, blank=False)
    abbreviation = models.CharField(max_length=4, blank=False)
    espn_id = models.CharField(max_length=100, blank=True, null=True)

    def as_dict(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'mascot': self.mascot,
            'abbreviation': self.abbreviation,
            'espn_id': self.espn_id,
        }

    def __unicode__(self):
        return u'%s %s' % (self.name, self.mascot)


class Bracket(models.Model):
    year = models.IntegerField(max_length=4, blank=False, default=2016)
    team = models.ForeignKey(Team)
    region = models.ForeignKey(Region)
    seed = models.IntegerField(max_length=2, blank=False)
    is_eliminated = models.BooleanField(default=False)

    def as_dict(self):
        dict = {
            'pk': self.pk,
            'year': self.year,
            'team': None,
            'region': self.region.name,
            'seed': self.seed,
            'is_eliminated': self.is_eliminated,
        }
        if self.team:
            dict['team'] = self.team.as_dict()
        return dict

    def __unicode__(self):
        return u'(%s) %s' % (self.seed, self.team.name)


class Game(models.Model):
    game_number = models.IntegerField(db_index=True)
    team_1 = models.ForeignKey(Bracket, related_name='+', null=True, blank=True)
    team_2 = models.ForeignKey(Bracket, related_name='+', null=True, blank=True)
    team_1_score = models.IntegerField(max_length=4, default=0)
    team_2_score = models.IntegerField(max_length=4, default=0)
    winner = models.ForeignKey(Bracket, related_name='+', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.team_1_score > self.team_2_score:
            self.winner = self.team_1
        elif self.team_2_score > self.team_1_score:
            self.winner = self.team_2
        super(Game, self).save(*args, **kwargs)

    def as_dict(self):
        dict = {
            'pk': self.pk,
            'game_number': self.game_number,
            'team_1': None,
            'team_2': None,
            'winner': None,
            'loser': None,
        }
        if self.team_1:
            dict['team_1'] = self.team_1.as_dict()
        if self.team_2:
            dict['team_2'] = self.team_2.as_dict()
        if self.winner:
            dict['winner'] = self.winner.as_dict()
        if self.winner:
            if self.team_1 == self.winner and self.team_2:
                dict['loser'] = self.team_2.as_dict()
            if self.team_2 == self.winner and self.team_1:
                dict['loser'] = self.team_1.as_dict()
        return dict

    def __unicode__(self):
        return u'%s - %s vs %s' % (self.game_number, self.team_1, self.team_2)


class Entry(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=250, blank=False)
    tie_break = models.IntegerField(max_length=3, blank=False)
    points = models.IntegerField(default=0)
    possible = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    prev_position = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)

    def create_pick(self, game, pick):
        old_pick = EntryPick.objects.filter(entry=self, game=game).first()
        if old_pick and old_pick.pick and old_pick.pick != pick:
            EntryPick.objects.filter(entry=self, game__game_number__gt=game.game_number, pick=old_pick.pick).delete()
        obj, created = EntryPick.objects.update_or_create(entry=self, game=game, defaults={'pick': pick})
        return obj

    @property
    def champion(self):
        c = self.entrypick_set.get(game=63)
        return c.pick

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
