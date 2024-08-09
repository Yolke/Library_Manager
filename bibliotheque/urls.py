from django.urls import path
from . import views

urlpatterns = [
    path('livres/', views.liste_livres, name='liste_livres'),
    path('livre/<int:pk>/', views.detail_livre, name='detail_livre'),
    path('livre/ajouter/', views.ajouter_livre, name='ajouter_livre'),
    path('livre/modifier/<int:pk>/', views.modifier_livre, name='modifier_livre'),
    path('livre/supprimer/<int:pk>/', views.supprimer_livre, name='supprimer_livre'),
    path('auteurs/', views.liste_auteurs, name='liste_auteurs'),
    path('auteur/<int:pk>/', views.detail_auteur, name='detail_auteur'),
    path('auteur/ajouter/', views.ajouter_auteur, name='ajouter_auteur'),
    path('auteur/modifier/<int:pk>/', views.modifier_auteur, name='modifier_auteur'),
    path('auteur/supprimer/<int:pk>/', views.supprimer_auteur, name='supprimer_auteur'),
]
