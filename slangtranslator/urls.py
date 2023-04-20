from django.urls import path, include
from . import views
from django.contrib import admin




urlpatterns = [
    path("admin/", admin.site.urls),
    #path("slangtranslator/", include('slangtranslator.urls')),
    path('hello/', views.say_hello), 
    path('slangreturn/', views.slangreturn, name = 'slang-response'),
    path('api/submit-string/', views.submit_string, name='submit_string'),
    
]