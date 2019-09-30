from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^show/(?P<get_id>\d+)$', views.show),
    url(r'^show/add$', views.new),
    url(r'^show/new$', views.addpage),
    url(r'^show/(?P<get_id>\d+)/edit$', views.edit),
    url(r'^new/(?P<get_id>\d+)$', views.update),
    url(r'^delete/(?P<get_id>\d+)$', views.delete),

]