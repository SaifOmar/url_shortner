from django.urls import path
from . import views
urlpatterns = [ 
    path("",views.home, name = "home"),
    path("url",views.shorten, name = "shorten"),
    path('<short_url>[^/]+',views.redirect_to_origin, name="redirect_to_origin")
] 