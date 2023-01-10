<template>
    <div class="drawer-background"
    :class="{show: active}"
    @cick="$emit('close-product-drawer')">
    </div>

    <div class="drawer" :class="{show: active}">
        <div class="drawer-close" @click="$emit('close-product-drawer')">X</div>
        <div v-if="product" class="product-details">
            <h3 class="text-center">{{ product.name }}</h3>
            <img class="productImage" src="https://images.epagine.fr/910/0724384260910.jpg"/>

            <h4>Pistes :</h4>
            <ul>
                <li class="song" v-for="song in product.songs" :key="song.id">{{ song.name }} - {{ song.time }}</li> 
            </ul>
            <h3 class="text-center">{{ product.price.toFixed(2) }}€</h3>
        
            <div class="cart-total" v-if="product_total">
                <h3>Au panier</h3>
                <h4>{{ product_total }}</h4>
            </div>

            <div class="button-container">
                <button class="remove" @click="removeFromCart">Retirer</button>
                <button class="add" @click="addToCart">Ajouter</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['product', 'active'],
        methods: {
            addToCart() {
                this.$store.commit('addToCart', this.product)
            },
            removeFromCart() {
                this.$store.commit('removeFromCart', this.product)
            }
        },
        computed: {
            product_total() {
                return this.$store.getters.productQuantity(this.product)
            }
        }
    }
</script>

<style lang="scss">
.drawer-background {
    width: 100%;
    height: 100vh;position: fixed;
    left: 0;
    top: 0;
    background-color: rgba(124, 124, 124, 0.55);
    z-index: 100;
    display: none;
    transition: display .5s;

    &.show {
        display: block;
    }
}

.drawer {
    width: 95vw;
    height: 100vh;
    background-color: #282828;
    position: fixed;
    transition: left .5s;
    top: 0;
    left: -105vw;
    padding: 15px;
    z-index: 101;
    overflow-y: scroll;

    &.show {
        left: 0;
    }
}

.drawer-close {
    font-size: 1.5rem;
    padding: 5px;
    border-radius: 5px;
    right: 10px;
    border: 2px solid gray;
    color: gray;
    width: 15px;
    float: right;
    cursor: pointer;

    &:hover {
        background-color: lightgray;
    }
}

.product-details {
    display: flex;
    justify-content: center;
    flex-direction: column;

    li.song {
        padding: 20px;
        line-height: 1.5rem;
    }

    .button-container {
        button {
            width: 150px;
            border: none;
            padding: 10px;
            border-radius: 5px;
            margin: 0 5px 0 5px;
            cursor: pointer;
        }
    }
}

@media (min-width: 500px) {
    .drawer {
        width: 450px;
    }
}
</style>