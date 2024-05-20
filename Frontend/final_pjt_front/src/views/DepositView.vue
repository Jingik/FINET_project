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
        <input type="checkbox" v-model="searchOptions" value="전화(텔레뱅킹)"> 전화(텔레뱅킹)
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
      <!-- 전체 결과가 있는 경우 -->
      <template v-if="filteredProducts.length > 0">
        <li v-for="product in filteredProducts" :key="product.id">
          <div class="card">
            <img :src="`/src/assets/img/${product.kor_co_nm}.png`" alt="" class="product-image">
            <div class="product-info">
              <h2>{{ product.fin_prdt_nm }}</h2>
              <h3>{{ getProductBankName(product.kor_co_nm) }}</h3>
              <p>{{ product.join_way }}</p>
            </div>
          </div>
        </li>
      </template>
      <!-- 전체 결과가 없는 경우 -->
      <template v-else>
        <li v-for="product in products" :key="product.id">
          <div class="card">
            <img :src="`/src/assets/img/${product.kor_co_nm}.png`" alt="" class="product-image">
            <div class="product-info">
              <h2>{{ product.fin_prdt_nm }}</h2>
              <h3>{{ getProductBankName(product.kor_co_nm) }}</h3>
              <p>{{ product.join_way }}</p>
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

const products = ref([]);
const sortBy = ref('productNameAsc'); // Default sort by name ascending
const searchOptions = ref([]); // 배열로 변경

const sortedProducts = computed(() => {
  const sorted = [...products.value];
  if (sortBy.value === 'releaseDateDesc') {
    sorted.sort((a, b) => new Date(b.dcls_month) - new Date(a.dcls_month));
  } else if (sortBy.value === 'productNameAsc') {
    sorted.sort((a, b) => a.fin_prdt_nm.localeCompare(b.fin_prdt_nm));
  }
  return sorted;
});

const filteredProducts = computed(() => {
  if (!searchOptions.value.length) return sortedProducts.value;
  return sortedProducts.value.filter(product => {
    // OR 연산으로 필터링
    return searchOptions.value.some(option => product.join_way.includes(option));
  });
});

async function fetchProducts() {
  try {
    const res = await axios.get('http://127.0.0.1:8000/financial/deposit-products/');
    products.value = res.data.filter(product => {
      const targetBanks = ['신한은행', '우리은행', '하나은행', '농협은행주식회사', '국민은행', '중소기업은행'];
      return targetBanks.includes(product.kor_co_nm);
    });
  } catch (error) {
    console.error('Error fetching products:', error);
  }
}


function sortProducts() {
  // No need to do anything here since computed property 'sortedProducts' will react to changes in 'sortBy'
}

function getProductBankName(bankName) {
  switch (bankName) {
    case '농협은행주식회사':
      return '농협은행';
    case '중소기업은행':
      return '기업은행';
    default:
      return bankName;
  }
}

onMounted(() => {
  // 페이지가 로드될 때 자동으로 조회
  fetchProducts();
});
</script>


<style scoped>

.searchcontainer {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  align-items: center;
  justify-content: center;
  margin: 50px auto; /* 페이지의 가운데 정렬 */
  width: 1500px;
}
.container {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 20px; /* 각 container 사이에 간격 추가 */
  display: flex; /* 가로 정렬 */
  justify-content: space-between; /* 양쪽 정렬 */
}

.selectcontainer {
  margin-bottom: 20px; /* 각 container 사이에 간격 추가 */
  align-items: center; /* 수직 중앙 정렬 */
  width:100%;
}
.select {
  text-align: center;
  margin-bottom: 10px; /* 선택 박스와 카드 사이 간격 */
}

.card {
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px auto;
  margin: 15px auto;
  width: 1400px; /* 카드 너비를 100%로 설정하여 부모 컨테이너에 맞춤 */
  height: 100px;
}

.product-image {
  margin-right: 10px;
}

.product-info {
  flex: 1;
}

.product-info h2 {
  font-weight: bold;
}
</style>
