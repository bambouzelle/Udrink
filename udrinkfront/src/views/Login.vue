<template>
  <div class='container' style='margin-top: 10%;'>
    <div class="row">
      <div class="col">
        <img class='icon' src="@/assets/cocktail-svgrepo-com.svg" style="height: 6em;">
      </div>
    </div>

    <div class="row">
      <div class="col">
        <h1 class='title'>Bienvenue</h1>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <p class='text-light'>Connectez vous à votre compte UDrink !</p>
      </div>
    </div>

    <div style='margin-top:20%;'>
      <div class="row">
        <div class="col-12 labels">
          <label class="text-regular" for="email">Adresse E-mail</label>
        </div>
        <div class='col-12'>
            <input class='input' id='email' type='email' name='email'>
        </div>
      </div>

      <div class="row">
        <div class="col-12 labels">
          <label class="text-regular" for="password">Mot de passe</label>
        </div>
        <div class='col-12' style='margin-left:-15%; width:103%;'>
          <input class='input' id='password' type='password' name='password'>
          <i @click='showPassword' class="far fa-eye" id="togglePassword" style='margin:-15%'></i>
        </div>
      </div>
    </div>

    <div class='row' style='margin-top:1.2em'>
      <div class='col-12'>
        <button class='button' type='submit'><router-link to='/DashBoard#goUp' style='color:#FFFFFF; font-style:normal;'>Connexion</router-link></button>
      </div>
    </div>
  
    <div class='row' style='margin-top:1.2em'>
      <div class='col-6'>
        <p>Mot de passe oublié ?</p>
      </div>
      <div class='col-6'>
        <router-link to='/create-account' style='textDecoration: none; color: black'>Créer un compte</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
	name: "LoginView",

  methods:{
    showPassword(){
      const passwordInput = document.getElementById('password');
      if (passwordInput.getAttribute("type") === "password") {
        passwordInput.setAttribute("type", "text");
      } else {
        passwordInput.setAttribute("type", "password");
      }
    }
  }
};
</script>

<style scoped>
  .icon {
    margin-top: 7%;
  }
  .title {
    color:#32A287;
    font-family:'Source Sans Pro', sans-serif;
    font-size: 280%;
    font-weight:600;
    line-height: 50px;
  }

  .labels{
    text-align: left;
    margin-left: 5%;
  }

  .input{
    box-shadow: 0px 0px 20px rgba(29, 40, 142, 0.07);
    -moz-box-shadow: 0px 0px 20px rgba(29, 40, 142, 0.07);
    -webkit-box-shadow: 0px 0px 20px rgba(29, 40, 142, 0.07);
    border:none;
    border-radius:10px;
    width:90%;
    margin:5%;
    height: 46px;

  }

  #togglePassword{
    margin-left: -15%; 
    cursor: pointer;
  }

  .button{
    box-shadow: 0px 0px 20px rgba(29, 40, 142, 0.05);
    -moz-box-shadow:0px 0px 20px rgba(29, 40, 142, 0.05);
    -webkit-box-shadow:0px 0px 20px rgba(29, 40, 142, 0.05);
    background-color: #32A287;
    color:aliceblue;
    border-radius:10px;
    width:90%;
    border: 1px solid #000000;
    box-sizing: border-box;
    height:55px;
  }
</style>
