from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success/(?P<user_id>\d+)$', views.success),
    url(r'^login$', views.login),
    url(r'^clear$', views.clear),
    url(r'^wall/(?P<user_id>\d+)$', views.wall),
    url(r'^comment/(?P<user_id>\d+)/(?P<message_id>\d+)$', views.comment),

]