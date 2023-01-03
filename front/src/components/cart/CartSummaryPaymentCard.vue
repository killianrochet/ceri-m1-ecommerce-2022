<template>
    <div class="cart-item-card">
        <h3>Coût total : {{ cart_total.toFixed(2) }}€</h3>

        <button class="view-product-button">Payer avec une carte de crédit</button>
    </div>
</template>

<script>
    export default {
        computed: {
            cart_total() {
                return this.$store.getters.cartTotal
            }
        }
    }
</script>