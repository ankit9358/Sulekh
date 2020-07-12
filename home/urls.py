from django.urls import path
from .views import home, home2

urlpatterns = [ path('home/<str:msg>/', home, name="home"),
                path('home/', home, name="home"),
                path('home2/', home2, name="home2"),
                path('home2/<slug:user>/', home2),
]

