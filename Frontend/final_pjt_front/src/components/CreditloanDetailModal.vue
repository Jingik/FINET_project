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
            <strong>이자 계산 방식:</strong> {{ selectedOption.crdt_lend_rate_type_nm }}
            <br>
            <strong>기본 금리:</strong> {{ selectedOption.crdt_grad_avg }}%
          </li>
          <li><strong>계좌 수 제한:</strong> {{ localSelectedProduct.spcl_cnd }}</li>
          <li><strong>최대 한도:</strong> {{ localSelectedProduct.max_limit ? localSelectedProduct.max_limit : '제한 없음' }}</li>
          <li><strong>가입 불가:</strong> 가입 가능</li>
          <li><strong>가입 대상:</strong> {{ localSelectedProduct.join_way }}</li>
          <li><strong>만기 후 이자율:</strong> {{ localSelectedProduct.mtrt_int }}</li>
          <li><strong>특별 조건:</strong> {{ localSelectedProduct.spcl_cnd }}</li>
        </ul>
        <div class="term-select">
          <label for="term-select">신용 등급 선택:</label>
          <select id="term-select" v-model="selectedTerm">
            <option v-for="term in uniqueTerms(localSelectedProduct)" :key="term" :value="term">{{ term }} 등급</option>
          </select>
        </div>
        <canvas ref="chartCanvas" width="400" height="200"></canvas>
        <button @click="subscribeProduct">상품 가입</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue';
import { Chart } from 'chart.js/auto';
import { useCounterStore } from '@/stores/counter'; // Adjust the path as necessary

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
  if (localSelectedProduct.value && localSelectedProduct.value.credit_loan_options) {
    return localSelectedProduct.value.credit_loan_options.find(option => option.save_trm === selectedTerm.value);
  }
  return null;
});

const rate12Months = computed(() => {
  if (localSelectedProduct.value && localSelectedProduct.value.credit_loan_options) {
    const option = localSelectedProduct.value.credit_loan_options.find(option => option.save_trm === "12");
    return option ? option.crdt_grad_avg : null;
  }
  return null;
});

const uniqueTerms = (product) => {
  if (product && product.credit_loan_options) {
    const terms = product.credit_loan_options.map(option => option.save_trm);
    return [...new Set(terms)].sort((a, b) => a - b);
  }
  return [];
};

watch(localSelectedProduct, (newProduct) => {
  if (newProduct && newProduct.credit_loan_options) {
    selectedTerm.value = newProduct.credit_loan_options[0]?.save_trm || null;
    renderChart();
  }
});

function renderChart() {
  if (chart.value) {
    chart.value.destroy();
  }
  if (localSelectedProduct.value && localSelectedProduct.value.credit_loan_options) {
    const terms = uniqueTerms(localSelectedProduct.value);
    const rates = terms.map(term => {
      const option = localSelectedProduct.value.credit_loan_options.find(option => option.save_trm === term);
      return option ? option.crdt_grad_avg : 0;
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

async function subscribeProduct() {
  try {
    const alreadySubscribed = await counterStore.isSubscribedToProduct(localSelectedProduct.value.id);
    if (alreadySubscribed) {
      alert('이미 가입된 상품입니다.');
      closeModal();
      return;
    }

    const response = await counterStore.subscribeToProduct(localSelectedProduct.value.id);
    alert('상품 가입이 성공적으로 완료되었습니다!');
    closeModal();
  } catch (error) {
    alert(`상품 가입에 실패했습니다: ${error.message}`);
    closeModal();
  }
}

onMounted(() => {
  renderChart();
});
</script>

<style scoped>
.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.5);
}

.modal-content {
  background-color: #fefefe;
  margin: 5% auto;
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
