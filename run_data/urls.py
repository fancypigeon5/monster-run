from . import views
from django.urls import path

urlpatterns = [
    path('enterrun/<str:choice>', views.enter_run, name='enter_run'),
    path('', views.run, name='run_data'),
]