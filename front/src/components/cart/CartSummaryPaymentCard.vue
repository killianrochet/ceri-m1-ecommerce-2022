<template>
    <div class="cart-item-card">
        <h3>Coût total : {{ cart_total.toFixed(2) }}€</h3>

        <div>
            <button @click="showPopup = true">Afficher la popup</button>

            <MyPopup v-if="showPopup" :title="popupTitle" :message="popupMessage">
                <button @click="showPopup = false; emptyCart()">Valider</button>
                <button @click="showPopup = false">Fermer</button>
            </MyPopup>
        </div>
    </div>
</template>

<script>
    import MyPopup from './MyPopup'

    export default {
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
            emptyCart() {
                window.localStorage.setItem('cart', []);
                window.location.reload();
                return 1;
            },
            cart_total() {
                return this.$store.getters.cartTotal
            }
        }
    }
</script>