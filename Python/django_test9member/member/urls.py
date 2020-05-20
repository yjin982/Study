from django.urls import path
from member import views

urlpatterns = [
    path('list', views.ListFunc),
    path('insert', views.InsertFunc),
    path('idcheck', views.IdCheckFunc),
    path('zipcheck', views.ZipCheckFunc),
    path('zipcheckok', views.ZipCheckOkFunc),
    
]
