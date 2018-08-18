# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def loginView(request):
	if request.method == 'POST':#when user clicks the submit button
		uname = request.POST['username']
    		password= request.POST['password']
    		user = authenticate(username=uname, password=password)#checks if username and password is correct
		if user is not None:#if user is correct
			if user.is_active:
		    		login(request, user)#login the user
			else:
		    		return HttpResponse('disabled account')
		return HttpResponseRedirect(request.path)#refresh page
	form = LoginForm()
	return render_to_response('reg/login.html', {'form':form,'logged_in':request.user.is_authenticated()})

@csrf_exempt
def logoutView(request):
	logout(request)
	return render_to_response('reg/logout.html')


