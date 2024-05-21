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
      <template v-if="filteredProducts.length > 0">
        <p v-for="product in filteredProducts" :key="product.id">
          <div class="card">
            <img :src="`/src/assets/img/${product.kor_co_nm}.png`" alt="" class="product-image">
            <div class="product-info">
              <h2 v-html="formatProductName(product.fin_prdt_nm)"></h2>
              <h3>{{ getProductBankName(product.kor_co_nm) }}</h3>
              <p>{{ product.join_way }}</p>
              <div>
                <label for="term">기간 선택: </label>
                <select v-model="selectedTerms[product.id]" @change="updateInterestRate(product)">
                  <option v-for="option in uniqueTerms(product)" :key="option.save_trm" :value="option.save_trm">
                    {{ option.save_trm }}개월
                  </option>
                </select>
                <p v-if="selectedInterestRates[product.id]">금리: {{ selectedInterestRates[product.id] }}%</p>
              </div>
            </div>
            <img 
              :src="wishlist.includes(product.id) ? '/src/assets/img/filledheart.png' : '/src/assets/img/heart.png'" 
              class="wishlist-button" 
              @click="toggleWishlist(product.id)" 
              alt="wishlist icon">
            <button class="comparison-button" @click="addToComparison(product)">비교함 담기</button>
          </div>
        </p>
      </template>
      <template v-else>
        <li v-for="product in products" :key="product.id">
          <div class="card">
            <img :src="`/src/assets/img/${product.kor_co_nm}.png`" alt="" class="product-image">
            <div class="product-info">
              <h2>{{ product.fin_prdt_nm }}</h2>
              <h3>{{ getProductBankName(product.kor_co_nm) }}</h3>
              <p>{{ product.join_way }}</p>
              <div>
                <label for="term">기간 선택: </label>
                <select v-model="selectedTerms[product.id]" @change="updateInterestRate(product)">
                  <option v-for="option in uniqueTerms(product)" :key="option.save_trm" :value="option.save_trm">
                    {{ option.save_trm }}개월
                  </option>
                </select>
                <p v-if="selectedInterestRates[product.id]">금리: {{ selectedInterestRates[product.id] }}%</p>
              </div>
            </div>
            <img 
              :src="wishlist.includes(product.id) ? '/src/assets/img/filledheart.png' : '/src/assets/img/heart.png'" 
              class="wishlist-button" 
              @click="toggleWishlist(product.id)" 
              alt="wishlist icon">
            <button class="comparison-button" @click="addToComparison(product)">비교함 담기</button>
          </div>
        </li>
      </template>
    </div>
    <MyPageRemote />
  </div>
</template>


<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import MyPageRemote from '@/components/MyPageRemote.vue';

const products = ref([]);
const sortBy = ref('productNameAsc');
const searchOptions = ref([]);
const wishlist = ref([]);
const selectedTerms = ref({});
const selectedInterestRates = ref({});

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

    // Initialize selectedTerms with default value of 12 months
    products.value.forEach(product => {
      selectedTerms.value[product.id] = '12';
      updateInterestRate(product);  // Update interest rate based on the default term
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

function addToComparison(product) {
  console.log('비교함에 담기:', product);
}

function toggleWishlist(productId) {
  if (wishlist.value.includes(productId)) {
    wishlist.value = wishlist.value.filter(id => id !== productId);
  } else {
    wishlist.value.push(productId);
  }
}

function uniqueTerms(product) {
  const terms = product.deposit_options.map(option => option.save_trm);
  return [...new Set(terms)].map(term => ({
    save_trm: term,
    intr_rate: product.deposit_options.find(option => option.save_trm === term).intr_rate
  }));
}

function updateInterestRate(product) {
  const selectedTerm = selectedTerms.value[product.id];
  const selectedOption = product.deposit_options.find(option => option.save_trm === selectedTerm);
  if (selectedOption) {
    selectedInterestRates.value[product.id] = selectedOption.intr_rate;
  } else {
    selectedInterestRates.value[product.id] = null;
  }
}

function formatProductName(productName) {
  return productName.replace(/ *\([^)]*\) */g, '<br>');
}


onMounted(() => {
  fetchProducts();
});
</script>


<style scoped>
.searchcontainer {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  align-items: center;
  justify-content: center;
  margin: 50px auto;
  width: 90%; /* 너비를 90%로 설정하여 반응형으로 조정 */
  max-width: 1500px; /* 최대 너비를 설정 */
}

img {
  margin-right: 10px;
}

.container {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 20px;
  display: flex; /* Flexbox 레이아웃 사용 */
  flex-wrap: wrap; /* 내용이 넘치면 다음 줄로 감 */
  gap: 20px; /* 카드 간격 */
  justify-content: flex-start; /* 카드 왼쪽 정렬 */
}

.selectcontainer {
  margin-bottom: 20px;
  width: 100%;
  text-align: end;
}

.select {
  display: inline-block;
  text-align: center;
  margin-bottom: 10px;
}

.card {
  display: flex;
  flex-direction: column; /* 반응형으로 변경 */
  align-items: center;
  position: relative;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px; /* 패딩을 키움 */
  margin: 15px auto;
  width: 350px; /* 고정 너비 */
  height: 300px; /* 고정 높이 */
}

.product-image {
  width: 100px; /* 이미지 크기를 고정 */
  height: 100px; /* 이미지 크기를 고정 */
  margin-bottom: 10px; /* 반응형으로 이미지 아래 여백 추가 */
}

.product-info {
  flex: 1;
  text-align: center; /* 중앙 정렬 */
  overflow: hidden; /* 내용이 넘칠 경우 숨김 */
}

.product-info h2 {
  font-weight: bold;
  font-size: 1.5em; /* 글자 크기를 키움 */
}

button {
  padding: 10px 20px; /* 버튼 크기를 키움 */
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-top: 10px; /* 버튼 위에 여백 추가 */
}

button:hover {
  background-color: #ddd;
}

.wishlist-button {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 30px; /* 버튼 크기를 키움 */
  height: 30px; /* 버튼 크기를 키움 */
  cursor: pointer;
}

.comparison-button {
  position: absolute;
  bottom: 10px;
  right: 10px;
}

.options {
  margin-top: 10px;
}

.options p {
  margin: 5px 0;
}

@media (min-width: 768px) {
  .card {
    flex-direction: column; /* 카드도 세로 방향으로 변경 */
    align-items: center;
  }

  .product-info {
    text-align: center; /* 텍스트를 중앙 정렬 */
  }
}

@media (max-width: 767px) {
  .wishlist-button,
  .comparison-button {
    position: static; /* 작은 화면에서는 버튼의 위치를 고정하지 않음 */
    margin-top: 10px; /* 버튼 위에 여백 추가 */
  }
}
</style>

