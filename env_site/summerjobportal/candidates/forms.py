from django import forms
from .models import Profile, Skill
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'country', 'location',
                  'resume', 'grad_year', 'looking_for']


class NewSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']
