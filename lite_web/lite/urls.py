from django.urls import path

from .views import VersionView

app_name = 'lite'

urlpatterns = [
    path('', VersionView.as_view(), name='version'),
    path('<int:pk>/', VersionView.as_view(), name='version/pk'),
]
