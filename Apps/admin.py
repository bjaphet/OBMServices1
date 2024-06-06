from django.contrib import admin

from .models import *


class ListeEmployes(admin.ModelAdmin):
    list_display = ('nom','prenom','quartier','contact', 'fonction')

admin.site.register(ListeEmploye, ListeEmployes)

admin.site.register(CategoriesFonction)


class SortiDuMatoss(admin.ModelAdmin):
    list_display = ('category','quantite','nom','sortie_date', 'nomAgentsAyantPris')

admin.site.register(SortiDuMatos, SortiDuMatoss)


class MatosRendus(admin.ModelAdmin):
    list_display = ('category','quantite','nomProduits','retour_date', 'agentsAyantretour','etat')

admin.site.register(MatosRendu, MatosRendus)


class MaterielsOBMs(admin.ModelAdmin):
    list_display = ('category','quantite','nomProduits','creation_date', 'desc')

admin.site.register(MaterielsOBM, MaterielsOBMs)

admin.site.register(CategoriesMatos)
