<template>
    <div class="popup">
        <div class="popup-inner">
            <h2>{{ title }}</h2>
            <p>{{ message }}</p>
            <slot />
        </div>
    </div>
</template>
  
<script>
    import { ref } from 'vue';

    export default {
        setup() {
            const title = ref('Confirmer le panier');
            const message = ref('Confirmez vous votre achat ? \nVotre panier sera vidé et vous serez redirigé sur notre partenaire de paiement.');
        
            return {
                title,
                message
            }
        }
    } 
  </script>
<style lang="scss" scoped>
.popup {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 99;
    background-color: rgb(0, 0, 0, 0.2);

    display: flex;
    align-items: center;
    justify-content: center;

    .popup-inner {
        background: #FFF;
        padding: 32px;
        color: black;
    }
}
</style>