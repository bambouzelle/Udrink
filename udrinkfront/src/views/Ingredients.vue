<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="container">
    <div class="row">
      <h1>Ingredients</h1>
    </div>
    <div class="row" style="margin-top:3em; margin-bottom: 3em;">
      <SearchBar />
    </div>
    <div v-for="ingredient in ingredients" class="row" :key="ingredient.id" style="margin-bottom: 1em;">
      <IngredientCard :ingredient="ingredient" />
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';
import IngredientCard from '@/components/IngredientCard.vue';

export default {
name: "IngredientsView",
components:{SearchBar, IngredientCard},
data(){
  return {
    ingredients:[
      {id:1, name:"i1", creation:1},
      {id:2, name:"i2", creation:0}
    ]
  }
}
}
</script>

<style>

</style>