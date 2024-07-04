from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/<str:id>/', views.profile, name='profile'),
    path('illustrations/', views.illustration_list, name='illustration_list'),
    path('collections/', views.collection_list, name='collection_list'),
    path('collection/<str:id>/', views.collection_details, name='collection_detail'),
    path('login/', views.login_page, name='login'),
    path('add/', views.add_collection, name='add'),

]
