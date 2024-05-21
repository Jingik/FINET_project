<!-- DepositDetailModal.vue -->

<template>
  <div class="modal" v-if="selectedProduct">
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>
      <h2>{{ selectedProduct.fin_prdt_nm }}</h2>
      <p><strong>은행:</strong> {{ selectedProduct.kor_co_nm }}</p>
      <p><strong>가입 방법:</strong> {{ selectedProduct.join_way }}</p>
      <p><strong>기간:</strong> {{ selectedTerm }} 개월</p>
      <p v-if="selectedOption">
        <strong>이자 계산 방식:</strong> {{ selectedOption.intr_rate_type }}
        <br>
        <strong>기본 금리:</strong> {{ selectedOption.intr_rate }}%
        <br>
        <strong>최고 금리:</strong> {{ selectedOption.intr_rate2 }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const selectedProduct = ref(null);
const selectedTerm = computed(() => selectedProduct.value ? selectedTerms.value[selectedProduct.value.id] : null);
const selectedOption = computed(() => {
  if (selectedProduct.value) {
    const term = selectedTerms.value[selectedProduct.value.id];
    return selectedProduct.value.deposit_options.find(option => option.save_trm === term);
  }
  return null;
});

function closeModal() {
  selectedProduct.value = null;
}
</script>

<style scoped>
.modal {
  display: none; /* 모달은 기본적으로 숨김 */
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.5); /* 투명한 배경색 */
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto; /* 모달을 화면 중앙에 위치시킴 */
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 600px;
  border-radius: 5px;
  position: relative;
}

.close {
  position: absolute;
  right: 10px;
  top: 5px;
  color: #aaa;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>
