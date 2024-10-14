from django.contrib import admin
from django.urls import path
from rest_app import views



urlpatterns = [
    
    path("admin/",admin.site.register),
    path('stuinfo/<int:pk>',views.student_Details),
    path('stuinfo/',views.student_list),
]


