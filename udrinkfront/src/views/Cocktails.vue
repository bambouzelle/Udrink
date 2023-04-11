<!-- eslint-disable vue/multi-word-component-names -->
<template>
	<div class="container">
		<div class="row">
			<div class="col">
				<h1>Cocktails</h1>
			</div>
		</div>

		<div v-for="i in data" class="row" :key="i" style="margin-top: 4em;">
			<CocktailCard :cocktail="i"/>
		</div>
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
				{ id: 5, title: "Cocktail3", ingredients: ["I2", "I3", "I4"], description: "HOW TO DO IT GOOFyyy", glass: "biere" }
			]
		}
	}
}
</script>

<style>
ul {
	list-style-type: none;
}
</style>