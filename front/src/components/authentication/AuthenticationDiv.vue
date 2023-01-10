<template>
    <div id="authentication">
        <GoogleLogin :callback="callbackResponse" v-if="userData === null"/>
        <button v-on:click="logout" v-else>Se déconnecter</button>
    </div>
</template>

<script>
    import { decodeCredential, googleLogout } from 'vue3-google-login'

    export default {
        data () {
            return {
                connected: true,
                userData: null
            }
        },
        methods: {
            callbackResponse(response) {
                console.log('login');
                // decodeCredential will retrive the JWT payload from the credential
                this.userData = decodeCredential(response.credential);
                console.log("Handle the userData", this.userData);
                this.connected = true;
            },
            logout() {
                console.log('logout');
                this.userData = null;
                googleLogout();
                console.log(this.userData);
                this.connected = false;
            },
            getUser() {
                return this.userData;
            }
        }
    }    
</script>