from django.contrib import admin
from django.urls import path
from projects.views import project_new
from projects import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.project_list, name='projects_list'),
    path('new/', views.project_new, name='new')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)