from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from forms import RegistrationForm
# from django.views.decorators.csrf import csrf_protect

def entry(request):
	if request.user.is_authenticated():
		c = { 'user': request.user}
		return render(request, 'index.html', c)
	else:
		return render(request, 'login.html')
	
def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['login'], password=request.POST['password'])
		if user is not None and user.is_active:
			auth.login(request,user)
		return HttpResponseRedirect("/Yellers/")
	
def logout(request):
	if request.method == 'POST' and request.user.is_authenticated():
			auth.logout(request)
			return HttpResponseRedirect("/Yellers/")
		
def registration(request):
	c = { 'RegistrationForm': RegistrationForm}
	return render(request, 'registration.html', c)