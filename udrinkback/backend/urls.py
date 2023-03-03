from django.urls import path
from udrinkapp import views


urlpatterns = [
    # URLs pour Ingredients
    path('ingredients/', views.ingredients_list_create, name='ingredients_list_create'),
    path('ingredients/<int:id>/', views.ingredient_retrieve_update_delete, name='ingredient_retrieve_update_delete'),

    # URLs pour Cocktails
    path('cocktails/', views.cocktails_list_create, name='cocktails_list_create'),
    path('cocktails/<int:id>/', views.cocktail_retrieve_update_delete, name='cocktail_retrieve_update_delete'),

    # URLs pour Ingredients_Cocktails
    path('ingredients_cocktails/', views.ingredients_cocktails_list_create, name='ingredients_cocktails_list_create'),
    path('ingredients_cocktails/<int:id>/', views.ingredient_cocktail_retrieve_update_delete, name='ingredient_cocktail_retrieve_update_delete'),

    path('ingredients/<int:ingredients_id>/cocktails/', views.cocktails_in_ingredients,name="cocktails_in_ingredients"),
    path('cocktails/<int:cocktails_id>/ingredients/', views.ingredients_in_cocktails,name="ingredients_in_cocktails"),

    path('personne/<int:personne_id>/favoris/', views.favoris_in_personne,name="favoris_in_personne"),
    path('personne/<int:personne_id>/ingredients/', views.ingredients_in_personne,name="ingredients_in_personne"),
    path('cocktails/<int:cocktails_id>/commentaires/', views.commentaires_in_cocktails,name="commentaires_in_cocktails"),
]
