<template>
    <div class="card">
        <h3>{{ product.name }}</h3>

        <h5 class="price">Prix: {{ product.price.toFixed(2) }}€</h5>
        <p class="author">Auteur: {{ product.author }}</p>
        <p class="text-muted">{{product.category }}</p>
        <button class="view-product-button" @click="$emit('view-product', product)">Détails</button>
    </div>
</template>

<script>
    export default {
        props: ['product'],
        computed: {
            description() {
                return this.product.description.substring(0, 150)
            }
        }
    }
</script>

<style lang="scss">
    .card {
        width: 80%;
        margin: 10%;
        padding: 10px;
        border-radius: 5px;
        background-color: gray;
        box-shadow: 0 0 5px orange;

        .h5.price {
            color: #282828;
        }

        p.text-muted {
            color: #282828;
        }
    }

    button.view-product-button {
        padding: 10px;
        background-color: orange;
        border: none;
        color: white;
        font-weight: bold;
        font-size: 1.15rem;
        border-radius: 5px;
        cursor: pointer;
    }
</style>