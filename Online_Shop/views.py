from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name="home.html"


class Registeration(TemplateView):
    template_name="registration.html"

class Login(TemplateView):
    template_name="login.html"


class Cart(TemplateView):
    template_name="cart.html"
