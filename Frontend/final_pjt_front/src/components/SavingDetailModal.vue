<template>
  <div class="modal" v-if="localSelectedProduct">
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>
      <h2>{{ localSelectedProduct.fin_prdt_nm }}</h2>
      <p>개인의 필요시기, 목적자금에 맞춰 가입해봐요!</p>
      <div class="product-details">
        <img :src="`/src/assets/img/${localSelectedProduct.kor_co_nm}.png`" alt="" class="product-image">
        <ul>
          <li><strong>은행:</strong> {{ localSelectedProduct.kor_co_nm }}</li>
          <li><strong>계약기간:</strong> 최소 1개월, 최대 2년 이하</li>
          <li><strong>적금종류:</strong> 자유적립식</li>
          <li v-if="rate12Months">
            <strong>금리안내:</strong> <span class="highlight">{{ rate12Months }}% (세전, 연 12개월)</span>
          </li>
          <li v-if="selectedOption">
            <strong>이자 계산 방식:</strong> {{ selectedOption.intr_rate_type }}
            <br>
            <strong>기본 금리:</strong> {{ selectedOption.intr_rate }}%
            <br>
            <strong>최고 금리:</strong> {{ selectedOption.intr_rate2 }}%
          </li>
          <li><strong>계좌 수 제한:</strong> {{ localSelectedProduct.etc_note }}</li>
          <li><strong>최대 한도:</strong> {{ localSelectedProduct.max_limit ? localSelectedProduct.max_limit : '제한 없음' }}</li>
          <li><strong>가입 불가:</strong> {{ localSelectedProduct.join_deny ? '가입 불가' : '가입 가능' }}</li>
          <li><strong>가입 대상:</strong> {{ localSelectedProduct.join_member }}</li>
          <li><strong>만기 후 이자율:</strong> {{ localSelectedProduct.mtrt_int }}</li>
          <li><strong>특별 조건:</strong> {{ localSelectedProduct.spcl_cnd }}</li>
        </ul>
        <div class="term-select">
          <label for="term-select">가입 기간 선택:</label>
          <select id="term-select" v-model="selectedTerm">
            <option v-for="term in uniqueTerms(localSelectedProduct)" :key="term" :value="term">{{ term }} 개월</option>
          </select>
        </div>
        <canvas ref="chartCanvas" width="400" height="200"></canvas>
        <button @click="savingsubscribeToProduct">상품 가입</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue';
import { Chart } from 'chart.js/auto';
import { useCounterStore } from '@/stores/counter'; 

const props = defineProps({
  selectedProduct: {
    type: Object,
    required: true,
  }
});

const emit = defineEmits(['close']);
const counterStore = useCounterStore();

const localSelectedProduct = ref(props.selectedProduct);
const selectedTerm = ref(null);
const chart = ref(null);
const chartCanvas = ref(null);

const selectedOption = computed(() => {
  if (localSelectedProduct.value && localSelectedProduct.value.saving_options) {
    return localSelectedProduct.value.saving_options.find(option => option.save_trm === selectedTerm.value) || null;
  }
  return null;
});

const rate12Months = computed(() => {
  if (localSelectedProduct.value && localSelectedProduct.value.saving_options) {
    const option = localSelectedProduct.value.saving_options.find(option => option.save_trm === "12");
    return option ? option.intr_rate : null;
  }
  return null;
});

const uniqueTerms = (product) => {
  if (product && product.saving_options) {
    const terms = product.saving_options.map(option => option.save_trm);
    return [...new Set(terms)].sort((a, b) => a - b);
  }
  return [];
};

watch(localSelectedProduct, (newProduct) => {
  if (newProduct && newProduct.saving_options) {
    selectedTerm.value = newProduct.saving_options[0]?.save_trm || null;
    if (selectedTerm.value) {
      renderChart();
    }
  }
});

function renderChart() {
  if (chart.value) {
    chart.value.destroy();
  }
  if (localSelectedProduct.value && localSelectedProduct.value.saving_options) {
    const terms = uniqueTerms(localSelectedProduct.value);
    const rates = terms.map(term => {
      const option = localSelectedProduct.value.saving_options.find(option => option.save_trm === term);
      return option ? option.intr_rate : 0;
    });

    chart.value = new Chart(chartCanvas.value, {
      type: 'line',
      data: {
        labels: terms,
        datasets: [{
          label: 'Interest Rates by Term',
          data: rates,
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
          fill: false
        }]
      },
      options: {
        responsive: true,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Term (Months)'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Interest Rate (%)'
            },
            beginAtZero: true
          }
        }
      }
    });
  }
}

function closeModal() {
  emit('close');
}

async function savingsubscribeToProduct() {
  try {
    // const alreadySubscribed = await counterStore.savingisSubscribedToProduct(localSelectedProduct.value.id);
    // if (alreadySubscribed) {
    //   alert('이미 가입된 상품입니다.');
    //   closeModal();
    //   return;
    // }

    const response = await counterStore.savingsubscribeToProduct(localSelectedProduct.value.id);
    alert('상품 가입이 성공적으로 완료되었습니다!');
    closeModal();
  } catch (error) {
    alert(`상품 가입에 실패했습니다: ${error.message}`);
    closeModal();
  }
}

onMounted(() => {
  if (localSelectedProduct.value && localSelectedProduct.value.saving_options) {
    selectedTerm.value = localSelectedProduct.value.saving_options[0]?.save_trm || null;
    if (selectedTerm.value) {
      renderChart();
    }
  }
});
</script>

<style scoped>
.modal {
  display: block; /* 모달은 기본적으로 숨김 */
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
  margin: 5% auto; /* 모달을 화면 중앙에 위치시킴 */
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 800px;
  border-radius: 5px;
  position: relative;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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

h2 {
  margin-bottom: 10px;
  font-size: 24px;
  color: #007bff;
}

.product-details {
  margin-top: 20px;
}

.product-image {
  width: 100px;
  height: auto;
  margin-bottom: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 10px;
  font-size: 16px;
  line-height: 1.5;
}

strong {
  margin-right: 5px;
}

.highlight {
  color: red;
}

.term-select {
  margin-top: 20px;
}

.button-group {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
}

.button-group button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.button-group button:hover {
  background-color: #0056b3;
}

.selected-button {
  background-color: #0056b3;
}

canvas {
  margin-top: 20px;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
