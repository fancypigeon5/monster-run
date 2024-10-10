from . import views
from django.urls import path

urlpatterns = [
    path('enterrun/<str:choice>', views.enter_run, name='enter_run'),
    path('deleterun/<int:run_data_id>', views.delete_run, name='delete_run'),
    path('', views.run, name='run_data'),
]
