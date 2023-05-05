<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <nav id="navBar" class="grid-container bg-dark">

    <router-link class="logo" to="/">LOGO</router-link>


    <router-link to="/" class="cocktail">
      <div> <img src="../assets/cocktail-svgrepo-com.svg" class="navbarIcon"></div>
      <div>Cocktails</div>
    </router-link>


    <router-link to="/cocktail-maker" class="shaker">
      <div> <img src="../assets/shaker.png" class="navbarIcon"></div>
      <div>Fait-moi un cocktail !</div>
    </router-link>


    <router-link to="/ingredients" class="ingredients">
      <div> <img src="../assets/ingredients.png" class="navbarIcon"></div>
      <div>Mes ingrédients</div>
    </router-link>


    <div v-if="!$auth0.loading" class="profil">
      <div v-if="!$auth0.loading">

        <a v-if="!$auth0.isAuthenticated" @click="login">Log in</a>

        <a v-if="$auth0.isAuthenticated" @click="logout">Log out</a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "TheNavBar",
  methods: {
    login() {
      this.$auth0.loginWithRedirect();
    },
    // Log the user out
    logout() {
      this.$auth0.logout({
        returnTo: window.location.origin
      });
    }
  }
};
</script>

<style>
.navbarIcon {
  max-height: 3em;
}

.wide {
  width: 200%;
}

.bg-dark {
  background-color: var(--main-black) !important;
}

#navBar {
  box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
}

.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 2fr 2fr 2fr 1fr 1fr;
}

.logo {
  grid-column-start: 1;
  grid-column-end: 2;
}

.vide {
  grid-column-start: 2;
  grid-column-end: 3;
}

.cocktail {
  grid-column-start: 3;
  grid-column-end: 4;
}

.shaker {
  grid-column-start: 4;
  grid-column-end: 5;
}

.ingredients {
  grid-column-start: 5;
  grid-column-end: 6;
}

.profil {
  grid-column-start: 7;
  grid-column-end: 8;
}
</style>