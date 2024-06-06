from django.urls import path
from .views import  affiche_matos, Recherche_Matos, Modification_Matos,AjoutMatos


urlpatterns = [
        path('OBM/Liste-Materiels/',affiche_matos,name="affiche-matos"),
        path('OBM/Liste-Materiels-Ajout',AjoutMatos.as_view(),name="ajout-matos"),
        path('OBM/Liste-Materiels/Modification/<int:pk>/',Modification_Matos.as_view(),name="modification-matos"),
        path('OBM/Resultat-Recherche-matos/',Recherche_Matos,name="recherche-matos"),
]
