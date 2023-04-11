import { createStore } from 'vuex'

export default createStore({
	state: {
		listeIngredients: []
	},
	getters: {
		all: state => { return state.listeIngredients },
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
	},
	mutations: {
		addIngredient(state, ingredient) {
			console.log('adddddddd inger')
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
		}
	},
})
