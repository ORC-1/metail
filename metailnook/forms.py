from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout #Import for processing Login







# class signupform(UserCreationForm):
#     position = forms.CharField(max_length=100, label="position", help_text='Required. Official company post')
#     phone = forms.IntegerField(label="Phone")
#     Birthday = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
#     email = forms.EmailField(label="Email")
#     class Meta:
#         model = User
#         fields = ('username', 'position', 'phone', 'Birthday', 'email', 'password1', 'password2',)


##################################################SIGNIN_FORM##########################################################

class SigninForm(forms.Form):
    username = forms.CharField(max_length=100,label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(SigninForm,self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not User(username=username, password=password):
            raise forms.ValidationError("Wrong login or password")
        return self.cleaned_data


##################################################END_OF_CONNECTION FORM##########################################################

##################################################SELECT_FORM#####################################################
# class selCustomer(forms.Form):
# 	option = forms.CharField(max_length=100, label="option")
# 	def clean(self):
# 		cleaned_data = super(selCustomer, self).clean()
# 		option = self.cleaned_data.get('option')
# 		return self.cleaned_data
##################################################SELECT_FORM#####################################################
	##############################account_profile_FORM###########################################
class account_profileForm(forms.ModelForm):
	class Meta:
		model = account_profile

		fields = ('name','position','phone','Birthday','email',)

	##############################END_account_profile_FORM###########################################
	##############################customer_FORM###########################################
class customerForm(forms.ModelForm):
	class Meta:
		model = customer

		fields = ('name','lastname','address','collectiondate',)

	##############################END_customer_FORM###########################################

##############################BLOUSE_FORM###########################################
class blouseForm(forms.ModelForm):
	class Meta:
		model = blouse

		fields = ('name','length','bust','shoulder','waist','neck','halflength','Quaterlength','hip','sleeve','Rsleeve',)

	##############################END_BLOUSE_FORM###########################################

	##############################skirt_FORM###########################################
class skirtForm(forms.ModelForm):
	class Meta:
		model = skirt

		fields = ('name','length','halflength','waist',)

	##############################END_skirt_FORM###########################################


	##############################sokoto_FORM###########################################
class sokotoForm(forms.ModelForm):
	class Meta:
		model = sokoto

		fields = ('name','length','halflength','bottom',)

	##############################END_sokoto_FORM###########################################
	##############################gown_FORM###########################################
class gownForm(forms.ModelForm):
	class Meta:
		model = gown

		fields = ('name','length','bust','underburst','shoulder','waist','halflength','Quaterlength','hip','sleeve','Rsleeve',)

	##############################END_gown_FORM###########################################
	##############################caftan_FORM###########################################
class caftanForm(forms.ModelForm):
	class Meta:
		model = caftan

		fields = ('name','length','underburst','neck','pocketline','shoulder','bust','Quaterlength','sleeve','Rsleeve',)

	##############################END_caftan_FORM###########################################	##############################shirt_FORM###########################################
class shirtForm(forms.ModelForm):
	class Meta:
		model = shirt

		fields = ('name','length','collar','neck','chest','shoulder','back','sleeve','Rsleeve','waist',)

	##############################END_shirt_FORM###########################################
	##############################buba_FORM###########################################
class bubaForm(forms.ModelForm):
	class Meta:
		model = buba

		fields = ('name','length','neck','shoulder','sleeve','Rsleeve',)

	##############################END_buba_FORM###########################################
	##############################suit_FORM###########################################
class suitForm(forms.ModelForm):
	class Meta:
		model = suit 

		fields = ('name','length','neck','shoulder','armhole','sleeve','Rsleeve','waist',)

	##############################END_suit_FORM###########################################
	##############################trouser_FORM###########################################
class trouserForm(forms.ModelForm):
	class Meta:
		model = trouser

		fields = ('name','length','waist','tight','roundkneel','flap','hip','rSit','bottom',)

	##############################END_trouser_FORM###########################################
	##############################payment_FORM###########################################
class paymentForm(forms.ModelForm):
	class Meta:
		model = payment

		fields = ('name','bill','advance',)

	##############################END_payment_FORM###########################################


