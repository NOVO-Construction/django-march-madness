# -*- coding: utf-8 -*-
from django import forms

from .models import Entry


class EntryForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = Entry

        # Constrain the UserForm to just these fields.
        fields = ("name",)
