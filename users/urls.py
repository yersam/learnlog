from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns=[
    url(r'^$',LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^register/$',views.register,name='register'),
]