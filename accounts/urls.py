from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about')
]
