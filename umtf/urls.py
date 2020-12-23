from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^latest$', views.ListMostRecentTradesView.as_view(), name='latest'),
    ]
