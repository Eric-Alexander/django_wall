from django import forms
from django.contrib.auth.models import User
#get all the models copy past from model INTEGRATOR
# from apps.get_app_config('comments') import Comment
# from apps.get_app_config('posts') import Message
from django.contrib.auth.forms import UserCreationForm
#make form for the wall user
from .models import Wall_User, Wall_Comment, Wall_Message

#use user registration and login in the same class
class UserFormRegistration(UserCreationForm):
	#password and Cpassword from UserCreationForm
	#first name last name email username from here
	#DOB from Wall_User

	first_name = forms.CharField (label = "First Name")
	last_name = forms.CharField (label = "Last Name")
	email = forms.EmailField (label = "Email")
	username = forms.CharField (label = "Username")

	#brings over a model and populates it here
	class Meta:
		model = Wall_User
		fields = ('first_name','last_name','email','DOB',)
	def save(self, commit = True):
		user = super(UserFormRegistration,self).save(commit = False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		user.set_password = (self.cleaned_data['password1'])
		if commit:
			user.save()
			return user

class messageForm(forms.ModelForm):
	class Meta:
		model = Wall_Message
		fields = ('message',)

class commentForm(forms.ModelForm):
	class Meta:
		model = Wall_Comment
		fields = ('comment',)

# class normalForm(forms.form):
# 	# by default will creeate a <th><td> with username as an input field no need for
# 	#blah = forms.charfield(max_length = 3)
