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

export default {
	components: { CocktailCard },
	name: 'CocktailsView',
	data() {
		return {
			data: [
				{ id: 1, title: "Cocktail1", ingredients: ["I1", "I2"], description: "HOW TO DO IT", glass: "coupe" },
				{ id: 2, title: "Cocktail2", ingredients: ["I1", "I2", "I3"], description: "HOW TO DO IT GOOF", glass: "ballon" },
				{ id: 3, title: "Cocktail3", ingredients: ["I1", "I2", "I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "whiskey" },
				{ id: 4, title: "Cocktail3", ingredients: ["I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "shooter" },
				{ id: 5, title: "Cocktail3", ingredients: ["I2", "I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "biere" },
				{ id: 1, title: "Cocktail1", ingredients: ["I1", "I2"], description: "HOW TO DO IT", glass: "coupe" },
				{ id: 2, title: "Cocktail2", ingredients: ["I1", "I2", "I3"], description: "HOW TO DO IT GOOF", glass: "ballon" },
				{ id: 3, title: "Cocktail3", ingredients: ["I1", "I2", "I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "whiskey" },
				{ id: 4, title: "Cocktail3", ingredients: ["I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "shooter" },
				{ id: 5, title: "Cocktail3", ingredients: ["I2", "I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "biere" },
				{ id: 1, title: "Cocktail1", ingredients: ["I1", "I2"], description: "HOW TO DO IT", glass: "coupe" },
				{ id: 2, title: "Cocktail2", ingredients: ["I1", "I2", "I3"], description: "HOW TO DO IT GOOF", glass: "ballon" },
				{ id: 3, title: "Cocktail3", ingredients: ["I1", "I2", "I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "whiskey" },
				{ id: 4, title: "Cocktail3", ingredients: ["I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "shooter" },
				{ id: 5, title: "Cocktail3", ingredients: ["I2", "I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "biere" }
			],
			dataToShow:[],
			noMore: false
		}
	},
	mounted(){
		this.getMoreData();
		this.getNextCocktails();
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
		}
	}
}
</script>

<style>
ul {
	list-style-type: none;
}
</style>