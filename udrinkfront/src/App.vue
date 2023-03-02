<template>
  <NavBar />
  <LateralBar/>
  <router-view />
</template>

<script>
import NavBar from './components/Navbar.vue'
import LateralBar from './components/Lateralbar.vue'

export default {
  components: {
    NavBar,
    LateralBar
  }
}
</script>

<style>
#app {
  font-family: "Golos Text", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #001e1f;
}

nav a {
  padding: 30px;
  color: #dce0d9;
  text-decoration: none;
}

</style>
