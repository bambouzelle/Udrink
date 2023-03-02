<template>
  <NavBar />
  <div class="container-fluid">
    <div class="row">
      <div class="col-3 px-0">
        <LateralBar />
      </div>
      <div class="col-6">
        <router-view />
      </div>
      <div class="col-3">
      </div>
    </div>
  </div>
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

.textMenu{
  color: #dce0d9;
  text-decoration: none;
}
</style>
