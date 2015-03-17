# -*- coding: utf-8 -*-
from crispy_forms.helper import FormHelper
from django import forms

from . import models


class EntryForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = models.Entry
        fields = ('name',)
