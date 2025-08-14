from django.urls import path
from . import views

urlpatterns = [

    # New 4-page setup
    path('', views.landing_view, name='landing'),  # Landing page is now root
    path('home/', views.home_view, name='home'),
    path('candidates/', views.candidates_view, name='candidates'),
    path('profile/', views.profile_view, name='profile'),
    
     # Auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]