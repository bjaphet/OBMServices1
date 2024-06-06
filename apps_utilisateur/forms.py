from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class LoginForm(forms.Form):
    username =forms.CharField(label='',max_length=15, required=True, widget = forms.TextInput (
        attrs={
            'placeholder':"Nom d'utilisateur",
            "class":'form-control'
            }
        )
        )
    pwd = forms.CharField(label='',required=True ,widget=forms.PasswordInput  (
        attrs={
            'placeholder':"Mot de passe",
            "class":'form-control'
            }
        )
        )
#     image = forms.ImageField(label='',required=True(
#         attrs={
#             "class":'form-control'
#             }
#         )
#         )


class UserCreationForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': "Nom d'utilisateur",
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': "Adresse e-mail",
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': "Mot de passe",
            'class': 'form-control'
        })
    )
    password_confirm = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': "Confirmer le mot de passe",
            'class': 'form-control'
        })
    )
    image = forms.ImageField(
        label='',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )

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

# class UserCreationForm(forms.ModelForm):
#     password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
#         'placeholder': "Mot de passe",
#         'class': 'form-control'
#     }))

#     password_confirm = forms.CharField(label='', widget=forms.PasswordInput(attrs={
#         'placeholder': "Confirmer le mot de passe",
#         'class': 'form-control'
#     }))

#     image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'password_confirm']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         image = self.cleaned_data.get('image')
#         if commit:
#             user.save()
#             profile = Profile.objects.create(user=user, image=image)
#         return user
