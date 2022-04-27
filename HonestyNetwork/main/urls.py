from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('register', views.register, name = "register"),
    path('logout', views.logout_request, name = "logout"),
    path('login', views.login_request, name = "login"),
    path('selectedSet', views.selectedSet, name = "selectedSet"),
    path('decisionSet', views.decisionSet, name = "decisionSet"),
    path('sets', views.sets_, name = "sets"),
    path('thanks', views.thanks, name = "thanks"),
    path('makePayment', views.makePayment, name = "makePayment"),
    path('handlePay', views.handlePay, name = "handlePay"),
]
