import logging
import re
import urllib

import requests
from django.core.management.base import NoArgsCommand

from madness.models import Game

log = logging.getLogger(__name__)


class Command(NoArgsCommand):
	help = "Update Madness scores"

	def handle_noargs(self, **options):
		url = 'http://sports.espn.go.com/ncb/bottomline/scores'
		r = requests.get(url)
		c = urllib.unquote(r.text).decode(r.encoding)
		games = Game.objects.filter(winner__isnull=True, team_1__isnull=False, team_2__isnull=False)
		for g in games:
			team_1 = re.escape(g.team_1.team.espn_id)
			team_2 = re.escape(g.team_2.team.espn_id)
			win_1 = re.compile(r'%s \d+\s+\^%s \d+' % (team_2, team_1))
			win_2 = re.compile(r'\^%s \d+\s+%s \d+' % (team_2, team_1))
			if win_1.search(c) is not None:
				g.winner = g.team_1
				g.save()
				g.team_2.is_eliminated = True
				g.team_2.save()
			elif win_2.search(c) is not None:
				g.winner = g.team_2
				g.save()
				g.team_1.is_eliminated = True
				g.team_1.save()
			else:
				pass
