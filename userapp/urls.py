from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /polls/
    #url(r'^$', views.index, name='dashboard'),
    url(r'^index/$', views.dashboard.as_view(), name='dashboard'),
    url(r'^register$', views.register, name='register'),
    url(r'^authors/$', views.NewView.as_view(), name='author-list'),
    #url(r'^login$', 'accounts.views.login', name='login'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^latestlogin/$', views.NewUserList.as_view(), name='login_drf'),
    #url(r'^userapp/login/$', auth_views.login),
    #url(r'^index/$', views.index, name='index'),

    #url(r'^display/$', views.display, name='display'),
    url(r'^display/$', views.DisplayUserList.as_view(), name='display'),
    # ex: /polls/5/
    url(r'^age/$', views.country, name='age'),
    url(r'^([0-9]+)/detail/$', views.detail, name='detail'),
#    url(r'^post/new/$', views.post_new, name='post_new'),
#    url(r'^post/new/$', views.NewUserListAng.as_view(), name='post_new')
    #url(r'^post/new/$', views.NewUserDetailsListAng.as_view(), name='post_new')
    url(r'^post/new/$', views.NewUserClass.as_view(), name='post_new')

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)