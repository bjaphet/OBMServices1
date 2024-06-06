from .form import *
from .models import *
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q, Sum
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView

#fonction principale

@login_required(login_url='connexion')
def home(request):
    donnees = ListeEmploye.objects.all()
    
    try:
        informatique = CategoriesMatos.objects.get(nom='Informatique & Technique')
        total_informatique = MaterielsOBM.objects.filter(category=informatique).aggregate(total_quantite=Sum('quantite'))['total_quantite']
    except CategoriesMatos.DoesNotExist:
        total_informatique = 0

    try:
        secretariat = CategoriesMatos.objects.get(nom='Secrétariat')
        total_secretariat = MaterielsOBM.objects.filter(category=secretariat).aggregate(total_quantite=Sum('quantite'))['total_quantite']
    except CategoriesMatos.DoesNotExist:
        total_secretariat = 0
    
    try:
        nettoyage = CategoriesMatos.objects.get(nom='Nettoyage')
        total_nettoyage = MaterielsOBM.objects.filter(category=nettoyage).aggregate(total_quantite=Sum('quantite'))['total_quantite']
    except CategoriesMatos.DoesNotExist:
        total_nettoyage = 0

    total_employes = ListeEmploye.objects.count()

    context = {
        'donnees': donnees,
        'total_informatique': total_informatique if total_informatique else 0,
        'total_secretariat': total_secretariat if total_secretariat else 0,
        'total_nettoyage': total_nettoyage if total_nettoyage else 0,
        'total_employes': total_employes,
    }
    
    return render(request, 'home.html', context)


@login_required(login_url='connexion')
#fonction affiche les sorties des matériels
def affiche_sortie(request):
    donnees = SortiDuMatos.objects.all()
    context = {
        'donnees': donnees,
            }
    return render(request,'sortie-matériel.html', context )

@login_required(login_url='connexion')
#fonction affiche les retours des matériels
def affiche_retour(request):
    donnees = MatosRendu.objects.all()
    context = {
        'donnees': donnees,
            }
    return render(request,'retour-matériel.html', context )

#fonction formulaire pour la sortie du matos
class sortieForm(LoginRequiredMixin,CreateView):
    login_url = 'connexion' #Précision de l'url de connection agit comme @login_required(login_url='connexion')  grace à 
    model = SortiDuMatos
    form_class = sortieForm
    template_name = "form-sortir-matos.html"
    success_url = reverse_lazy('affiche-sortie')

# @login_required(login_url='connection')
#fonction formulaire pour le retour du matos
class retourForm(LoginRequiredMixin, CreateView):
    login_url = 'connexion' #Précision de l'url de connection agit comme @login_required(login_url='connexion')  grace à 
    model = SortiDuMatos
    form_class = FormRetour
    template_name = "form-retour-matos.html"
    success_url = reverse_lazy('affiche-retour')

# Ajout des matériels
class AjoutEmployer(LoginRequiredMixin, CreateView):
    login_url = 'connexion' #Précision de l'url de connection agit comme @login_required(login_url='connexion')  grace à 
    model = ListeEmploye
    form_class = AjoutFormEmployer
    template_name = "ajout-employer.html"
    success_url = reverse_lazy('home')

# Modification des matériels
class Modification_Employer(LoginRequiredMixin, UpdateView):
    login_url = 'connexion'
    model = ListeEmploye
    form_class = AjoutFormEmployer
    template_name = "modification-employer.html"
    success_url = reverse_lazy('home')

@login_required(login_url='connection')
#fonction pour la recherche des employés
def search_employé(request):
    query = request.GET.get('employer', '')
    donnees = ListeEmploye.objects.filter(
        models.Q(nom__icontains=query) |
        models.Q(prenom__icontains=query) |
        models.Q(fonction__nom__icontains=query) |
        models.Q(quartier__icontains=query)
    ) if query else []

    contexte = {
        "donnees": donnees,
        "query": query,
    }
    return render(request, 'résultat-recherche-employer.html', contexte)