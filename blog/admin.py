from django.contrib import admin
from .models import Article  # On importe ton modèle Article

admin.site.register(Article) # On dit à Django de l'afficher