from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book

class OurForm(UserCreationForm):
	email= forms.EmailField(required=True)

	class Meta:
		model = User
		fields=('username','email','password1','password2')

	def save(self, commit=True):
		user=super(OurForm,self).save(commit=False0)
		user.email=self.cleaned_data['email']
		if commit:
			user.save()
		return user

class OurForm(forms.ModelForm):
	class Meta:
		model = Book 
		fields = ('title', 'name', 'pdf')