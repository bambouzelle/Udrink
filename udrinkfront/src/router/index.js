import { createRouter, createWebHistory } from 'vue-router'
import Cocktails from '../views/Cocktails.vue'
import CocktailMaker from '../views/CocktailMaker.vue'
import Ingredients from '../views/Ingredients.vue'
import Profil from '../views/Profil.vue'
import Login from '../views/Login.vue'



const routes = [
  {
    path: '/',
    name: 'cocktails',
    component: Cocktails
  },
  {
    path: '/cocktail-maker',
    name: 'cocktailMaker',
    component: CocktailMaker
  },
  {
    path: '/ingredients',
    name: 'ingredients',
    component: Ingredients
  },
    {
    path: '/profil',
    name: 'profil',
    component: Profil
  },
    {
    path: '/login',
    name: 'login',
    component: Login
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
