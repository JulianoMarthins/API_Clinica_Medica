"""
URL configuration for clinica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from agendamentos.api.viewsets import AgendamentoViewSet
from imagens.api.viewsets import ImagensHistoricoViewSets
from pacientes.api.viewsets import PacientesViewSet
from historicos.api.viewsets import HistoricoViewSet

router = routers.DefaultRouter()
router.register(r'pacientes', PacientesViewSet )
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'historicos', HistoricoViewSet)
router.register(r'imagens_historicos', ImagensHistoricoViewSets)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
