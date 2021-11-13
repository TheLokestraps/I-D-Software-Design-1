from .views import aviso, inicio, conocenos, ofrecer
from django.urls import path

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('conocenos', conocenos, name = 'conocenos'),
    path('ofrecer', ofrecer, name = 'ofrecer'),
    path('aviso', aviso, name = 'aviso'),
]