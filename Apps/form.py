from django import forms
from .models import *


# Ajout desemployer dans la BD
class AjoutFormEmployer(forms.ModelForm):


    nom = forms.CharField(
        help_text='Veuillez entrez le nom du matériel',
        error_messages={
            'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez sélectionner un nom valide.'
        }
    )
    prenom = forms.CharField(
        help_text='Veuillez entrez le nom du matériel',
        error_messages={
            'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez sélectionner un nom valide.'
        }
    )
    quartier = forms.CharField(
        help_text='Veuillez entrez le nom du matériel',
        error_messages={
            'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez sélectionner un nom valide.'
        }
    )
    contact = forms.CharField(
        help_text='Veuillez entrez le nom du matériel',
        error_messages={
            'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez sélectionner un nom valide.'
        }
    )

    fonction = forms.ModelChoiceField(
        queryset=CategoriesFonction.objects.all(),
        help_text='Veuillez sélectionner la catégorie du produit',
        error_messages={
            'required': 'La catégorie est obligatoire.',
            'invalid': 'Veuillez sélectionner une catégorie valide.'
        }
    )

    class Meta:
        model = ListeEmploye

        fields = ['nom', 'prenom', 'quartier','contact','fonction']
        widgets = {
            'nom': forms.CharField(
            help_text='Veuillez entrer le nom employer',
            error_messages={
                'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez entrer un nom valide.'
                }
            ),
            'prenom': forms.CharField(
            help_text='Veuillez entrer le prénom employer',
            error_messages={
                'required': 'Le prénom est obligatoire.',
            'invalid': 'Veuillez entrer un prénom valide.'
                }
            ),
            'quartier': forms.CharField(
            help_text='Veuillez entrer le quartier',
            error_messages={
                'required': 'Le quartier est obligatoire.',
            'invalid': 'Veuillez entrer un quartier valide.'
                }
            ),
            'contact': forms.CharField(
            help_text='Veuillez entrer le contact',
            error_messages={
                'required': 'Le contact est obligatoire.',
            'invalid': 'Veuillez entrer un contact valide.'
                }
            ),
            'fonction': forms.CharField(
            help_text='Veuillez entrer la fonction',
            error_messages={
                'required': 'La fonction est obligatoire.',
            'invalid': 'Veuillez entrer une fonction valide.'
                }
            )

            }
        
# gere la sortie des matériel 
class sortieForm(forms.ModelForm):


    nom = forms.ModelChoiceField(
        queryset=MaterielsOBM.objects.all(),
        help_text='Veuillez sélectionner le nom du matériel',
        error_messages={
            'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez sélectionner un nom valide.'
        }
    )

    category = forms.ModelChoiceField(
        queryset=CategoriesMatos.objects.all(),
        help_text='Veuillez sélectionner la catégorie du produit',
        error_messages={
            'required': 'La catégorie est obligatoire.',
            'invalid': 'Veuillez sélectionner une catégorie valide.'
        }
    )

    nomAgentsAyantPris = forms.ModelChoiceField(
        queryset=ListeEmploye.objects.all(),
        help_text="Veuillez sélectionner le nom de l'employé",
        error_messages={
            'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez sélectionner un nom valide.'
        }
    )
       
    quantite = forms.IntegerField(
        help_text='Veuillez entrer la quantité de sortie',
        error_messages={
            'required': 'La quantité est obligatoire.',
            'invalid': 'Veuillez entrer une quantité valide.'
        }
    )

    class Meta:
        model = SortiDuMatos
        fields = ['nom', 'category','quantite','nomAgentsAyantPris']
        widgets = {
            'nom': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nomAgentsAyantPris': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantite': forms.TextInput(
                attrs={
                    'placeholder': 'La quantité',
                    'class': 'form-control'
                }
            ),

            }

# gère le retour des matériels après l'utilisation
class FormRetour(forms.ModelForm):

    nomProduits = forms.ModelChoiceField(
        queryset=MaterielsOBM.objects.all(),
        help_text='Veuillez sélectionner le nom du matériel',
        error_messages={
            'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez sélectionner un nom valide.'
        }
    )

    category = forms.ModelChoiceField(
        queryset=CategoriesMatos.objects.all(),
        help_text='Veuillez sélectionner la catégorie du produit',
        error_messages={
            'required': 'La catégorie est obligatoire.',
            'invalid': 'Veuillez sélectionner une catégorie valide.'
        }
    )

    agentsAyantretour = forms.ModelChoiceField(
        queryset=ListeEmploye.objects.all(),
        help_text="Veuillez sélectionner le nom de l'employé",
        error_messages={
            'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez sélectionner un nom valide.'
        }
    )
       
    quantite = forms.IntegerField(
        help_text='Veuillez entrer la quantité de sortie',
        error_messages={
            'required': 'La quantité est obligatoire.',
            'invalid': 'Veuillez entrer une quantité valide.'
        }
    )
    etat = forms.CharField(
        help_text="Veuillez entrer l'état du matériel, après usage",
        error_messages={
            'required': 'La quantité est obligatoire.',
            'invalid': 'Veuillez entrer une quantité valide.'
        }
    )

    class Meta:
        model = MatosRendu
        fields = ['nomProduits', 'category','quantite','agentsAyantretour','etat']
        widgets = {
            'nomProduits': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nomAgentsAyantPris': forms.Select(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),
            'quantite': forms.TextInput(
                attrs={
                    'placeholder': 'La quantité',
                    'class': 'form-control',
                    'rows': 4
                }
            ),
            'etat':forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'class': 'form-control',
                    'rows': 4
                }
            ),

            }