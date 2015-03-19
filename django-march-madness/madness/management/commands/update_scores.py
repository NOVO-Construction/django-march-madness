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
		for g in Game.objects.all():
			regexp = re.compile(r'%s (.*?) %s' % (g.team_2.team.espn_id, g.team_1.team.espn_id))
			if regexp.search(c) is not None:
				print regexp.pattern
			else:
				print "No game today"
			# win_1 = re.compile(r'%s \d+   \^%s \d+' % (g.team_2.team.espn_id, g.team_1.team.espn_id))
			# win_2 = re.compile(r'\^%s \d+   %s \d+' % (g.team_2.team.espn_id, g.team_1.team.espn_id))
			# print win_1.pattern
			# print win_2.pattern
