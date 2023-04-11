<template>
	<div class="card mb-3 px-0" style="max-width: 100%;">
		<div class="row g-0">
			<h5 class="card-header">{{ cocktail.title }}</h5>
		</div>
		<div class="row g-0">
			<div class="col-md-9">
				<div class="card px-0 border-top-0 border-start-0 border-bottom-0 rounded-0">
					<div class="card-body">
						<ul>
							<li v-for="ing in cocktail.ingredients" :key="ing">- {{ ing }}</li>
						</ul>
					</div>
				</div>
			</div>
			<div class="col-md-3">
				<div class="card px-0 rounded-0 border-0">
					<div class="card-body">
						<img :src="(link)" style="max-height: 3em;">
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import cocktailGlass from "@/assets/glasses/cocktailGlass.svg";
import wineGlass from "@/assets/glasses/wineGlass.svg";
import whiskeyGlass from "@/assets/glasses/whiskeyGlass.svg";
import shotGlass from "@/assets/glasses/shotGlass.svg";
import beerGlass from "@/assets/glasses/beerGlass.svg";


export default {
	name:"CocktailCard",
	props:["cocktail"],
	data(){
		return {
			glassMap:{
				coupe:cocktailGlass,
				ballon:wineGlass,
				whiskey:whiskeyGlass,
				shooter:shotGlass,
				biere:beerGlass
			}
		}	
	},
	computed: {
		link(){
				return (this.glassMap[this.cocktail.glass])
		}
	}
}
</script>

<style></style>