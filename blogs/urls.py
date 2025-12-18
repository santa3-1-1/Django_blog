from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('signup/', views.signup, name='signup'),
    path('new/', views.new_post, name='new_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
]