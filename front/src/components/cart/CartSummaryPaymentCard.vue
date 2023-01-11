<template>
    <div class="cart-item-card">
        <h3>Coût total : {{ cart_total.toFixed(2) }}€</h3>

        <div>
            <button @click="showPopup = true">Payer</button>

            <MyPopup v-if="showPopup" :title="popupTitle" :message="popupMessage">
                <button @click="showPopup = false; validateCart()">Valider</button>
                <button @click="showPopup = false">Fermer</button>
            </MyPopup>
        </div>
    </div>
</template>

<script>
    import MyPopup from './MyPopup'
    import userData from './../authentication/AuthenticationDiv.vue'
    import axios from 'axios'

    

    export default {
        methods: {
            validateCart() {
                let cart = window.localStorage.getItem('cart');
                console.log(cart);
                axios
                    .post('http://127.0.0.1:8002/order/create', {
                        customer_name: "Thomas",
                        customer_address: "legrandt84@gmail.com",
                        customer_phone_number: '0614225061',
                        album_id: 1
                    },
                    {'Content-Type': 'application/json'}
                    )
                    .then(
                        function (response) {
                            window.localStorage.setItem('cart', []);
                            window.location.reload();
                        }
                    );
            }
        },
        components: {
            MyPopup
        },
        data() {
            return {
                showPopup: false,
                popupTitle: 'Confirmer le panier',
                popupMessage: 'Confirmez vous votre achat ? \nVotre panier sera vidé et vous serez redirigé sur notre partenaire de paiement.'
            }
        },
        computed: {
            cart_total() {
                return this.$store.getters.cartTotal
            }
        }
    }
</script>