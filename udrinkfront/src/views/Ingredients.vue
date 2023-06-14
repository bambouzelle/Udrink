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
		this.getApiData()
		},
	components:{SearchBar, IngredientCard, AjouteurInput},
	data(){
		return {
			ing:{}
		}
	}, 
	methods: {
		async getApiData () {
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
			.then(function(result) {
				let data = JSON.parse(result).results
				console.log(data)
				data.forEach(element => {
					T.$store.dispatch('addIngredient', element)
					});
				})
			.catch(error => console.log('error', error));
			}
	}
}
</script>

<style scoped>
	
</style>