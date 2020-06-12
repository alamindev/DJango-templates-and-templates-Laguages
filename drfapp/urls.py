from django.contrib import admin
from django.urls import path, include
from drfapp.views import *
from.import views


 


urlpatterns = [
    path('api/', include(('drfapp.api.urls', 'drfapp'), namespace='drfapp_url')),
    path('Article/', views.get_article, name="article"),
    
    #test 
    path('article_test/', views.test_template, name="article"), 
    path('home_test/', views.home, name="blog_home_url"),
    path('about_test/', views.about, name="blog_about_url"),
]