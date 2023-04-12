<!-- eslint-disable vue/multi-word-component-names -->
<template>
	<div class="container">
		<div class="row">
			<h1>Ingredients</h1>
		</div>
		<div class="row" style="margin-top:3em; margin-bottom: 3em;">
			<SearchBar />
		</div>
		<div v-for="ingredient in $store.state.listeIngredients" class="row" :key="ingredient.name" style="margin-bottom: 1em;">
			<IngredientCard :ingredient="ingredient" />
		</div>
		<div class="row justify-content-center" >
			<AjouteurInput/>
		</div>
	</div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';
import IngredientCard from '@/components/IngredientCard.vue';
import AjouteurInput from '@/components/Ajouteur.vue';

export default {
	name: "IngredientsView",
	created(){
		},
	components:{SearchBar, IngredientCard, AjouteurInput},
	data(){
		return {
		}
	}, 
}
</script>

<style scoped>
	
</style>