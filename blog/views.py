from django.shortcuts import render, get_object_or_404 # Vérifie bien cet import !
from .models import Article

# 1. La liste
def liste_articles(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'blog/liste.html', {'articles': articles})

# 2. Le détail (C'EST CELLE-CI QUI MANQUE SUREMENT)
def detail_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/detail.html', {'article': article})