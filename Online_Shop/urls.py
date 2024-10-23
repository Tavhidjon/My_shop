from django.urls import path
from .views import HomePageView,Registeration,Login,Extra



urlpatterns=[
    path("",HomePageView.as_view(),name="home"),
    path("registration",Registeration.as_view(),name="registration"),
    path("login",Login.as_view(),name="login"),
    path("cart",Login.as_view(),name="cart"),
    path("extra",Extra,name="extra")
]