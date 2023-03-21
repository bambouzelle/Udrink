<template>
  <div id="page">
        <NavBar id="navbar"/>
        <LateralBar id="lateralBar"/>
        <router-view  id="centralZone"/>
  </div>
</template>
<script>
import NavBar from './components/TheNavbar.vue'
import LateralBar from './components/TheLateralBar.vue'

export default {
  components: {
    NavBar,
    LateralBar
  },
}
</script>

<style>
#app {
  font-family: "Golos Text", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: var(--main-black);
  background-color:var(--main-white);
}

#page{
  display: grid;
  grid-template-rows: 1fr 10fr;
  grid-template-columns:  2fr 8fr 2fr;
}

#navbar{
  grid-column-start: 1;
  grid-column-end: 5;
  grid-row-start: 1;
  grid-row-end: 2;
}

#lateralBar{
  grid-column-start: 1;
  grid-column-end: 1;
  grid-row-start: 2;
  grid-row-end: 3;
}

#centralZone{
  grid-row-start: 2;
  grid-row-end: 3;
  grid-column-start: 2;
  grid-column-end: 3;
}

nav a {
  padding: 30px;
  color: var(--main-white);
  text-decoration: none;
}

.textMenu{
  color: var(--main-white);
  text-decoration: none;
}

</style>
