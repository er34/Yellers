from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect
from forms import RegistrationForm, LoginForm, AccountForm
import random
import unicodedata
from string import ascii_lowercase
import hashlib 
import time
from models import Captcha, Account
import uuid
from django.contrib.auth.models import User
from django.core.mail import send_mail
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

# from django.views.decorators.csrf import csrf_protect

def entry(request):
	if request.user.is_authenticated():
		c = { 'user': request.user, }
		return render(request, 'index.html', c)
	else:
		c = { 'form': LoginForm, }
		return render(request, 'login.html', c)
	
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
	cletters = random.choice(ascii_lowercase) + random.choice(ascii_lowercase) + random.choice(ascii_lowercase) + random.choice(ascii_lowercase)
	ckey = str(random.SystemRandom().randrange(0, 18446744073709551616L)) + str(time.time())
	key_ = unicodedata.normalize('NFKD', ckey + unicode(cletters.upper())).encode('ascii', 'ignore') + unicodedata.normalize('NFKD', unicode(cletters)).encode('ascii', 'ignore')
	key = hashlib.sha1(key_).hexdigest()
	print key
	print cletters
	cptmod = Captcha()
	cptmod.hash = key
	cptmod.code = cletters
	cptmod.save()
	c = { 'key' : key,
		'form': RegistrationForm, }
	return render(request, 'registration.html', c)

def doregister(request):
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			print 'yes'
			mailkey = uuid.uuid1().hex[0:29]
			u = User()
			userlogin =  request.POST ['login']
			u.username = mailkey
			u.last_name = request.POST ['lastname']
			u.first_name = request.POST ['firstname']
			u.email = request.POST ['email']
			u.set_password (request.POST['password'])
			u.is_superuser = 0
			u.is_active = 0
			u.is_staff = 0
			u.save()
			send_mail('Yellers email verification',
			          'To verify your email please follow the link below: http://5.19.200.78/Yellers/mailverify/'+userlogin+'/'+mailkey+
			          '\nyour login is: ' + userlogin + '\nyour password is ' + request.POST['password'],
			          'onlybox@gmail.com', [request.POST['email']], fail_silently=False)
			return HttpResponseRedirect("/Yellers/")
		else:
			print 'no'
			form = RegistrationForm
			return HttpResponseRedirect("/Yellers/registration/")
		
def mailverify(request,username,mailkey):
	try:
		fuser = User.objects.get(username=mailkey)
		fuser.username = username
		fuser.is_active = 1
		fuser.save()
		return HttpResponseRedirect("/Yellers/")
	except User.DoesNotExist:
		return HttpResponseRedirect("/Yellers/")
	
def isUserExists(request,username):
	try:
		User.objects.get(username=username)
		return HttpResponse("User "+username+" exists!")
	except:
		return HttpResponse("")

@login_required
def account(request):
	try:
		accdata = Account.objects.get(user=request.user)
	except:
		accdata = Account.objects.get(user=request.user)
	c = { 'form': AccountForm, 
		  'accdata': accdata, }
	return render(request, 'account.html', c)

			