from django import forms
from django.forms import ModelForm
from .models import *


class AchievementsheetForm(ModelForm):
    class Meta:
        model = AchievementsSheet
        fields = '__all__'