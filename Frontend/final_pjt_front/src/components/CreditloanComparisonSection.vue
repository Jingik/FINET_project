<template>
  <div v-if="comparisonProducts.length > 0" class="comparison-container">
    <div class="comparison-cards">
      <div v-for="product in comparisonProducts" :key="product.id" class="comparison-card">
        <div class="image-parent">
          <img class="image-icon" loading="lazy" alt="" :src="`/src/assets/img/${product.kor_co_nm}.png`" />
          <div class="product-details">
            <div class="bank-name">{{ product.kor_co_nm }}</div>
            <b class="product-name" v-html="formatProductName(product.fin_prdt_nm)"></b>
          </div>
        </div>
        <div class="interest-rates">
          <div class="rate-container">
            <div class="rate-label">최대금리</div>
            <b class="rate">{{ getMaxRate(product) }}%</b>
          </div>
          <div class="rate-container">
            <div class="rate-label">일반금리</div>
            <b class="rate">{{ getAvgRate(product) }}%</b>
          </div>
        </div>
        <button class="remove-button" @click="removeProduct(product.id)">제거</button>
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

function getMaxRate(product) {
  if (!product || !product.deposit_options) return 0;
  return Math.max(...product.deposit_options.map(option => option.intr_rate || 0));
}

function getAvgRate(product) {
  if (!product || !product.deposit_options) return 0;
  const rates = product.deposit_options.map(option => option.intr_rate || 0);
  return (rates.reduce((a, b) => a + b, 0) / rates.length).toFixed(2);
}

function formatProductName(productName) {
  return productName.replace(/ *\([^)]*\) */g, '<br>');
}
</script>

<style scoped>
.comparison-container {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 20px;
  margin-bottom: 20px;
}

.comparison-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.comparison-card {
  flex: 1;
  border-radius: 10px;
  background-color: #fff;
  border: 1px solid #000;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  padding: 10px;
  gap: 10px;
  text-align: left;
  font-size: 16px;
  color: #333;
  font-family: 'Inter', sans-serif;
  width: 158px; /* width 고정 */
  position: relative;
}

.image-parent {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  gap: 10px;
  position: relative;
  z-index: 0; /* Ensure this is at the lowest z-index */
}

.image-icon {
  height: 40px;
  width: 40px;
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
  object-fit: cover;
}

.bank-name {
  position: relative;
  font-size: 14px;
  color: #777;
  line-height: 24px;
  display: inline-block;
}

.product-name {
  position: relative;
  font-size: 18px;
  line-height: 24px;
  display: inline-block;
  color: #000;
}

.product-details {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 5px;
}

.interest-rates {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  gap: 20px;
  width: 100%;
}

.rate-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.rate-label {
  font-size: 12px;
  color: #777;
}

.rate {
  font-size: 14px;
  color: #007ace;
}

.remove-button {
  align-self: flex-end;
  padding: 5px 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f8f8f8;
  cursor: pointer;
}

.remove-button:hover {
  background-color: #ddd;
}

.compare-button {
  margin-top: 20px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007ace;
  color: white;
  cursor: pointer;
}

.compare-button:hover {
  background-color: #005cac;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000; /* 높은 z-index 값으로 설정하여 최상단에 위치 */
}

.modal {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 80%;
  max-width: 800px;
  overflow-y: auto;
  max-height: 90vh;
  position: relative; /* 추가 */
  z-index: 1001; /* 추가 */
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

th, td {
  padding: 10px;
  border: 1px solid #ccc;
  text-align: center;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button:hover {
  background-color: #ddd;
}

@media screen and (max-width: 900px) {
  .product-name {
    font-size: 16px;
    line-height: 20px;
  }

  .rate-label {
    font-size: 10px;
  }

  .rate {
    font-size: 12px;
  }
}

@media screen and (max-width: 450px) {
  .bank-name {
    font-size: 12px;
    line-height: 20px;
  }

  .product-name {
    font-size: 14px;
    line-height: 18px;
  }

  .image-parent {
    flex-wrap: wrap;
  }

  .rate-label {
    font-size: 10px;
  }

  .rate {
    font-size: 12px;
  }
}
</style>
