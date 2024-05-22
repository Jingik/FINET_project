<template>
  <div class="content">
    <div class="searchcontainer">
      <div class="filter-container">
        <div class="filter-section">

          <div class="filter-title">[이자 계산 방식]</div>
          <div class="filter-row">
            <div class="checkbox-container">
              <input class="checkbox" type="checkbox" v-model="searchOptions" value="단리" />
              <label class="checkbox-label">단리</label>
            </div>
            <div class="checkbox-container">
              <input class="checkbox" type="checkbox" v-model="searchOptions" value="복리" />
              <label class="checkbox-label">복리</label>
            </div>
          </div>
          <div class="filter-title">[가입방법]</div>
          <div class="filter-row">
            <div class="checkbox-container">
              <input class="checkbox" type="checkbox" v-model="searchOptions" value="영업점" />
              <label class="checkbox-label">영업점</label>
            </div>
            <div class="checkbox-container">
              <input class="checkbox" type="checkbox" v-model="searchOptions" value="스마트폰" />
              <label class="checkbox-label">스마트폰</label>
            </div>
            <div class="checkbox-container">
              <input class="checkbox" type="checkbox" v-model="searchOptions" value="인터넷" />
              <label class="checkbox-label">인터넷</label>
            </div>
            <div class="checkbox-container">
              <input class="checkbox" type="checkbox" v-model="searchOptions" value="전화(텔레뱅킹)" />
              <label class="checkbox-label">전화(텔레뱅킹)</label>
            </div>
          </div>
          <div class="filter-title">[신용 등급 선택]</div>
          <div class="filter-options">
            <div class="filter-row">
              <div class="checkbox-container">
                <input class="checkbox" type="checkbox" v-model="searchOptions" value="1등급" />
                <label class="checkbox-label">1등급</label>
              </div>
              <div class="checkbox-container">
                <input class="checkbox" type="checkbox" v-model="searchOptions" value="4등급" />
                <label class="checkbox-label">4등급</label>
              </div>
              <div class="checkbox-container">
                <input class="checkbox" type="checkbox" v-model="searchOptions" value="5등급" />
                <label class="checkbox-label">5등급</label>
              </div>
              <div class="checkbox-container">
                <input class="checkbox" type="checkbox" v-model="searchOptions" value="6등급" />
                <label class="checkbox-label">6등급</label>
              </div>
              <div class="checkbox-container">
                <input class="checkbox" type="checkbox" v-model="searchOptions" value="10등급" />
                <label class="checkbox-label">10등급</label>
              </div>
              <div class="checkbox-container">
                <input class="checkbox" type="checkbox" v-model="searchOptions" value="11등급" />
                <label class="checkbox-label">11등급</label>
              </div>
              <div class="checkbox-container">
                <input class="checkbox" type="checkbox" v-model="searchOptions" value="12등급" />
                <label class="checkbox-label">12등급</label>
              </div>
              <div class="checkbox-container">
                <input class="checkbox" type="checkbox" v-model="searchOptions" value="13등급" />
                <label class="checkbox-label">13등급</label>
              </div>
            </div>
          </div>
        </div>
      </div>
      <CreditloanComparisonSection 
        :comparisonProducts="comparisonProducts" 
        @removeFromComparison="removeFromComparison"
        @compareProducts="showCreditloanComparisonModal = true"
      />
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
  </div>
  
  <!-- 상품 카드 목록 -->
  <div class="container">
    <template v-if="filteredProducts.length > 0">
      <p v-for="product in filteredProducts" :key="product.id">
        <div class="card">
          <img :src="`/src/assets/img/${product.kor_co_nm}.png`" alt="" class="product-image">
          <div class="product-info">
            <h2 v-html="formatProductName(product.fin_prdt_nm)" class="product-name"></h2>
            <h4>{{ getProductBankName(product.kor_co_nm) }}</h4>
            <p>{{ product.join_way }}</p>
            <div>
              <label for="grade">신용 등급 선택: </label>
              <select v-model="selectedGrades[product.id]" @change="updateInterestRate(product)">
                <option v-for="option in uniqueGrades(product)" :key="option" :value="option">
                  {{ option }}등급
                </option>
              </select>
              <br>
              <br>
              <p v-if="selectedInterestRates[product.id]" class="strong">기본금리 <span class="highlight">{{ selectedInterestRates[product.id] }}%</span></p>
            </div>
            <img 
              :src="wishlist.includes(product.id) ? '/src/assets/img/filledheart.png' : '/src/assets/img/heart.png'" 
              class="wishlist-button" 
              @click="toggleWishlist(product.id)" 
              alt="wishlist icon">
            <button class="comparison-button" @click="addToComparison(product)" :disabled="isInComparison(product.id)">비교함 담기</button>
          </div>
          <img 
          :src="wishlist.includes(product.id) ? '/src/assets/img/filledheart.png' : '/src/assets/img/heart.png'" 
          class="wishlist-button" 
          @click="toggleWishlist(product.id)" 
          alt="wishlist icon">
          <div class="align">
          <button class="detail-button" @click="openModal(product)">상세보기</button>
          <button class="comparison-button" @click="addToComparison(product)" :disabled="isInComparison(product.id)">비교함 담기</button>
        </div>
        </div>
      </p>
    </template>
    <template v-else>
      <p v-for="product in products" :key="product.id">
        <div class="card">
          <img :src="`/src/assets/img/${product.kor_co_nm}.png`" alt="" class="product-image">
          <div class="product-info">
            <h3 class="product-name">{{ product.fin_prdt_nm }}</h3>
            <h4>{{ getProductBankName(product.kor_co_nm) }}</h4>
            <p>{{ product.join_way }}</p>
            <div>
              <label for="grade">신용 등급 선택: </label>
              <select v-model="selectedGrades[product.id]" @change="updateInterestRate(product)">
                <option v-for="option in uniqueGrades(product)" :key="option" :value="option">
                  {{ option }}등급
                </option>
              </select>
              <br>
              <br>
              <p v-if="selectedInterestRates[product.id]" class="strong">기본금리 <span class="highlight">{{ selectedInterestRates[product.id] }}%</span></p>       
            </div>
            <img 
              :src="wishlist.includes(product.id) ? '/src/assets/img/filledheart.png' : '/src/assets/img/heart.png'" 
              class="wishlist-button" 
              @click="toggleWishlist(product.id)" 
              alt="wishlist icon">
            <button class="comparison-button" @click="addToComparison(product)" :disabled="isInComparison(product.id)">비교함 담기</button>
          </div>
          <img 
          :src="wishlist.includes(product.id) ? '/src/assets/img/filledheart.png' : '/src/assets/img/heart.png'" 
          class="wishlist-button" 
          @click="toggleWishlist(product.id)" 
          alt="wishlist icon">
          <div class="align">
          <button class="detail-button" @click="openModal(product)">상세보기</button>
          <button class="comparison-button" @click="addToComparison(product)" :disabled="isInComparison(product.id)">비교함 담기</button>
        </div>
        </div>
      </p>
    </template>
  </div>
  <MyPageRemote />
  <CreditloanComparisonModal 
    v-if="showCreditloanComparisonModal" 
    :comparisonProducts="comparisonProducts" 
    @close="showCreditloanComparisonModal = false"
  />
  <CreditloanDetailModal
    v-if="showCreditloanDetailModal"
    :selectedProduct="selectedProduct"
    @close="showCreditloanDetailModal = false"
  />
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import MyPageRemote from '@/components/MyPageRemote.vue';
import CreditloanComparisonSection from '@/components/CreditloanComparisonSection.vue';
import CreditloanComparisonModal from '@/components/CreditloanComparisonModal.vue';
import CreditloanDetailModal from '@/components/CreditloanDetailModal.vue';

const products = ref([]);
const selectedProduct = ref(null);
const sortBy = ref('productNameAsc');
const searchOptions = ref([]);
const wishlist = ref([]);
const selectedGrades = ref({});
const selectedInterestRates = ref({});
const comparisonProducts = ref([]);
const showCreditloanComparisonModal = ref(false);
const showCreditloanDetailModal = ref(false);

function openModal(product) {
  selectedProduct.value = product;
  showCreditloanDetailModal.value = true;
  console.log(selectedProduct.value);
}

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
    const res = await axios.get('http://127.0.0.1:8000/financial/creditloan-products/');
    products.value = res.data.filter(product => {
      const targetBanks = ['신한은행', '우리은행', '하나은행', '농협은행주식회사', '국민은행', '중소기업은행'];
      return targetBanks.includes(product.kor_co_nm);
    });

    // Initialize selectedGrades with default value of 1등급
    products.value.forEach(product => {
      selectedGrades.value[product.id] = '1';
      updateInterestRate(product);  // Update interest rate based on the default grade
    });

    const wishlistRes = await axios.get('http://127.0.0.1:8000/financial/favorites/');
    wishlist.value = wishlistRes.data.creditloan_subscriptions.map(item => item.creditloan_product);
  } catch (error) {
    console.error('Error fetching products:', error);
  }
}

function sortProducts() {
  // No need to do anything here since computed property 'sortedProducts' will react to changes in 'sortBy'
}

function toggleWishlist(productId) {
  if (wishlist.value.includes(productId)) {
    axios.post('http://127.0.0.1:8000/financial/favorites/remove_creditloan/', { creditloan_product_id: productId })
      .then(() => {
        wishlist.value = wishlist.value.filter(id => id !== productId);
      })
      .catch(error => {
        console.error('Error removing from wishlist:', error);
      });
  } else {
    axios.post('http://127.0.0.1:8000/financial/favorites/add_creditloan/', { creditloan_product_id: productId })
      .then(() => {
        wishlist.value.push(productId);
      })
      .catch(error => {
        console.error('Error adding to wishlist:', error);
      });
  }
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
  if (comparisonProducts.value.length < 5 && !isInComparison(product.id)) {
    comparisonProducts.value.push(product);
  }
}

function removeFromComparison(productId) {
  comparisonProducts.value = comparisonProducts.value.filter(product => product.id !== productId);
}

function isInComparison(productId) {
  return comparisonProducts.value.some(product => product.id === productId);
}


function uniqueGrades(product) {
  const grades = Object.keys(product.creditloan_options[0])
    .filter(key => key.startsWith('crdt_grad_') && product.creditloan_options[0][key] !== null)
    .map(key => key.split('_')[2]);
  return grades;
}

function updateInterestRate(product) {
  const selectedGrade = selectedGrades.value[product.id];
  const selectedOption = product.creditloan_options[0];
  if (selectedOption) {
    selectedInterestRates.value[product.id] = selectedOption[`crdt_grad_${selectedGrade}`];
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

<style src="@/assets/global.css"></style>
<style scoped>
.content {
  padding-top: 0px; /* Adjust to match the height of your header */
}

img {
  width:20px;
  height:20px;
}

.searchcontainer {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  align-items: center;
  justify-content: center;
  margin: 50px auto;
  width: 90%; /* 너비를 90%로 설정하여 반응형으로 조정 */
  max-width: 1500px; /* 최대 너비를 설정 */
}

.filter-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 20px;
}

.filter-title {
  width: 100%;
  font-weight: bold;
  margin-bottom: 10px;
}

.filter-options {
  display: flex;
  flex-wrap: wrap;
}

.filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.checkbox-container {
  display: flex;
  align-items: center;
  gap: 5px;
}

img {
  margin-right: 10px;
}

.container {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 0 auto 20px auto; /* 위, 아래는 20px, 좌우는 자동으로 가운데 정렬 */
  display: flex; /* Flexbox 레이아웃 사용 */
  flex-wrap: wrap; /* 내용이 넘치면 다음 줄로 감 */
  gap: 20px; /* 카드 간격 */
  justify-content: flex-start; /* 카드 왼쪽 정렬 */
  width: 80%; /* 너비를 90%로 설정하여 반응형으로 조정 */
}

.selectcontainer {
  margin-bottom: 20px;
  width: 85%;
  text-align: end;
}

.select {
  display: inline-block;
  text-align: center;
  margin-bottom: 10px;
}

.align {
  align-items: self-end;
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
  width: 360px; /* 고정 너비 */
  height: 360px; /* 고정 높이 */
}

.product-name {
  font-family: 'Arial', sans-serif; /* 원하는 글꼴 설정 */
  font-size: 1.5em; /* 글자 크기를 키움 */
  font-weight: bold;
}

.highlight {
  color: #393434;
  font-size: 30px;
  font-weight: bold;
}

.highlight2 {
  color: #005cac;
  font-size: 30px;
  font-weight: bold;
}

.strong {
  font-size: 15px;
}

.superstrong {
  font-size: 15px;
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

button {
  padding: 10px 20px; /* 버튼 크기를 키움 */
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-top: 10px; /* 버튼 위에 여백 추가 */
  margin-right : 10px;
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

.comparison-button .detail-button {
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
  .detail-button {
    position: static; /* 작은 화면에서는 버튼의 위치를 고정하지 않음 */
    margin-top: 10px; /* 버튼 위에 여백 추가 */
  }
}
</style>
