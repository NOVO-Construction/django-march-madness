import logging

from django.core.management.base import NoArgsCommand

from madness.models import Entry, Bracket

log = logging.getLogger(__name__)


class Command(NoArgsCommand):
    help = "Update Madness possible points"

    def handle_noargs(self, **options):
        elim = Bracket.objects.filter(is_eliminated=True).values_list('id', flat=True)
        for e in Entry.objects.all():
            # calculate points
            p = 0
            #round - 1
            for rd1 in e.entrypick_set.filter(game__lte=32, game__winner__isnull=True):
                if rd1.pick_id not in elim:
                    p = p + 1

            #round - 2
            for rd2 in e.entrypick_set.filter(game__gte=17, game__lte=38, game__winner__isnull=True):
                if rd2.pick_id not in elim:
                    p = p + 2

            #round - 3
            for rd3 in e.entrypick_set.filter(game__gte=49, game__lte=56, game__winner__isnull=True):
                if rd3.pick_id not in elim:
                    p = p + 4

            #round - 4
            for rd4 in e.entrypick_set.filter(game__gte=57, game__lte=60, game__winner__isnull=True):
                if rd4.pick_id not in elim:
                    p = p + 8

            #round - 5
            for rd5 in e.entrypick_set.filter(game__gte=61, game__lte=62, game__winner__isnull=True):
                if rd5.pick_id not in elim:
                    p = p + 16

            #round - 6
            for rd6 in e.entrypick_set.filter(game=63, game__winner__isnull=True):
                if rd6.pick_id not in elim:
                    p = p + 32

            e.possible = p
            e.save()
