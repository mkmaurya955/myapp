from __future__ import unicode_literals
from django.shortcuts import render,redirect

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.generic import View

import random
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import Q

from django.shortcuts import render

import datetime

def index(request):
	myDate = datetime.datetime.now().date()
	myTime= datetime.datetime.now().time()
	return render(request, 'welcome.html', {'date': myDate,'time':myTime})
    

def registration(request):
	if request.method=='POST':
		form1=userform(request.POST)
		if form1.is_valid():
			username1=form1.cleaned_data['username']
			first_name1=form1.cleaned_data['first_name']
			last_name1=form1.cleaned_data['last_name']
			password1=form1.cleaned_data['password']
			email1=form1.cleaned_data['email']
			User.objects.create_user(username=username1,first_name=first_name1,last_name=last_name1,password=password1,email=email1)
			messages.success(request,'User registration successfully')
			#usr=auth.authenticate(username=username,password=password)
			#auth.login(request,usr)
			#return render(request,'welcome.html')
			return HttpResponseRedirect('/registration/')
	else:
		form1=userform()
	return render(request,'registration.html',{'frm':form1})




def login(request):
	if request.method=='POST':
		username=request.POST['user']
		password=request.POST['pas']
		try:
			user=auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request,user)
				return render(request,'welcome.html')
			else:
				messages.error(request,'Username and password did not matched')


		except auth.ObjectNotExist:
			print("Invalid user")
	return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return render(request,'logout.html')


def useraccount(request):
	return render(request,'useraccount.html')

def report(request):
	myDate = datetime.datetime.now().date()
	myTime= datetime.datetime.now().time()
	obj=TempHumdity.objects.all()
	return render(request,'report.html',{'obj1':obj,'date': myDate,'time':myTime})

def calibration(request):
	if request.method=='POST':
		form1=View_Report_Form(request.POST)
		if form1.is_valid():
			temp1=form1.cleaned_data['temperature']
			hmdt=form1.cleaned_data['humidity']
			form1.save()
			return HttpResponseRedirect('/calibration/')
	else:
		form1=View_Report_Form()

	return render(request,'calibration.html',{'form':form1})

		

def user(request):
	myTime= datetime.datetime.now().time()
	return render(request,'user.html',{'time':myTime})

def submit(request):
	return render(request,'submit.html')

# charts view.py
User=get_user_model()




	


#class HomeView(View):
 #   def get(self,request,*args,**kwargs):
  #  	obj=TempHumdity.objects.all()
   # 	return render(request,'charts.html',{'obj1':obj,})

    

#def get_data(request,*args,**kwargs):
#
 #   data={}
  #  return JsonResponse(data)


#class ChartData(APIView):
 #   authentication_classes = []
  ##
    #def get(self, request, format=None):
    #	obj=TempHumdity.objects.all().count()
    #	labels=["0", "2", "4", "6", "8", "10","12","14","16","18"]
    #	default_items=[]
    #	for items in range(10):
    #		t=random.randint(0,50)
    ##	data={"labels":labels,"obj1":default_items,}
    #	return Response(data)
    #	return render(request,'charts.html',{'obj1':obj,})
 