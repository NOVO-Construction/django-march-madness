# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser

# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username
