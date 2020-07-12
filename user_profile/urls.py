from django.urls import path
from .views import profile

urlpatterns = [path('profile/<str:msg>/', profile, name="profile"),
               path('profile/', profile, name="profile"),
               ]
