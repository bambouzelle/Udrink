<template>
  <div class="ajouteur">
    <input v-model="name" placeholder="ajouter un ingrédient" class="inputAdd" />
    <button type='button' class="addButton" @click="addIngredient()">
      <p>+</p>
    </button>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      name: ""
    }
  },
  methods: {
    addIngredient() {
      console.log('ingredinet added')
      if (this.name != "") {
        let ingredient = { id: null, name: this.name, creation: 1 }
        this.$store.dispatch('addIngredient', ingredient)
      }
      this.name = ''
    }
  },

}
</script>

<style scoped>

p{
  color: #f58a07;
  text-size-adjust: var(--main-orange);
  font-size:1.5em;
}
.ajouteur {
  display: grid;
  grid-template-columns: 10fr 1fr;
}

.inputAdd {
  border-radius: 30px;
  box-shadow: var(--main-purple) 4px 4px 0 0;
  max-width: 100%;
}

.addButton{
		width: 3em;
		height : 3em;
		border-radius: 50%;
		z-index: 33;
		margin-left:-3em;
    background-color: var(--main-brown);
	}
</style>