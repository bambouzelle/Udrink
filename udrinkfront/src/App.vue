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
import AuthService from './auth/AuthService'
import axios from 'axios'
const API_URL = 'http://localhost:8000'

const auth = new AuthService()

export default {
  data () {
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })

    return {
      authenticated: false,
      message: ''
    }
  },

  components: {
    NavBar,
    LateralBar
  },
  mounted(){
    let a = document.getElementById('navbar').getBoundingClientRect().height;
    document.getElementById('navbar').style.height = a + "px";
    document.getElementById('lateralBar').style.marginBlockStart = a + 'px';
  },
  methods: {
    login () {
        auth.login()
      },
    handleAuthentication () {
      auth.handleAuthentication()
    },
    logout () {
      auth.logout()
    },
    privateMessage () {
      const url = `${API_URL}/api/private/`
      return axios.get(url, {headers: {Authorization: `Bearer ${auth.getAuthToken()}`}}).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    }
  }
}
</script>

<style>
body{
  background-color:var(--main-white);
}
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
  position:absolute;
  width: 100%;
}

#lateralBar{
  position:fixed;
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
  max-height: 2em;
}

</style>
