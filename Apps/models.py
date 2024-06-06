from django.db import models

# Modèle pour les catégories des matériels
class CategoriesMatos(models.Model):
    nom = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom

# Modèle pour les catégories de fonctions
class CategoriesFonction(models.Model):
    nom = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom

# Modèle pour la liste des employés
class ListeEmploye(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    quartier = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    fonction = models.ForeignKey(CategoriesFonction, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"

# Modèle pour l'ajout des matériels
class MaterielsOBM(models.Model):
    category = models.ForeignKey(CategoriesMatos, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    nomProduits = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    
    class Meta:
        ordering = ['-creation_date']
    
    def __str__(self):
        return self.nomProduits

# Modèle pour la sortie des matériels
class SortiDuMatos(models.Model):
    category = models.ForeignKey(CategoriesMatos, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    nom = models.ForeignKey(MaterielsOBM, on_delete=models.CASCADE)
    sortie_date = models.DateTimeField(auto_now_add=True)
    nomAgentsAyantPris = models.ForeignKey(ListeEmploye, on_delete=models.CASCADE,  default='1')

    class Meta:
        ordering = ['-sortie_date']


# Modèle pour le retour des matériels
class MatosRendu(models.Model):
    category = models.ForeignKey(CategoriesMatos, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    nomProduits = models.ForeignKey(MaterielsOBM, on_delete=models.CASCADE)
    retour_date = models.DateTimeField(auto_now_add=True)
    agentsAyantretour = models.ForeignKey(ListeEmploye, on_delete=models.CASCADE)
    etat = models.TextField(default='1')
    
    class Meta:
        ordering = ['-retour_date']

