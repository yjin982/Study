from django.urls import path
from myboard import views


urlpatterns = [
    path('list', views.ListFunc),
    path('insert', views.InsertFunc),
    path('insertok', views.InsertOkFunc),
    path('search', views.SearchFunc),
    path('content', views.ContentFunc),
    path('update', views.UpdateFunc),
    path('updateok', views.UpdateOkFunc),
    path('delete', views.DeleteFunc),
    path('deleteok', views.DeleteOkFunc),
    path('reply', views.ReplyFunc),
    path('replyok', views.ReplyOkFunc),
    
]
