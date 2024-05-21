<template>
  <div class="modal-overlay" @click.self="close">
    <div class="modal">
      <h3>비교하기</h3>
      <table>
        <thead>
          <tr>
            <th>상품명</th>
            <th>은행명</th>
            <th>금리</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in comparisonProducts" :key="product.id">
            <td>{{ product.fin_prdt_nm }}</td>
            <td>{{ product.kor_co_nm }}</td>
            <td>{{ getInterestRate(product) }}%</td>
          </tr>
        </tbody>
      </table>
      <button @click="close">닫기</button>
    </div>
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

const emits = defineEmits(['close']);

function close() {
  emits('close');
}

function getInterestRate(product) {
  return product.deposit_options.find(option => option.save_trm === '12')?.intr_rate || 'N/A';
}
</script>

<style scoped>
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
}

.modal {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 80%;
  max-width: 600px;
}

table {
  width: 100%;
  border-collapse: collapse;
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
</style>
