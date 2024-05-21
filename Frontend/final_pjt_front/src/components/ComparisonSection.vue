<template>
  <div v-if="comparisonProducts.length > 0" class="comparison-container">
    <h3>비교함</h3>
    <div class="comparison-cards">
      <div v-for="product in comparisonProducts" :key="product.id" class="comparison-card">
        <img :src="`/src/assets/img/${product.kor_co_nm}.png`" alt="" class="product-image">
        <div class="product-info">
          <h2>{{ product.fin_prdt_nm }}</h2>
          <h3>{{ product.kor_co_nm }}</h3>
          <button @click="removeProduct(product.id)">제거</button>
        </div>
      </div>
    </div>
    <button class="compare-button" @click="compareProducts">비교하기</button>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  comparisonProducts: {
    type: Array,
    required: true,
  },
});

const emits = defineEmits(['removeFromComparison', 'compareProducts']);

function removeProduct(productId) {
  emits('removeFromComparison', productId);
}

function compareProducts() {
  emits('compareProducts');
}
</script>

<style scoped>
.comparison-container {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 20px;
}

.comparison-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.comparison-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  width: 200px;
}

.product-image {
  width: 100px;
  height: 100px;
}

.product-info {
  text-align: center;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button:hover {
  background-color: #ddd;
}

.compare-button {
  margin-top: 20px;
  padding: 10px 20px;
}
</style>
