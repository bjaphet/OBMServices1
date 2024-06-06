
from django.urls import path
from apps_utilisateur.views import *

urlpatterns = [
    path('OBM-Services/connection/',Connection,name='connexion'),
    path('OBM-Services/creation/',Creation,name='creation'),
    path('OBM-Services/deconnection/',Deconnection,name='deconnection'),
    path('OBM-Services/404Error/connection',PageError,name='404'),
]