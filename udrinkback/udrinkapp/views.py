from django.http import JsonResponse 
import json
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from .models import Ingredients, Cocktails, Ingredients_Cocktails, Commentaires, Favoris,Ingredients_Personne
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')

@csrf_exempt
def ingredients_list_create(request):
    if request.method == 'GET':
        ingredients = Ingredients.objects.all()
        data = {'results': list(ingredients.values('id', 'nom', 'description'))}
        return JsonResponse(data)

    elif request.method == 'POST':
        payload = json.loads(request.body)
        nom = payload.get('nom')
        description = payload.get('description')

        ingredient = Ingredients(nom=nom, description=description)
        ingredient.save()

        data = {'message': f"Ingredient '{nom}' créé avec succès!"}
        return JsonResponse(data, status=201)


@csrf_exempt
def ingredient_retrieve_update_delete(request, id):
    try:
        ingredient = Ingredients.objects.get(id=id)
    except Ingredients.DoesNotExist:
        data = {'message': f"L'ingredient avec l'id {id} n'existe pas!"}
        return JsonResponse(data, status=404)

    if request.method == 'GET':
        data = {
            'id': ingredient.id,
            'nom': ingredient.nom,
            'description': ingredient.description
        }
        return JsonResponse(data)

    elif request.method == 'PUT':
        payload = json.loads(request.body)
        nom = payload.get('nom')
        description = payload.get('description')

        ingredient.nom = nom
        ingredient.description = description
        ingredient.save()

        data = {'message': f"L'ingredient avec l'id {id} a été mis à jour avec succès!"}
        return JsonResponse(data)

    elif request.method == 'DELETE':
        ingredient.delete()
        data = {'message': f"L'ingredient avec l'id {id} a été supprimé avec succès!"}
        return JsonResponse(data, status=204)


@csrf_exempt
def cocktails_list_create(request):
    if request.method == 'GET':
        cocktails = Cocktails.objects.all()
        data = {'results': list(cocktails.values('id', 'nom', 'description', 'image', 'alcoolise', 'categorie', 'verre', 'createur'))}
        return JsonResponse(data)

    elif request.method == 'POST':
        payload = json.loads(request.body)
        nom = payload.get('nom')
        description = payload.get('description')
        image = payload.get('image')
        alcoolise = payload.get('alcoolise')
        categorie = payload.get('categorie')
        verre = payload.get('verre')
        createur = payload.get('createur', 0)

        cocktail = Cocktails(nom=nom, description=description, image=image, alcoolise=alcoolise, categorie=categorie, verre=verre, createur=createur)
        cocktail.save()

        data = {'message': f"Cocktail '{nom}' créé avec succès!"}
        return JsonResponse(data, status=201)


@csrf_exempt
def cocktail_retrieve_update_delete(request, id):
    try:
        cocktail = Cocktails.objects.get(id=id)
    except Cocktails.DoesNotExist:
        data = {'message': f"Le cocktail avec l'id {id} n'existe pas!"}
        return JsonResponse(data, status=404)

    if request.method == 'GET':
        data = {
            'id': cocktail.id,
            'nom': cocktail.nom,
            'description': cocktail.description,
            'image': cocktail.image,
            'alcoolise': cocktail.alcoolise,
            'categorie': cocktail.categorie,
            'verre': cocktail.verre,
            'createur': cocktail.createur
        }
        return JsonResponse(data)

    elif request.method == 'PUT':
        payload = json.loads(request.body)
        nom = payload.get('nom')
        description = payload.get('description')
        image = payload.get('image')
        alcoolise = payload.get('alcoolise')
        categorie = payload.get('categorie')
        verre = payload.get('verre')
        createur = payload.get('createur')

        cocktail.nom = nom
        cocktail.description = description
        cocktail.image = image
        cocktail.alcoolise = alcoolise
        cocktail.categorie = categorie
        cocktail.verre = verre
        cocktail.createur = createur
        cocktail.save()

        data = {'message': f"Le cocktail avec l'id {id} a été mis à jour avec succès!"}
        return JsonResponse(data)

    elif request.method == 'DELETE':
        cocktail.delete()
        data = {'message': f"Le cocktail avec l'id {id} a été supprimé avec succès!"}
        return JsonResponse(data, status=204)

@csrf_exempt
def ingredients_cocktails_list_create(request):
    if request.method == 'GET':
        ingredients_cocktails = Ingredients_Cocktails.objects.all()
        data = {'results': list(ingredients_cocktails.values('cocktails', 'ingredients', 'quantite', 'unite'))}
        return JsonResponse(data)

    elif request.method == 'POST':
        payload = json.loads(request.body)
        cocktails = payload.get('cocktails')
        ingredients = payload.get('ingredients')
        quantite = payload.get('quantite')
        unite = payload.get('unite')

        try:
            cocktail = Cocktails.objects.get(id=cocktails)
        except Cocktails.DoesNotExist:
            data = {'message': f"Le cocktail avec l'id {cocktails} n'existe pas!"}
            return JsonResponse(data, status=404)

        try:
            ingredient = Ingredients.objects.get(id=ingredients)
        except Ingredients.DoesNotExist:
            data = {'message': f"L'ingredient avec l'id {ingredients} n'existe pas!"}
            return JsonResponse(data, status=404)

        ingredient_cocktail = Ingredients_Cocktails(cocktails=cocktail, ingredients=ingredient, quantite=quantite, unite=unite)
        ingredient_cocktail.save()

        data = {'message': f"La relation entre le cocktail '{cocktail.nom}' et l'ingredient '{ingredient.nom}' a été créée avec succès!"}
        return JsonResponse(data, status=201)


@csrf_exempt
def ingredient_cocktail_retrieve_update_delete(request, id):
    try:
        ingredient_cocktail = Ingredients_Cocktails.objects.get(id = id)
        cocktails = ingredient_cocktail.cocktails
        ingredients = ingredient_cocktail.ingredients
    except Ingredients_Cocktails.DoesNotExist:
        data = {'message': f"La relation entre le cocktail avec l'id {cocktails} et l'ingredient avec l'id {ingredients} n'existe pas!"}
        return JsonResponse(data, status=404)

    if request.method == 'GET':
        data = {
            'cocktails': ingredient_cocktail.cocktails.id,
            'ingredients': ingredient_cocktail.ingredients.id,
            'quantite': ingredient_cocktail.quantite,
            'unite': ingredient_cocktail.unite
        }
        return JsonResponse(data)

    elif request.method == 'PUT':
        payload = json.loads(request.body)
        quantite = payload.get('quantite')
        unite = payload.get('unite')

        ingredient_cocktail.cocktails = cocktails
        ingredient_cocktail.ingredients = ingredients
        ingredient_cocktail.quantite = quantite
        ingredient_cocktail.unite = unite
        ingredient_cocktail.save()

        data = {'message': f"La relation entre le cocktail avec l'id {cocktails} et l'ingredient avec l'id {ingredients} a été mise à jour avec succès!"}
        return JsonResponse(data)

    elif request.method == 'DELETE':
        ingredient_cocktail.delete()
        data = {'message': f"La relation entre le cocktail avec l'id {cocktails} et l'ingredient avec l'id {ingredients} a été supprimée avec succès!"}
        return JsonResponse(data, status=204)

@csrf_exempt
def ingredients_in_cocktails(request, cocktails_id):
    cocktails = get_object_or_404(Cocktails, pk=cocktails_id)
    ingredients = Ingredients.objects.filter(ingredients_cocktails__cocktails=cocktails).values()
    data = {'cocktail': cocktails.nom, 'ingredients': list(ingredients)}
    return JsonResponse(data)

@csrf_exempt
def cocktails_in_ingredients(request, ingredients_id):
    ingredients = get_object_or_404(Ingredients, pk=ingredients_id)
    cocktails = Cocktails.objects.filter(ingredients_cocktails__id_Ingredients=ingredients.id).values()
    data = {'ingredient': ingredients.nom, 'cocktail': list(cocktails)}
    return JsonResponse(data)


@csrf_exempt
def favoris_in_personne(request, personne_id):
    if request.method == 'GET':
        favoris = Favoris.objects.filter(personne_id=personne_id)
        data = []
        for fav in favoris:
            fav_dict = {}
            fav_dict['id'] = fav.id
            fav_dict['cocktail'] = fav.cocktails.nom
            data.append(fav_dict)
        return JsonResponse(data, safe=False)
        
    elif request.method == 'POST':
        payload = json.loads(request.body)
        cocktails_id = payload.get('cocktails')

        try:
            cocktail = Cocktails.objects.get(id=cocktails_id)
        except Cocktails.DoesNotExist:
            data = {'message': f"Le cocktail avec l'id {cocktails_id} n'existe pas!"}
            return JsonResponse(data, status=404)

        favori = Favoris(cocktails=cocktail, personne_id=personne_id)
        favori.save()

        data = {'message': f"Le cocktail '{cocktail.nom}' a été ajouté aux favoris de la personne {personne_id} avec succès!"}
        return JsonResponse(data, status=201)


@csrf_exempt
def ingredients_in_personne(request, personne_id):
    if request.method == 'GET':
        ingredients_personne = Ingredients_Personne.objects.filter(personne_id=personne_id)
        data = []
        for ing in ingredients_personne:
            ing_dict = {}
            ing_dict['id'] = ing.id
            ing_dict['ingredients'] = ing.ingredients.nom
            data.append(ing_dict)
        return JsonResponse(data, safe=False)


    elif request.method == 'POST':
        payload = json.loads(request.body)
        ingredient_id = payload.get('ingredients')

        try:
            ingredient = Ingredients.objects.get(id=ingredient_id)
        except Ingredients.DoesNotExist:
            data = {'message': f"L'ingredient avec l'id {ingredient_id} n'existe pas!"}
            return JsonResponse(data, status=404)

        ingredients_personne = Ingredients_Personne(ingredients=ingredient, personne_id=personne_id)
        ingredients_personne.save()

        data = {'message': f"La relation entre la personne '{personne_id}' et l'ingrédient avec l'ID '{ingredient.id}' a été créée avec succès!"}
        return JsonResponse(data, status=201)

@csrf_exempt
def commentaires_in_cocktails(request, cocktails_id):
    if request.method == 'GET':
        cocktails = get_object_or_404(Cocktails, pk=cocktails_id)
        commentaires = Commentaires.objects.filter(cocktails_id=cocktails.id).values()
        data = {'cocktail': cocktails.nom, 'commentaires': list(commentaires)}
        return JsonResponse(data)

    elif request.method == 'POST':
        payload = json.loads(request.body)
        personne_id = payload.get('personne')
        note = payload.get('note')
        avis = payload.get('avis')
        nom = payload.get('nom')

        try:
            cocktail = Cocktails.objects.get(id=cocktails_id)
        except Cocktails.DoesNotExist:
            data = {'message': f"Le cocktail avec l'id {cocktails_id} n'existe pas!"}
            return JsonResponse(data, status=404)

        commentaire = Commentaires(cocktails=cocktail, personne_id=personne_id, nom=nom, note=note, avis=avis)
        commentaire.save()

        data = {'message': f"La relation entre le cocktail '{cocktail.nom}' et le commentaire '{commentaire.nom}' a été créée avec succès!"}
        return JsonResponse(data, status=201)
