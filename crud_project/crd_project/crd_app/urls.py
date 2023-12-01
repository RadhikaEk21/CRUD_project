from django.urls import path
from.import views
urlpatterns = [
    path('reg/',views.register),
    path('msg/',views.msg)
    
]