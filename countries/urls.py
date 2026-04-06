from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("countries/", views.country_list, name="country_list"),
    path("countries/add/", views.country_create, name="country_create"),
    path("countries/<int:country_id>/edit/", views.country_edit, name="country_edit"),
    path("countries/<int:country_id>/", views.country_detail, name="country_detail"),
    path("test/", views.test_mode, name="test_mode"),
    path("test/<int:country_id>/", views.test_country, name="test_country"),
]