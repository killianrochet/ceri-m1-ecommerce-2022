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
//import items from '../data/items.js'
import ProductSummaryCard from '../components/products/ProductSummaryCard.vue'
import ProductDetailsDrawer from '../components/products/ProductDetailsDrawer.vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    ProductSummaryCard,
    ProductDetailsDrawer
  },
  data () {
    return {
      items: [],
      product: null,
      active: {
        product_drawer: false
      }
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:8002/api/test', {
        headers: {
          'Access-Control-Allow-Origin': '*',
        }
      })
      .then(response => (this.items = response.data[0]))
    
    console.log(this.items)
  },
  methods: {
    viewProduct(product) {
      this.product = product
      this.active.product_drawer = true
      //console.log(this.product)
    },
    closeProductDrawer() {
      this.active.product_drawer = false;
    }
  }
}

</script>

<style lang="scss">
  .product-cards-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
</style>
