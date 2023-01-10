<template>
  <AuthenticationDiv/>

  <nav>
    <router-link to="/">Accueil</router-link> |
    <router-link to="/cart">Panier</router-link>
  </nav>
  
  <router-view/>
</template>

<script>
  import AuthenticationDiv from './components/authentication/AuthenticationDiv.vue'

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
