import { createStore } from 'vuex'

export default createStore({
	state: {
		listeIngredients: [],
		listeIngredientsPerso: [],
	},
	getters: {
		allIngredients: state => { return state.listeIngredients },
		allIngredientsPerso: state => { return state.listeIngredientsPerso }
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
		}
	},
})
