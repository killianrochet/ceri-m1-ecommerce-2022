<template>
  <nav>
    <router-link to="/">Accueil</router-link> |
    <router-link to="/cart">Panier</router-link>
  </nav>
  <AuthenticationDiv/>
  <router-view/>
</template>

<script>
  import AuthenticationDiv from './components/authentication/AuthenticationDiv.vue'

  // function decodeJwtResponse(token) {
  //   let base64Url = token.split('.')[1]
  //   let base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  //   let jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
  //       return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  //   }).join(''));
  //   return JSON.parse(jsonPayload)
  // }


  // let responsePayload;
  // console.log(responsePayload);
  // window.handleCalback = (response) => {
  //   responsePayload = callbackResponse(response.credential);
  // }

  // let responsePayload;
  // console.log(responsePayload);
  // window.handleCredentialResponse = (response) => {
  //   // decodeJwtResponse() is a custom function defined by you
  //   // to decode the credential response.
  //   responsePayload = decodeJwtResponse(response.credential);

  //   console.log("ID: " + responsePayload.sub);
  //   console.log('Full Name: ' + responsePayload.name);
  //   console.log('Given Name: ' + responsePayload.given_name);
  //   console.log('Family Name: ' + responsePayload.family_name);
  //   console.log("Image URL: " + responsePayload.picture);
  //   console.log("Email: " + responsePayload.email);
  // }

  export default {
    components: {
      AuthenticationDiv
    },
    mounted() {
      this.$store.commit('updateCartFromLocalStorage'); // Changed commit to dispatch
    }
  };
</script>

<style lang="scss">
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: white;
  }

  html, body {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
  }

  body {
    background-color: #282828;
  }

  nav {
    padding: 10px;
    width: 100%;
    height: 30px;
    background-color: #404040;
    line-height: 30px;

    a {
      font-weight: bold;
      color: white;
      text-decoration: none;
      margin: 0 5px 0 5px;
      font-size: 1.25rem;

      &.router-link-exact-active {
        color: orange;
        text-decoration: underline;
      }
    }
  }

  .text-center {
    text-align: center;
  }
</style>
