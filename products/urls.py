from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^$',
    RedirectView.as_view(
	pattern_name='sanitary_ware',
	permanent=False),
    name='home'),
    url(r'^sanitary_ware/$', views.sanitary_ware, name='sanitary_ware'),
    url(r'^acrylic_bathtubs/$', views.acrylic_bathtubs, name='acrylic_bathtubs'),
    url(r'^water_taps/$', views.water_taps, name='water_taps'),
    url(r'^additional_items/$', views.additional_items, name='additional_items'),
]
