from django.urls import path
from . import views, admin_views


urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('about', views.about, name='about'),
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited/', views.place_was_visited, name='place_was_visited'),
    path('place/<int:place_pk>', views.place_details, name='place_details'),
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place'),
    path('catfact', admin_views.get_cat_fact, name='admin_get_cat_fact'),
]