<template>
    <div id="authentication">
        <GoogleLogin :callback="callbackResponse" v-if="userData == null"/>
        <button v-on:click="logout" v-else>Se déconnecter</button>
    </div>
</template>

<script>
    import { decodeCredential, googleLogout } from 'vue3-google-login'

    let userData = null;

    export default {
        data () {
            return {
                connected: true
            }
        },
        methods: {
            callbackResponse(response) {
                console.log('login');
                // decodeCredential will retrive the JWT payload from the credential
                userData = decodeCredential(response.credential);
                console.log("Handle the userData", userData);
                this.connected = true;
            },
            logout() {
                console.log('logout');
                userData = null;
                googleLogout();
                console.log(userData);
                this.connected = false;
            },
            getUser() {
                return userData;
            }
        }
    }

    
</script>