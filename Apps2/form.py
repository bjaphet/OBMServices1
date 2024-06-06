from django import forms
from Apps.models import MaterielsOBM, CategoriesMatos

class AjoutFormMatos(forms.ModelForm):


    nomProduits = forms.CharField(
        help_text='Veuillez entrez le nom du matériel',
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

    desc = forms.CharField(
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
        model = MaterielsOBM

        fields = ['nomProduits', 'category','quantite','desc']
        widgets = {
            'nomProduits': forms.CharField(
            help_text='Veuillez entrer la quantité le nom ',
            error_messages={
                'required': 'Le nom est obligatoire.',
            'invalid': 'Veuillez entrer un nom valide.'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'desc':forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'class': 'form-control',
                    'rows': 4
                }
            ),

            'quantite': forms.TextInput(
                attrs={
                    'placeholder': 'La quantité',
                    'class': 'form-control'
                }
            ),

            }
        
