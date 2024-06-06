from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserCreationForm
from django.contrib import messages
from .forms import *

# Création des fonctions pour les utilisateurs
# def Creation(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             image = form.cleaned_data.get('image')

#             user = User.objects.create_user(username=username, email=email, password=password)
#             profile = user.profile
#             if image:
#                 profile.image = image
#                 profile.save()

#             login(request, user)
#             messages.success(request, 'Compte créé avec succès ! Connectez-vous maintenant.')
#             return redirect('connexion')
#         else:
#             return render(request, 'creation.html', {'form': form})
#     else:
#         form = UserCreationForm()
#         return render(request, 'creation.html', {'form': form})
    


# def Creation(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             image = form.cleaned_data.get('image')  # Image can be None if not provided

#             user = User.objects.create_user(username=username, email=email, password=password)
#             # Save the image to the user profile or handle it as required
#             if image:
#                 user.profile.image = image  # Assuming you have a profile model linked to the user
#                 user.profile.save()

#             login(request, user)
#             messages.success(request, 'Compte créé avec succès ! Connectez-vous maintenant.')
#             return redirect('connexion')
#         else:
#             return render(request, 'connection.html', {'form': form})
#     else:
#         form = UserCreationForm()
#         return render(request, 'creation.html', {'form': form})

#Creation de compte
class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Ce nom d'utilisateur existe déjà ! Réessayez.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cette adresse e-mail est déjà utilisée ! Réessayez.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError("Les mots de passe ne sont pas identiques ! Réessayez.")
        return cleaned_data

def Creation(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, 'Compte créé avec succès ! Connectez-vous maintenant.')
            return redirect('connexion')
        else:
            return render(request, 'connection.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'creation.html', {'form': form})




############################################################################################################################

def Connection(request):
    if request.method == 'POST':
        if 'login_attempts' in request.session:
            login_attempts = request.session['login_attempts']
            if login_attempts >= 5:
                messages.error(request, "Vous avez atteint la limite de tentatives de connexion. c'est la cause de cette rédirectrion réessayez plus tard")
                return redirect('404')
        # Traitement de la soumission du formulaire de connexion
        #Recupere les valeurs de la
        # class LoginForm
        form = LoginForm(request.POST)
        #Si les données saisi sont correctes
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username,password=pwd)
            #Si cela a marché redirige vers la page d'acceuil
            if user is not None:
                #Permet de stocker les infos de utlisateur connecte 
                login(request,user )
                messages.success(request,"Bravo!!! Bienvenue🤩🤗!")
                if 'login_attempts' in request.session:
                    del request.session['login_attempts']
                return redirect('home')
            else:
                # Incrémentation du nombre de tentatives de connexion
                if 'login_attempts' in request.session:
                    request.session['login_attempts'] += 1
                else:
                    request.session['login_attempts'] = 1
                messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe invalide. Réessayez 😥")
    else:
        form = LoginForm()
    return render(request, 'connection.html', {'form': form})

#Deconnection

def Deconnection(request):
    logout(request)
    return redirect('home')


#Page d'erreur
# @login_required(login_url='connection')
def PageError(request):
    return render(request,'404.html')