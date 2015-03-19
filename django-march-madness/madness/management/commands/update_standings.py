import logging

from django.core.management.base import NoArgsCommand

from madness.models import Entry, Game

log = logging.getLogger(__name__)


class Command(NoArgsCommand):
    help = "Update Madness standings"

    def handle_noargs(self, **options):
        for e in Entry.objects.all():
            # calculate points
            p = 0
            #round - 1
            for rd1 in e.entrypick_set.filter(game__lte=32):
                result = Game.objects.get(game_number=rd1.game_id)
                if result.winner == rd1.pick:
                    p = p + 1

            #round - 2
            for rd2 in e.entrypick_set.filter(game__gte=33, game__lte=48):
                result = Game.objects.get(game_number=rd2.game_id)
                if result.winner == rd2.pick:
                    p = p + 2

            #round - 3
            for rd3 in e.entrypick_set.filter(game__gte=49, game__lte=56):
                result = Game.objects.get(game_number=rd3.game_id)
                if result.winner == rd3.pick:
                    p = p + 4

            #round - 4
            for rd4 in e.entrypick_set.filter(game__gte=57, game__lte=60):
                result = Game.objects.get(game_number=rd4.game_id)
                if result.winner == rd4.pick:
                    p = p + 8

            #round - 5
            for rd5 in e.entrypick_set.filter(game__gte=61, game__lte=62):
                result = Game.objects.get(game_number=rd5.game_id)
                if result.winner == rd5.pick:
                    p = p + 16

            #round - 6
            for rd6 in e.entrypick_set.filter(game=63):
                result = Game.objects.get(game_number=rd6.game_id)
                if result.winner == rd6.pick:
                    p = p + 32

            e.points = p
            e.save()
