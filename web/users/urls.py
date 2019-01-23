from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'redirect_demo/$',views.redirect_demo),
    url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),

]
