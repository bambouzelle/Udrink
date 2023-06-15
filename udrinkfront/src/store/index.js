import { createStore } from 'vuex'

export default createStore({
	state: {
		listeIngredients: [],
		listeIngredientsPerso: [],
		listeCocktails: []
	},
	getters: {
		allIngredients: state => { return state.listeIngredients },
		allIngredientsPerso: state => { return state.listeIngredientsPerso },
	},
	actions: {
		removeIngredient({ commit }, ingredient) {
			commit('removeIngredient', ingredient)
		},

		addIngredient({ commit }, ingredient) {
			commit('addIngredient', ingredient)
		},

		resetIngredients({ commit }) {
			commit('resetIngredients')
		},
		removeIngredientPerso({ commit }, ingredient) {
			commit('removeIngredientPerso', ingredient)
		},

		addIngredientPerso({ commit }, ingredient) {
			commit('addIngredientPerso', ingredient)
		},

		resetIngredientsPerso({ commit }) {
			commit('resetIngredientsPerso')
		},
		addCocktail({ commit }, cocktail) {
			commit('addCocktail', cocktail)
		},
		resetCocktails({ commit }) {
			commit('resetCocktails')
		},
	},
	mutations: {
		addIngredient(state, ingredient) {
			state.listeIngredients.push(ingredient)
		},
		removeIngredient(state, ingredient) {
			var index = state.listeIngredients.indexOf(ingredient);
			if (index > -1) {
				state.listeIngredients.splice(index, 1);
			}
		},

		resetIngredients(state) {
			state.listeIngredients = []
		},
		addIngredientPerso(state, ingredient) {
			state.listeIngredientsPerso.push(ingredient)
		},
		removeIngredientPerso(state, ingredient) {
			var index = state.listeIngredientsPerso.indexOf(ingredient);
			if (index > -1) {
				state.listeIngredientsPerso.splice(index, 1);
			}
		},

		resetIngredientsPerso(state) {
			state.listeIngredientsPerso = []
		},
		addCocktail(state, cocktail) {
			state.listeCocktails.push(cocktail)
		},
		resetCocktails(state) {
			state.listeCocktails = []
		},
	},
})
