# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from application.forms import RegistrationForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
    	if request.user.is_authenticated():
    		return HttpResponseRedirect(reverse('home'))
    	form = self.form_class(None, request.POST or None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        # next_url = request.POST.get('next','/home/')
        if form.is_valid():
        	auth_login(self.request, form.get_user())
        	return HttpResponseRedirect('/home/')
        return render(request, self.template_name, {'form': form})


class RegisterView(TemplateView):
    template_name = "register.html"
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
    	if request.user.is_authenticated():
    		return HttpResponseRedirect(reverse('home'))
    	form = self.form_class(None, request.POST or None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
        	form.save()
        	username = form.cleaned_data.get('username')
        	raw_password = form.cleaned_data.get('password1')
        	user = authenticate(username=username, password=raw_password)
        	auth_login(request, user)
        	return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

