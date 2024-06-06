from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name="home"),
    
    path('OBM/Liste-Materiels-Ajout',AjoutEmployer.as_view(),name="ajout-employer"),
    path('OBM/Liste-Materiels-Modification/Employer/<int:pk>/',Modification_Employer.as_view(),name="modification-employer"),

    path('OBM/Resultat-Recherche-employé/',search_employé,name="recherche-employer"),


    path('OBM/Liste-Materiels-sortie/',affiche_sortie,name="affiche-sortie"),
    path('OBM/Liste-Materiels-retour/',affiche_retour,name="affiche-retour"),
    path('OBM/Liste-Materiels-sortie-form/',sortieForm.as_view(),name="affiche-sortie-form"),
    path('OBM/Liste-Materiels-revenue-form/',retourForm.as_view(),name="affiche-retour-form"),
]





