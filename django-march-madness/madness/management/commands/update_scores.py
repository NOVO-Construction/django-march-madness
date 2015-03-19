import logging

from django.core.management.base import NoArgsCommand

from madness.models import Game

import re
import requests
import urllib

log = logging.getLogger(__name__)


class Command(NoArgsCommand):
	help = "Update Madness scores"

	def handle_noargs(self, **options):
		url = 'http://sports.espn.go.com/ncb/bottomline/scores'
		r = requests.get(url)
		c = urllib.unquote(r.text).decode(r.encoding)
		for g in Game.objects.all():
			win_1 = re.compile(r'%s \d+   \^%s \d+' % (g.team_2.team.espn_id, g.team_1.team.espn_id))
			win_2 = re.compile(r'\^%s \d+   %s \d+' % (g.team_2.team.espn_id, g.team_1.team.espn_id))
			print win_1.pattern
			print win_2.pattern