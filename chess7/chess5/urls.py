"""chess5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from testimonials.views import home, about
from sendemail.views import contactView, successView
from signup.views import SignupView, SuccessView, CancelView#, CreateCheckoutSessionView


urlpatterns = [
    path('admin/', admin.site.urls),

    path("", home, name="home"),
    path("about/", about, name="about"),

    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
    
    path("signup/", SignupView, name="signup"), #added as_view() and fixed __init__ issue

    path('cancel/', CancelView.as_view(), name='cancel'),
    path('signedup/', SuccessView.as_view(), name='signedup'),
    #path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    #path('', ProductLandingPageView.as_view(), name='landing'),
]
