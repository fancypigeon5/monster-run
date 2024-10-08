"""
URL configuration for monster_run project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500, handler403, handler405

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("arena/", include("arena.urls"), name="arena-urls"),
    path("equipment/", include("equipment.urls"), name="equipment-urls"),
    path("rundata/", include("run_data.urls"), name="run-data-urls"),
    path("", include("monster.urls"), name="monster-urls"),
]

handler404 = 'monster_run.views.handler404'
handler500 = 'monster_run.views.handler500'
handler403 = 'monster_run.views.handler403'
handler405 = 'monster_run.views.handler405'
