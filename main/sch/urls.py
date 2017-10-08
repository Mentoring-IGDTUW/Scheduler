from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login_option, name='login'),
	url(r'^login1/$', views.login1),
	url(r'^login2/$', views.login2),
	url(r'^login/$', views.login_check1),
	url(r'main/', views.main, name='main'),
]