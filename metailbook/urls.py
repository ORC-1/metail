
from django.conf.urls import  include
from django.conf.urls import url
from django.contrib import admin
import metailnook
from django.views import generic
from metailnook import views as mviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^metail/$', include('metailnook.urls')),
    url(r'^measure/$', mviews.FormView.as_view(),name="form_list"),
    # url('(?P<pk>\d+)$', mviews.indexDetailView.as_view(), name='index'),
    url('', mviews.SignIn, name='SignIn'),
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
