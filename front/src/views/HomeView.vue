<template>
  <div class="home">
    <ProductDetailsDrawer
    :product="product"
    :active="active.product_drawer"
    v-on:close-product-drawer="closeProductDrawer()"
    />
    <div class="product-cards-container">
      <ProductSummaryCard
        v-for="product in items"
        :key="product.id"
        :product="product"
        v-on:view-product="viewProduct($event)" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import items from '../data/items.js'
import ProductSummaryCard from '../components/products/ProductSummaryCard.vue'
import ProductDetailsDrawer from '../components/products/ProductDetailsDrawer.vue'

export default {
  name: 'HomeView',
  components: {
    ProductSummaryCard,
    ProductDetailsDrawer
  },
  data () {
    return {
      items: items,
      product: null,
      active: {
        product_drawer: false
      }
    }
  },
  methods: {
    viewProduct(product) {
      this.product = product
      this.active.product_drawer = true
      console.log(this.product)
    },
    closeProductDrawer() {
      this.active.product_drawer = false;
    }
  }
}
console.log(items)
</script>

<style lang="scss">
  .product-cards-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
</style>
