from django.urls import path

from . import views

app_name = 'lite'

urlpatterns = [
    path('', views.version, name='version'),
    path('version/<int:lite_pk>/', views.one_version, name='openid'),
    path('correct/<int:lite_pk>/', views.correct, name='correct'),
    path('delete/<int:lite_pk>/', views.delete, name='delete'),
]
