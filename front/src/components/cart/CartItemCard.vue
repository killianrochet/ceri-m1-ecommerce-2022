<template>
    <div class="cart-item-card">
        <div class="header">
            <h3>{{ product.name }}</h3>
            <h4>Artiste : {{ product.author }}</h4>
            <h4>Dans le panier : {{ product.quantity }}</h4>
            <h4>Prix total : {{ item_cost.toFixed(2) }}</h4>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['product'],
        computed: {
            item_cost() {
                return this.product.price * this.product.quantity;
            }
        }
    }
</script>

<style lang="scss">
    .cart-item-card {
        width: 90%;
        margin: 5%;
        background-color: gray;
        box-shadow: 0 0 5px orange;
        border-radius: 5px;
        padding: 10px;
        text-align: left;

        .header {
            display: flex;
            justify-content: space-around;
        }
    }
</style>