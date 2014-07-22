from django.shortcuts import render_to_response

def entry(request):
	if request.user.is_authenticated():
		return render_to_response('index.html')
	else:
		return render_to_response('login.html')
