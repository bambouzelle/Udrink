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
			data: [
			],
			dataToShow:[],
			noMore: false
		}
	},
	mounted(){
		this.getApiData();
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
				if (this.data[i]){
					this.dataToShow.push(this.data[i])
				}
				else{
					this.noMore = true
				}
			}
		},

		async getIngredients (id_cocktail) {
			//const T = this
      const url = `${API_URL}/cocktails/${id_cocktail}/ingredients`;
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
				//let data = JSON.parse(result)
				console.log(result)
				/*let in_arr = []
				data.forEach(element => {
					in_arr.push(element)
				});
				T.data.*/
			})
			.catch(error => console.log('error', error));
		},

		async getApiData () {
			const T = this
      const url = `${API_URL}/cocktails`
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
					console.log(element.id)
					T.data.push(element)
					//T.getIngredients( element.id); TODO corrigé ce retour 500
				});
				T.getMoreData();
				T.getNextCocktails();
			})
			.catch(error => console.log('error', error));
		}
	}
}
</script>

<style>
ul {
	list-style-type: none;
}
</style>