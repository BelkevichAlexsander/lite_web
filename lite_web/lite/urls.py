from django.urls import path

from . import views

app_name = 'lite'

urlpatterns = [
    path('', views.index, name='index'),
    path('version/', views.version, name='version'),
    path('versions/', views.versions, name='versions'),
    path('version/<int:lite_pk>/', views.openid, name='openid'),
    path('version/<int:lite_pk>/correct', views.correct, name='correct'),
    path('version/<int:lite_pk>/delete', views.delete, name='delete'),
]
