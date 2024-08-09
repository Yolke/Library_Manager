from django.shortcuts import render, get_object_or_404, redirect
from .models import Auteur, Livre
from .forms import AuteurForm, LivreForm

# Liste des livres
def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'bibliotheque/liste_livres.html', {'livres': livres})

# Détails d'un livre
def detail_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    return render(request, 'bibliotheque/detail_livre.html', {'livre': livre})

# Ajouter un livre
def ajouter_livre(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'bibliotheque/ajouter_livre.html', {'form': form})

# Modifier un livre
def modifier_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == "POST":
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('detail_livre', pk=livre.pk)
    else:
        form = LivreForm(instance=livre)
    return render(request, 'bibliotheque/modifier_livre.html', {'form': form})

# Supprimer un livre
def supprimer_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == "POST":
        livre.delete()
        return redirect('liste_livres')
    return render(request, 'bibliotheque/supprimer_livre.html', {'livre': livre})

# Liste des auteurs
def liste_auteurs(request):
    auteurs = Auteur.objects.all()
    return render(request, 'bibliotheque/liste_auteurs.html', {'auteurs': auteurs})

# Détails d'un auteur
def detail_auteur(request, pk):
    auteur = get_object_or_404(Auteur, pk=pk)
    return render(request, 'bibliotheque/detail_auteur.html', {'auteur': auteur})

# Ajouter un auteur
def ajouter_auteur(request):
    if request.method == "POST":
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_auteurs')
    else:
        form = AuteurForm()
    return render(request, 'bibliotheque/ajouter_auteur.html', {'form': form})

# Modifier un auteur
def modifier_auteur(request, pk):
    auteur = get_object_or_404(Auteur, pk=pk)
    if request.method == "POST":
        form = AuteurForm(request.POST, instance=auteur)
        if form.is_valid():
            form.save()
            return redirect('detail_auteur', pk=auteur.pk)
    else:
        form = AuteurForm(instance=auteur)
    return render(request, 'bibliotheque/modifier_auteur.html', {'form': form})

# Supprimer un auteur
def supprimer_auteur(request, pk):
    auteur = get_object_or_404(Auteur, pk=pk)
    if request.method == "POST":
        auteur.delete()
        return redirect('liste_auteurs')
    return render(request, 'bibliotheque/supprimer_auteur.html', {'auteur': auteur})
