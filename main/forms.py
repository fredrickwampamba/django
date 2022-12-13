from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField()
	username = forms.TextInput()
	password1 = forms.PasswordInput()
	password2 = forms.PasswordInput()

	class Meta:
		model = User
		fields = ("username", "password1", "password2", "email")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user