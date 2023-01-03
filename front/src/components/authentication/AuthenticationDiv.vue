<template>
    <div id="authentication">
    <GoogleLogin :callback="callbackResponse" prompt/>TEST
    <button v-on:click="logout">Déconnecter</button>
  </div>
</template>

<script>
    import { decodeCredential, googleLogout } from 'vue3-google-login'

    let userData;

    export default {
        methods: {
            callbackResponse(response) {
                console.log('test')
                // decodeCredential will retrive the JWT payload from the credential
                userData = decodeCredential(response.credential)
                console.log("Handle the userData", userData)
            },
            logout() {
                console.log(userData);
                console.log('logout');
                userData = null;
                googleLogout();
                console.log(userData);
            },
            getUser() {
                return userData;
            }
        }
    }

    
</script>