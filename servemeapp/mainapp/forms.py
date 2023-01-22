from django import forms
from django.forms import ModelForm
from .models import Diner, Manager


class DinerLogin(ModelForm):
	class Meta:
		model = Diner
		fields = ("username", "password", "phone")
		widgets = {
            "password": forms.PasswordInput()
        }

	def save(self, commit=True):
		user = super(DinerLogin, self).save(commit=False)
		if commit:
			user.save()
		return user

class ManagerLogin(ModelForm):
	class Meta:
		model = Manager
		fields = ("username", "password", "phone", "rest_name", "branch")
		widgets = {
            "password": forms.PasswordInput()
        }
	def save(self, commit=True):
		user = super(ManagerLogin, self).save(commit=False)
		if commit:
			user.save()
		return user