<!-- eslint-disable vue/multi-word-component-names -->
<template>
	<div class="container">
		<div class="row">
			<h1 style="margin-top: 1em;">Ingredients</h1>
		</div>
		<div class="row" style="margin-top:2em; margin-bottom: 3em;">
			<SearchBar v-on:checkIng="checkIngredient"/>
		</div>
		<div v-for="ingredient in filteredList" :key="ingredient">
			<IngredientCard :ingredient="ingredient" />
		</div>
		<h2>Mes ingredients</h2>
		<div v-for="ingredient in $store.state.listeIngredientsPerso" class="row" :key="ingredient.name">
			<IngredientCard :ingredient="ingredient" />
		</div>
		<div class="row justify-content-center">
			<AjouteurInput />
		</div>
	</div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';
import IngredientCard from '@/components/IngredientCard.vue';
import AjouteurInput from '@/components/Ajouteur.vue';

export default {
	name: "IngredientsView",
	created() {
		this.getApiData()
	},
	components: { SearchBar, IngredientCard, AjouteurInput },
	data() {
		return {
			ing: {},
			searchValue: "",
		}
	},
	methods: {
		async getApiData() {
			const API_URL = 'http://127.0.0.1:8000'
			const url = `${API_URL}/ingredients`
			const T = this;
			var myHeaders = new Headers();
			myHeaders.append("Access-Control-Allow-Origin", "*");

			var requestOptions = {
				method: 'GET',
				headers: myHeaders,
				redirect: 'follow'
			};

			fetch(url, requestOptions)
				.then(response => response.text())
				.then(function (result) {
					let data = JSON.parse(result).results
					data.forEach(element => {
						T.$store.dispatch('addIngredient', element)
					});
				})
				.catch(error => console.log('error', error));
		},

		checkIngredient(ing){
			this.searchValue = ing.toLowerCase() 
		},
		add(ingredient){
			this.$store.dispatch('addIngredientPerso', ingredient)
		}
	},
	computed: {
			filteredList() {
				if (this.searchValue == ""){
					return []
				}
				return this.$store.state.listeIngredients.filter((element) => element.nom.toLowerCase().includes(this.searchValue))
			},
	}
}
</script>

<style scoped></style>