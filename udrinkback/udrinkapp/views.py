from django.http import JsonResponse 
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Ingredients, Cocktails, Ingredients_Cocktails


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
