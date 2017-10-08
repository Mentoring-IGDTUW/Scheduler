# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from .models import Person


def login_option(request):
	return render(request, 'sch/login_option.html', {})




def login_check1(request):
	uname=request.POST['username']
	pas=request.POST['password']
	user={'name' : ''}
	P=Person.objects.filter(Tid = uname, password = pas).count()
	try:
    		name=Person.objects.get(Tid = uname, password = pas)
	except Person.DoesNotExist:
    		name = None	
	
	if (P==1):
        	#user['roll'] = uname
		user['name'] = name
		return render(request,'sch/main.html', user)

	else:
		messages.error(request, 'Please try again')
		return render(request, 'sch/login1.html', {})
		

def login1(request):
	return render(request, 'sch/login1.html')

def login2(request):
	return render(request, 'sch/login2.html')

def main(request):
	return render(request, 'sch/main.html', {})
