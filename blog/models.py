from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200) # Un titre court
    contenu = models.TextField()               # Un texte long
    date_publication = models.DateTimeField(auto_now_add=True) # Date automatique

    def __str__(self):
        return self.titre # Pour voir le titre dans l'administration