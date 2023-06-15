<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <h1 class="titre">Cocktails pouvant être réalisés avec vos ingrédients :</h1>
      </div>
    </div>
    <div v-show="filteredList.length != 0" v-for="cocktail in filteredList" class="row" :key="cocktail" style="margin-top: 2em;">
      <CocktailCard :cocktail="cocktail" />
    </div>
    <div v-show="filteredList.length == 0">
      <p>Pas de cocktails pouvant être réalisés avec vos ingrédients.</p>
    </div>
  </div>
</template>

<script>
import CocktailCard from "@/components/CocktailCard.vue"

export default {
  components: { CocktailCard },
  name: "CocktailMakerView",
  methods:{
    areArraysIdentical(array1, array2) {
      // Check if arrays have the same length
      if (array1.length !== array2.length) {
        return false;
      }

      // Sort the arrays to ensure elements are in the same order
      const sortedArray1 = array1.sort();
      const sortedArray2 = array2.sort();

      // Compare each element of the sorted arrays
      for (let i = 0; i < sortedArray1.length; i++) {
        if (sortedArray1[i] !== sortedArray2[i]) {
          return false;
        }
      }

      return true;
    }
  },
  computed: {
    filteredList() {
      if (this.$store.state.listeIngredientsPerso.length == 0) {
        return []
      }
      let coPo = []
      let nomIngredientsPerso = []
      this.$store.state.listeIngredientsPerso.forEach(ing => nomIngredientsPerso.push(ing.nom))
      this.$store.state.listeCocktails.forEach(element => {
        if (this.areArraysIdentical(JSON.parse(JSON.stringify(element)).ingredients, nomIngredientsPerso)) {
          coPo.push(element)
        }
      })
      return coPo
    },
  }
}
</script>

<style scoped>
.titre{
  margin-top: 2em;
}
</style>