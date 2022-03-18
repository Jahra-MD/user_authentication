from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('',views.IndexView,name="home"),
    path('register/',views.registerView,name='register'),
    path('login/',LoginView.as_view(),name="login_url"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name='logout'),
] 