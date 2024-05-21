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
        <template v-if="filteredSavings.length > 0">
          <li v-for="saving in filteredSavings" :key="saving.id">
            <div class="card">
              <img :src="`/src/assets/img/${saving.kor_co_nm}.png`" alt="" class="saving-image">
              <div class="saving-info">
                <h2>{{ saving.fin_prdt_nm }}</h2>
                <h3>{{ getProductBankName(saving.kor_co_nm) }}</h3>
                <p>{{ saving.join_way }}</p>
              </div>
              <img 
                :src="wishlist.includes(saving.id) ? '/src/assets/img/filledheart.png' : '/src/assets/img/heart.png'" 
                class="wishlist-button" 
                @click="toggleWishlist(saving.id)" 
                alt="wishlist icon">
              <button class="comparison-button" @click="addToComparison(saving)">비교함담기</button>
            </div>
          </li>
        </template>
        <template v-else>
          <li v-for="saving in savings" :key="saving.id">
            <div class="card">
              <img :src="`/src/assets/img/${saving.kor_co_nm}.png`" alt="" class="saving-image">
              <div class="saving-info">
                <h2>{{ saving.fin_prdt_nm }}</h2>
                <h3>{{ getProductBankName(saving.kor_co_nm) }}</h3>
                <p>{{ saving.join_way }}</p>
              </div>
              <img 
                :src="wishlist.includes(saving.id) ? '/src/assets/img/filledheart.png' : '/src/assets/img/heart.png'" 
                class="wishlist-button" 
                @click="toggleWishlist(saving.id)" 
                alt="wishlist icon">
                <button class="comparison-button" @click="addToComparison(saving)">비교함담기</button>
            </div>
          </li>
        </template>
      </ul>
    </div>
    <MyPageRemote />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import MyPageRemote from '@/components/MyPageRemote.vue';

const savings = ref([]);
const sortBy = ref('productNameAsc');
const searchOptions = ref([]);
const wishlist = ref([]);
const comparisonList = ref([]);

const sortedSavings = computed(() => {
  const sorted = [...savings.value];
  if (sortBy.value === 'releaseDateDesc') {
    sorted.sort((a, b) => new Date(b.dcls_month) - new Date(a.dcls_month));
  } else if (sortBy.value === 'productNameAsc') {
    sorted.sort((a, b) => a.fin_prdt_nm.localeCompare(b.fin_prdt_nm));
  }
  return sorted;
});

const filteredSavings = computed(() => {
  if (!searchOptions.value.length) return sortedSavings.value;
  return sortedSavings.value.filter(saving => {
    return searchOptions.value.some(option => saving.join_way.includes(option));
  });
});

async function fetchSavings() {
  try {
    const res = await axios.get('http://127.0.0.1:8000/financial/saving-products/');
    savings.value = res.data.filter(saving => {
      const targetBanks = ['신한은행', '우리은행', '하나은행', '농협은행주식회사', '국민은행', '중소기업은행'];
      return targetBanks.includes(saving.kor_co_nm);
    });
  } catch (error) {
    console.error('Error fetching products:', error);
  }
}

function sortProducts() {
  // This function is intentionally left empty as 'sortedSavings' is reactive
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

function toggleWishlist(savingId) {
  if (wishlist.value.includes(savingId)) {
    wishlist.value = wishlist.value.filter(id => id !== savingId);
  } else {
    wishlist.value.push(savingId);
  }
}

function addToComparison(saving) {
  if (!comparisonList.value.includes(saving)) {
    comparisonList.value.push(saving);
  }
}

onMounted(() => {
  fetchSavings();
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
  align-items: center;
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
  align-items: center;
  justify-content: space-between;
  position: relative;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 15px auto;
  width: 1400px;
  height: 100px;
}

.saving-image {
  margin-right: 10px;
}

.saving-info {
  flex: 1;
}

.saving-info h2 {
  font-weight: bold;
}

button {
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button:hover {
  background-color: #ddd;
}

.wishlist-button {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}

.comparison-button {
  position: absolute;
  bottom: 10px;
  right: 10px;
}
</style>
