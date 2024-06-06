from .form import *
from django.shortcuts import render
from Apps.models import MaterielsOBM
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView

@login_required(login_url='connection')
#fonction affiche les matériels
def affiche_matos(request):
    info = MaterielsOBM.objects.all()
    context = {
        'info': info,
            }
    return render(request,'liste-matériels.html', context )

@login_required(login_url='connection')
def Recherche_Matos(request):
    # Récupération des données en fonction du produit qui est le name qui se trouve dans affichage 
    query = request.GET.get('matos', '')
    info = []

    if query:
        info = MaterielsOBM.objects.filter(nomProduits__icontains=query)

    contexte = {
        "info": info,
        "query": query,  # Pour garder la valeur de recherche dans le formulaire
    }
    return render(request, 'résultat-recherche-matos.html', contexte)

# ajout matériel
class AjoutMatos(LoginRequiredMixin, CreateView):
    login_url = 'connexion' #Précision de l'url de connection agit comme @login_required(login_url='connexion')  grace à 
    model = MaterielsOBM
    form_class = AjoutFormMatos
    template_name = "ajout-matériel.html"
    success_url = reverse_lazy('affiche-matos')

# modification matériel
class Modification_Matos(LoginRequiredMixin, UpdateView):
    login_url = 'connexion'
    model = MaterielsOBM
    form_class = AjoutFormMatos
    template_name = "modification-matos.html"
    success_url = reverse_lazy('affiche-matos')
