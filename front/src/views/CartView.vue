<template>
    <div>
        <h1>Votre Panier</h1>

        <div v-for="product in items" :key="product.id">
            {{ product.name }}
        </div>
        <CartItemCard 
            v-for="product in products"
            :key="product.id"
            :product="product"
        />

        <CartSummaryPaymentCard
        />
    </div>
</template>

<script>
import CartItemCard from '../components/cart/CartItemCard.vue'
import CartSummaryPaymentCard from '../components/cart/CartSummaryPaymentCard.vue'

    export default {
        components: {
            CartItemCard,
            CartSummaryPaymentCard,
        },
        computed: {
            products() {
                return this.$store.getters.cartItems;
            }
        }
    }
</script>