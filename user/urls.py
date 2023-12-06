from django.urls import path
from .views import cadastro, log, plataforma

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', log, name='login'),
    path('plataforma/', plataforma, name='plataforma')
]
