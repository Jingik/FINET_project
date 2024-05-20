<template>
  <div>
    <div class="searchcontainer">
      <div class="checkbox-options">
        <label>
          <input type="checkbox" v-model="searchOptions" value="인터넷"> 인터넷
        </label>
        <label>
          <input type="checkbox" v-model="searchOptions" value="스마트폰"> 스마트폰
        </label>
        <label>
          <input type="checkbox" v-model="searchOptions" value="영업점"> 영업점
        </label>
        <label>
          <input type="checkbox" v-model="searchOptions" value="모집인"> 모집인
        </label>
      </div>
    </div>
    <div class="selectcontainer">
      <div class="select">
        <label for="sort">정렬방식: </label>
        <select id="sort" v-model="sortBy" @change="sortProducts">
          <option value="productNameAsc">가나다순</option>
          <option value="releaseDateDesc">최근 출시순</option>
        </select>
      </div>
    </div>
    <div class="container">
      <ul>
        <template v-if="filteredCreditLoans.length > 0">
          <li v-for="creditloan in filteredCreditLoans" :key="creditloan.id">
            <div class="card">
              <img :src="`/src/assets/img/${creditloan.kor_co_nm}.png`" alt="" class="creditloan-image">
              <div class="creditloan-info">
                <h2>{{ getProductName(creditloan.kor_co_nm) }} {{ getProductName(creditloan.fin_prdt_nm) }}</h2>
                <p>{{ getCreditLoanType(creditloan.crdt_prdt_type_nm) }}</p>
                <p>{{ creditloan.join_way }}</p>
              </div>
            </div>
          </li>
        </template>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

const creditLoans = ref([]);
const sortBy = ref('productNameAsc');
const searchOptions = ref([]);

const sortedCreditLoans = computed(() => {
  const sorted = [...creditLoans.value];
  if (sortBy.value === 'releaseDateDesc') {
    sorted.sort((a, b) => new Date(b.dcls_month) - new Date(a.dcls_month));
  } else if (sortBy.value === 'productNameAsc') {
    sorted.sort((a, b) => a.fin_prdt_nm.localeCompare(b.fin_prdt_nm));
  }
  return sorted;
});

const filteredCreditLoans = computed(() => {
  if (!searchOptions.value.length) return sortedCreditLoans.value;
  return sortedCreditLoans.value.filter(creditloan => {
    return searchOptions.value.some(option => creditloan.join_way.includes(option));
  });
});

async function fetchCreditLoans() {
  try {
    const res = await axios.get('http://127.0.0.1:8000/financial/creditloan-products/');
    creditLoans.value = res.data.filter(creditloan => {
      const targetBanks = ['신한은행', '우리은행', '하나은행', '농협은행주식회사', '국민은행', '중소기업은행'];
      return targetBanks.includes(creditloan.kor_co_nm);
    });
  } catch (error) {
    console.error('Error fetching products:', error);
  }
}

function sortProducts() {
  // This function is intentionally left empty as 'sortedCreditLoans' is reactive
}

function getProductName(productName) {
  if (productName.endsWith('고객')) {
    return productName + '전용';
  }
  return productName;
}

function getCreditLoanType(type) {
  switch (type) {
    case '1':
      return '일반신용대출';
    case '2':
      return '마이너스한도대출';
    case '3':
      return '장기카드대출(카드론)';
    default:
      return '';
  }
}

onMounted(() => {
  fetchCreditLoans();
});
</script>

<style scoped>
.searchcontainer {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  align-items: center;
  justify-content: center;
  margin: 50px auto;
  width: 1500px;
}

.container {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
}

.selectcontainer {
  margin-bottom: 20px;
  align-items: center;
  width: 100%;
}

.select {
  text-align: center;
  margin-bottom: 10px;
}

.card {
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin: 15px auto;
  width: 1400px;
  height: 100px;
}

.creditloan-image {
  margin-right: 10px;
}

.creditloan-info {
  flex: 1;
}

.creditloan-info h2 {
  font-weight: bold;
}
</style>
