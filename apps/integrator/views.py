from django.shortcuts import render
from django.contrib.auth import forms, login, authenticate, logout
from django.views.generic import View
from .forms import UserFormRegistration, messageForm, commentForm



class login(View):
	#this goes to our django,contib,auth and retreives pre built form
	form = forms.AuthenticationForm

	def get(self, request):
		context = {"login_form":self.form(),}
	
		return render(request, 'integrator/login.html', context)
	def post(self, request):
		print request.POST
		print self.form(request.POST).is_valid()
		context = {"login_form":self.form(),}

		return render(request, 'integrator/login.html', context)

class register(View):
	#this goes to our django,contib,auth and retreives pre built form
	form = UserFormRegistration

	def get(self, request):
		context = {"registration_form":self.form(),}
	
		return render(request, 'integrator/registration.html', context)
	def post(self, request):
		registration = self.form(request.POST)
		if registration.is_valid():
			user = registration.save()
			# request.session['user'] = {'username' : user['username']}
		else:


			context = {"login_form":self.form(request.POST or None),}
			return render(request, 'integrator/registration.html')

		return render(request, 'integrator/wall.html')
