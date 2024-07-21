from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('profile/<str:id>/', views.profile, name='profile'),
    path('illustrations/', views.illustrations_list, name='illustrations'),
    path('collections/', views.collections_list, name='collections'),
    path('collection/<str:id>/', views.collection_details, name='collection_detail'),
    path('illustration/<str:id>/', views.illustration_detail, name='illustration_detail'),
    path('delete_illustration/<str:id>/', views.delete_illustration, name='delete_illustration'),
    path('delete_collection/<str:id>/', views.delete_collection, name='delete_collection'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register_page, name='register'),
    path('add/', views.add_collection, name='add'),
    path('update', views.update_user, name = 'update'),
    path('collection/<int:collection_id>/update/', views.update_collection, name='update_collection'),
    path('delete_comment/<str:id>/', views.delete_comment, name='delete_comment')
]
