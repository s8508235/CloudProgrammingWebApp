from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	url(r'^$',views.home,name='home'),
    url(r'^accounts/profile/$',views.post_list,name='post_list'),
    url(r'^signin/$',auth_views.login, {'template_name': 'blog/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
