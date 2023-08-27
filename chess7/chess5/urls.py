from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from testimonials.views import home, about
from sendemail.views import contactView, successView
from signup.views import SignupView, SuccessView, CancelView
from django.http import HttpResponse

def robots_txt(request):
    content = "User-agent: *\nDisallow:"
    return HttpResponse(content, content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", home, name="home"),
    path("about/", about, name="about"),

    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
    
    path("signup/", SignupView, name="signup"), #added as_view() and fixed __init__ issue

    path('cancel/', CancelView.as_view(), name='cancel'),
    path('signedup/', SuccessView.as_view(), name='signedup'),

]




urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)