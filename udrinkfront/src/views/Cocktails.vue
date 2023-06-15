<!-- eslint-disable vue/multi-word-component-names -->
<template>
	<div class="container">
		<div class="row">
			<div class="col">
				<h1>Cocktails</h1>
			</div>
		</div>

		<div v-for="cocktail in dataToShow" class="row" :key="cocktail" style="margin-top: 2em;">
			<CocktailCard :cocktail="cocktail"/>
		</div>

		<div v-if="noMore"> Vous avez vu tout les cocktails !</div>
	</div>
</template>

<script>
import CocktailCard from "@/components/CocktailCard.vue"
const API_URL = 'http://127.0.0.1:8000'

export default {
	components: { CocktailCard },
	name: 'CocktailsView',
	data() {
		return {
			data:[],
			dataToShow:[],
			ingredients:[],
			noMore: false
		}
	},
	mounted(){
		//this.$store.dispatch('resetCocktails')
		if (this.$store.state.listeCocktails.length == 0){
					this.getApiData();
		}
		this.getMoreData();
	},
	methods:{
		getNextCocktails(){
			window.onscroll = () => {
				let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;

				if (bottomOfWindow) {
						console.log('rendu en bas')
						this.getMoreData()
				}
			};
		},

		getMoreData(){
			let i = this.dataToShow.length;
			let imax = i+10;
			for ( i ; i<imax ; i++){
				if (this.$store.state.listeCocktails[i]){
					this.dataToShow.push(this.$store.state.listeCocktails[i])
				}
				else{
					this.noMore = true
				}
			}
		},

		async getIngredients (cocktail) {
      const url = `${API_URL}/cocktails/${cocktail.id}/ingredients`;
			var myHeaders = new Headers();
			myHeaders.append("Access-Control-Allow-Origin", "*");

			var requestOptions = {
			method: 'GET',
			headers: myHeaders,
			redirect: 'follow'
			};

			let res = []
			const response = await fetch(url, requestOptions)
			const data = await response.json()
			await data.ingredients.forEach(element => {
				res.push(element.nom)
			})
			this.$store.state.listeCocktails.forEach(el => {
				if (el.nom == cocktail.nom){
					el.ingredients = res
				}
			})
		},

		async getApiData () {
			await this.getCocktails();
			await this.$store.state.listeCocktails.forEach(cocktail => {
					this.getIngredients(cocktail)
					cocktail.ingredients = this.ingredients

			})
		},

		async getCocktails(){
      const url = `${API_URL}/cocktails`
			var myHeaders = new Headers();
			myHeaders.append("Access-Control-Allow-Origin", "*");

			var requestOptions = {
			method: 'GET',
			headers: myHeaders,
			redirect: 'follow'
			};

			const response = await fetch(url, requestOptions)
			const data = await response.json()
			data.results.forEach(element => {
					this.$store.dispatch('addCocktail', element)
				});
			this.getMoreData();
			this.getNextCocktails();
		}
	}
}
</script>

<style>
ul {
	list-style-type: none;
}
</style>