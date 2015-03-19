from django.conf import settings


def lock_brackets(request):
    return {'LOCK_BRACKETS': settings.LOCK_BRACKETS}
