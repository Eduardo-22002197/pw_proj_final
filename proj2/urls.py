from django.urls import path
from . import views
import proj2


app_name = 'proj2'

urlpatterns = [
    path('', views.home_page_view, name = "home"),
    path('history', views.history_page_view, name = 'history'),
    path('location', views.location_page_view, name = 'location'),
    path('contact', views.contact_page_view, name = 'contact'),
    path('about', views.about_page_view, name = 'about')
]
