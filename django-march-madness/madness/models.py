from django.db import models
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
    team_1 = models.ForeignKey(Bracket, related_name='+')
    team_2 = models.ForeignKey(Bracket, related_name='+')
    team_1_score = models.IntegerField(max_length=4, blank=True)
    team_2_score = models.IntegerField(max_length=4, blank=True)


class Entry(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=250, blank=False)
    tie_break = models.IntegerField(max_length=3, blank=False)


class EntryPick(models.Model):
    entry = models.ForeignKey(Entry)
    game = models.ForeignKey(Game)
    pick = models.ForeignKey(Team)


class Standing(models.Model):
    # standings to be recalulated when scores are updated
    entry = models.ForeignKey(Entry)
    position = models.IntegerField(blank=False)
    prev_position = models.IntegerField(blank=True)
    points = models.IntegerField(default=0)


class Result(models.Model):
    game = models.ForeignKey(Game)
    winner = models.ForeignKey(Bracket)
