<template>
  <NavBar/>
  <div id="page" class="container-fluid" style="height: pageHeight">
    <div class="row">
      <div class="col-3 px-0">
        <LateralBar/>
      </div>
      <div class="col-7">
        <router-view />
      </div>
      <div class="col-2">
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
  },
  data(){
    return{
      navbarHeight:0
    }
  },
  mounted(){
    this.setHeight()
  },
  methods:{
    setHeight(){
      const element = document.querySelector('#page');
      const navbar = document.getElementById('navBar'); 
      const lateralbar = document.getElementById('lateralBar') 
      navbar.style.height = 12/100 * this.pageHeight+"px";   
      this.navbarHeight = Number(navbar.style.height.replace("px", ""));
      lateralbar.style.height = this.innerPageHeight+"px";
      element.style.height = this.innerPageHeight+"px";
    }
  },
  computed:{
    pageHeight(){
      var body = document.body,
      html = document.documentElement;
      var height = Math.max( body.scrollHeight, body.offsetHeight, 
                html.clientHeight, html.scrollHeight, html.offsetHeight );
      return (height);
    },
    innerPageHeight(){
      return this.pageHeight-this.navbarHeight;
    }
  }
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
