<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <nav class="navbar navbar-dark bg-dark">
    <div class='container-fluid'>
      <div class="row wide">
        <div class="col-2">
          <router-link class="navbar-brand" to="/">LOGO</router-link>
        </div>
        <div class="col-2">
          <router-link to="/">
            <div> <img src="../assets/cocktail-svgrepo-com.svg" class="navbarIcon"></div>
            <div>Cocktails</div>
          </router-link>
        </div>
        <div class="col-2">
          <router-link to="/cocktail-maker">
            <div> <img src="../assets/shaker.png" class="navbarIcon"></div>
            <div>Fait-moi un cocktail !</div>
          </router-link>
        </div>
        <div class="col-2">
          <router-link to="/ingredients">
            <div> <img src="../assets/ingredients.png" class="navbarIcon"></div>
            <div>Mes ingrédients</div>
          </router-link>
        </div>
        <div class="col-2" style="text-align: right;">
          <router-link to="/profil">
            <div> <img src="../assets/user.png" class="navbarIcon"></div>
            <div>Profil</div>
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar"
};
</script>

<style>
.navbarIcon {
  max-height: 3em;
}

.wide {
  width: 200%;
}
</style>