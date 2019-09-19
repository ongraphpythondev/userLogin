from django.urls import path
from . import views
app_name ='verify_app'
urlpatterns = [

    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path("logout/", views.logout_request, name="logout"),
]
