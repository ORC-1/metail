# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic 
from django.views.generic import ListView
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout #Import for processing Login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class FormView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = '/home'
    context_object_name = 'form_list'    
    template_name = 'metails/forms.html'
    queryset  = customer.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        customers = self.request.GET.get('option') 
        context['blouse'] = blouse.objects.filter(name = customers)
        context['Homeurl'] = navbar_link.objects.all()
        context['Bis'] = account_profile.objects.all()
        context['namec'] = customer.objects.filter(id = customers)
        context['skirt'] = skirt.objects.filter(name = customers)
        context['sokoto'] = sokoto.objects.filter(name = customers)
        context['gown'] = gown.objects.filter(name = customers)
        context['caftan'] = caftan.objects.filter(name = customers)
        context['shirt'] = shirt.objects.filter(name = customers)
        context['buba'] = buba.objects.filter(name = customers)
        context['suit'] = suit.objects.filter(name = customers)
        context['trouser'] = trouser.objects.filter(name = customers)
        context['payment'] = payment.objects.filter(name = customers)
       
        return context




@login_required
def homepage(request):

    url = navbar_link.objects.all()
    Bis = account_profile.objects.all()



    context={
    "Homeurl":url,
    "Bis":Bis
    }

    return render(request, 'metails/home.html', context)


##################################################VIEW_FOR_PROCESSING_SIGN_FORM##########################################################

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'metails/signup.html', {'form': form})
################################################## ENDVIEW_FOR_PROCESSING_SIGNUP_FORM##########################################################



##################################################VIEW_FOR_PROCESSING_SIGNIN_FORM##########################################################

def SignIn(request):
    if request.POST:
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')

            else:
                return render(request, 'metails/login.html', {'form': form})


    else:
        form = SigninForm()
        return render(request, 'metails/login.html', {'form': form})


##################################################VIEW_FOR_PROCESSING_SIGNIN_FORM##########################################################


#########################END OF VIEW FOR PROCESSING LOGIN (error 22-01-2018)###################################

##########################Django assisted logout function################################################
def logout(request):
    logout(request)
    return render(request, 'metails/Logout.html')
##########################END OF Django assisted logout function################################################

#####################################FORMS_FOR_account_profile########################################################

###blouse_form############
@login_required
def account_profile_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    if request.POST:
        form= account_profileForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/account_profileForm.html', {'form':form,"Homeurl":url,"Bis":Bis})
    else:
        form= account_profileForm()
        return render(request,'metails/account_profileForm.html', {'form':form,"Homeurl":url,"Bis":Bis})
#####################################END_FORMS_FOR_account_profile########################################################
#####################################FORMS_FOR_customer########################################################

###blouse_form############
@login_required
def customer_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    if request.POST:
        form= customerForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/customerForm.html', {'form':form,"Homeurl":url,"Bis":Bis})
    else:
        form= customerForm()
        return render(request,'metails/customerForm.html', {'form':form,"Homeurl":url,"Bis":Bis})
#####################################END_FORMS_FOR_customer########################################################

#####################################FORMS_FOR_MEASURES########################################################

###blouse_form############
@login_required
def blouse_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    blousex= customer.objects.all()
    if request.POST:
        form= blouseForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/blouseForm.html', {'form':form,'blousex':blousex,"Homeurl":url,"Bis":Bis})
    else:
        form= blouseForm()
        return render(request,'metails/blouseForm.html', {'form':form, 'blousex':blousex,"Homeurl":url,"Bis":Bis})
#####################################END_FORMS_FOR_blouse########################################################

###skirt_form############
@login_required
def skirt_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    skirtx = customer.objects.all()
    if request.POST:
        form= skirtForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/skirtForm.html', {'form':form,"skirtx":skirtx,"Homeurl":url,"Bis":Bis})
    else:
        form= blouseForm()
        return render(request,'metails/skirtForm.html', {'form':form,"skirtx":skirtx,"Homeurl":url,"Bis":Bis})


#####################################END_FORMS_FOR_Skirt########################################################
###sokoto_form############
@login_required
def sokoto_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    sokotox= customer.objects.all()
    if request.POST:
        form= sokotoForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/sokotoForm.html', {'form':form,"sokotox":sokotox,"Homeurl":url,"Bis":Bis})
    else:
        form= sokotoForm()
        return render(request,'metails/sokotoForm.html', {'form':form,"sokotox":sokotox,"Homeurl":url,"Bis":Bis})


#####################################END_FORMS_FOR_sokoto########################################################
###gown_form############
@login_required
def gown_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    gownx= customer.objects.all()
    if request.POST:
        form= gownForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/gownForm.html', {'form':form,'gownx':gownx,"Homeurl":url,"Bis":Bis})
    else:
        form= gownForm()
        return render(request,'metails/gownForm.html', {'form':form, 'gownx':gownx,"Homeurl":url,"Bis":Bis})


#####################################END_FORMS_FOR_gown########################################################
###caftan_form############
@login_required
def caftan_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    caftanx= customer.objects.all()
    if request.POST:
        form= caftanForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/caftanForm.html', {'form':form, 'caftanx':caftanx,"Homeurl":url,"Bis":Bis})
    else:
        form= caftanForm()
        return render(request,'metails/caftanForm.html', {'form':form, 'caftanx':caftanx,"Homeurl":url,"Bis":Bis})


#####################################END_FORMS_FOR_caftan########################################################
###shirt_form############
@login_required
def shirt_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    shirtx= customer.objects.all()
    if request.POST:
        form= shirtForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/shirtForm.html', {'form':form, 'shirtx':shirtx,"Homeurl":url,"Bis":Bis})
    else:
        form= shirtForm()
        return render(request,'metails/shirtForm.html', {'form':form, 'shirtx':shirtx, "Homeurl":url,"Bis":Bis})


#####################################END_FORMS_FOR_shirt########################################################
###buba_form############
@login_required
def buba_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    bubax= customer.objects.all()
    if request.POST:
        form= bubaForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/bubaForm.html', {'form':form, 'bubax':bubax,"Homeurl":url,"Bis":Bis})
    else:
        form= bubaForm()
        return render(request,'metails/bubaForm.html', {'form':form, 'bubax':bubax, "Homeurl":url,"Bis":Bis})


#####################################END_FORMS_FOR_########################################################
###suit_form############
@login_required
def suit_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    suitx = customer.objects.all()

    if request.POST:
        form= suitForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/suitForm.html', {'form':form,"suitx":suitx,"Homeurl":url,"Bis":Bis})
    else:
        form= suitForm()
        return render(request,'metails/suitForm.html', {'form':form,"suitx":suitx,"Homeurl":url,"Bis":Bis})


#####################################END_FORMS_FOR_suit########################################################
###trouser_form############
@login_required
def trouser_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()
    trouserx = customer.objects.all()

    if request.POST:
        form= trouserForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/trouserForm.html', {'form':form,"trouserx":trouserx, "Homeurl":url,"Bis":Bis})
    else:
        form= trouserForm()
        return render(request,'metails/trouserForm.html', {'form':form,"trouserx":trouserx, "Homeurl":url,"Bis":Bis})


#####################################END_FORMS_FOR_trouser########################################################
@login_required
def payment_form(request):
    Bis = account_profile.objects.all()
    url = navbar_link.objects.all()

    if request.POST:
        form= paymentForm(request.POST)
        if form.is_valid():            
            form.save()            
            return render(request,'metails/thanks.html')
        else:
            return render(request,'metails/paymentForm.html', {'form':form,"Homeurl":url,"Bis":Bis})
    else:
        form= paymentForm()
        return render(request,'metails/paymentForm.html', {'form':form,"Homeurl":url,"Bis":Bis})


#####################################END_FORMS_FOR_payment########################################################
#####################################END_FORMS_FOR_MEASURES########################################################
