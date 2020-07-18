from django.urls import path
from .views import home_views,blog_views

app_name = 'blogapp'
urlpatterns = [
   path('',home_views,name="home"),
   path('blog',blog_views,name="blog"),

]

