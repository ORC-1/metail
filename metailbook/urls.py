"""metailbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import  include
from django.conf.urls import url
from django.contrib import admin
import metailnook
from django.views import generic
from metailnook import views as mviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('metailnook.urls')),
    url(r'^measure/$', mviews.FormView.as_view(),name="form_list"),
    url(r'^measure2/$', mviews.etra_homeview.as_view(),name="form_list2"),
    # url('(?P<pk>\d+)$', mviews.indexDetailView.as_view(), name='index'),
    url(r'^signup/$', mviews.signup, name='signup'),
    url(r'^home/$', mviews.homepage, name='homepage'),
    url(r'^account/$', mviews.account_profile_form, name='account'),
    url(r'^customer/$', mviews.customer_form, name='customer'),
    url(r'^blouse/$', mviews.blouse_form, name='blouse'),
    url(r'^skirt/$', mviews.skirt_form, name='skirt'),
    url(r'^blouse/$', mviews.blouse_form, name='blouse'),
    url(r'^skirt/$', mviews.skirt_form, name='skirt'),
    url(r'^sokoto/$', mviews.sokoto_form, name='sokoto'),
    url(r'^gown/$', mviews.gown_form, name='gown'),
    url(r'^caftan/$', mviews.caftan_form, name='caftan'),
    url(r'^shirt/$', mviews.shirt_form, name='shirt'),
    url(r'^buba/$', mviews.buba_form, name='buba'),
    url(r'^suit/$', mviews.suit_form, name='suit'),
    url(r'^trouser/$', mviews.trouser_form, name='trouser'),
    url(r'^payment/$', mviews.payment_form, name='payment'),

]
