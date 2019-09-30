from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout/(?P<order_id>\d+)$', views.checkout),
    url(r'^place_order$', views.order)
]