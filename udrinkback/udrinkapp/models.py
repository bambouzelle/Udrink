from django.db import models

class Ingredients(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Cocktails(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.BinaryField()
    alcoolise = models.BooleanField()
    categorie = models.CharField(max_length=255)
    verre = models.CharField(max_length=255)
    createur = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

class Ingredients_Cocktails(models.Model):
    cocktails = models.ForeignKey(Cocktails, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    unite = models.CharField(max_length=255)
    
    class Meta:
        unique_together = (("cocktails", "ingredients"))

    def __str__(self):
        return f"{self.id_Cocktails.nom} - {self.id_Ingredients.nom}"

class Commentaires(models.Model):
    cocktails = models.ForeignKey(Cocktails, on_delete=models.CASCADE)
    personne = models.IntegerField()
    note = models.IntegerField()
    avis = models.TextField()

class Favoris(models.Model):
    cocktails = models.ForeignKey(Cocktails, on_delete=models.CASCADE)
    personne = models.IntegerField()

class Ingredients_Personne(models.Model):
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    personne = models.IntegerField()