<template>
  <div class="larger">
    <div class="smallcontainer">
      <span>
        <img src="@/assets/img/user.png" alt="interest">
        <h2>내 정보 수정</h2> {{ userProfile.username }}
      </span>
      <hr />
      <div class="content">
        <div class="margintop">
          <label for="phone_number">휴대폰 번호</label>
          <input type="tel" v-model.trim="userProfile.phone_number" id="phone_number" required>
          <button @click="handleSubmit" class="submit-button">수정완료</button>
        </div>
        <div class="margintop">
          <label for="password1">새 비밀번호</label>
          <input type="password" v-model.trim="password1" id="password1" required>
        </div>
        <div class="margintop">
          <label for="password2">새 비밀번호 재입력</label>
          <input type="password" v-model.trim="password2" id="password2" required>
          <button @click="handleSubmit" class="submit-button">수정완료</button>
        </div>
        <div v-if="passwordError" class="error-message">{{ passwordError }}</div>
        <div class="margintop">
          <label for="user_age_group">연령대</label>
          <select v-model="userProfile.user_age_group" id="user_age_group" required>
            <option value="10대">10대</option>
            <option value="20대">20대</option>
            <option value="30대">30대</option>
            <option value="40대">40대</option>
            <option value="50대">50대</option>
          </select>
          <button @click="handleSubmit" class="submit-button">수정완료</button>
        </div>
        <div class="margintop">
          <label for="service_purpose">서비스 목적</label>
          <select v-model="userProfile.service_purpose" id="service_purpose" required>
            <option value="예금 가입">예금 가입</option>
            <option value="적금 가입">적금 가입</option>
            <option value="대출 가입">대출 가입</option>
          </select>
          <button @click="handleSubmit" class="submit-button">수정완료</button>
        </div>
        <div class="margintop">
          <label for="email">이메일</label>
          <input type="email" v-model.trim="userProfile.email" id="email" required>
          <button @click="handleSubmit" class="submit-button">수정완료</button>
        </div>
        <div class="margintop">
          <label for="assets">자산</label>
          <input type="number" v-model.trim="userProfile.asset" id="assets" required>
          <button @click="handleSubmit" class="submit-button">수정완료</button>
        </div>
      </div>
      <transition name="fade">
        <div v-if="showToast" class="toast">수정이 완료되었습니다.</div>
      </transition>
    </div>
    <div class="smallcontainer">
      <span>
        <img src="@/assets/img/deposit.png" alt="interest">
        <h2>내 예금 상품</h2>
      </span>
      <hr />
      <div class="cards">
        <div v-for="subscription in subscribedProducts.deposits" :key="subscription.id" class="card">
          <p>{{ getProductById('deposits', subscription.deposit_product)?.fin_prdt_nm || "Unknown Product" }}
            <span class="bank-name">{{ getProductById('deposits', subscription.deposit_product)?.kor_co_nm }}</span>
          </p>
        </div>
        <p v-if="subscribedProducts.deposits.length === 0">관심 상품이 없습니다.</p>
      </div>
    </div>
  </div>
  <div class="larger">
    <div class="smallcontainer">
      <span>
        <img src="@/assets/img/saving.png" alt="interest">
        <h2>내 적금 상품</h2>
      </span>
      <hr />
      <div class="cards">
        <div v-for="subscription in subscribedProducts.savings" :key="subscription.id" class="card">
          <p>{{ getProductById('savings', subscription.saving_product)?.fin_prdt_nm || "Unknown Product" }}
            <span class="bank-name">{{ getProductById('savings', subscription.saving_product)?.kor_co_nm }}</span>
          </p>
        </div>
        <p v-if="subscribedProducts.savings.length === 0">관심 상품이 없습니다.</p>
      </div>
    </div>
    <div class="smallcontainer">
      <span>
        <img src="@/assets/img/loan.png" alt="interest">
        <h2>내 대출 상품</h2>
      </span>
      <hr />
      <div class="cards">
        <div v-for="subscription in subscribedProducts.creditloans" :key="subscription.id" class="card">
          <p>{{ getProductById('creditloans', subscription.creditloan_product)?.fin_prdt_nm || "Unknown Product" }}
            <span class="bank-name">{{ getProductById('creditloans', subscription.creditloan_product)?.kor_co_nm }}</span>
          </p>
        </div>
        <p v-if="subscribedProducts.creditloans.length === 0">관심 상품이 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();
const token = ref(userStore.token);
const userProfile = reactive({
  username: '',
  phone_number: '',
  user_age_group: '',
  service_purpose: '',
  email: '',
  asset: '',
});
const password1 = ref('');
const password2 = ref('');
const passwordError = ref('');
const showToast = ref(false);

const depositProducts = ref([]);
const savingProducts = ref([]);
const creditloanProducts = ref([]);
const subscribedProducts = reactive({
  deposits: [],
  savings: [],
  creditloans: []
});

onMounted(async () => {
  await fetchUserProfile();
  await fetchAllProducts();
  await fetchUserSubscriptions();
});

const fetchUserProfile = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/users/profile/${userStore.user}/`, {
      headers: { Authorization: `Token ${token.value}` },
    });
    console.log("Fetched user profile data:", response.data);
    Object.assign(userProfile, response.data.user_profile);
  } catch (error) {
    console.error("Error fetching user profile:", error);
  }
};

const fetchAllProducts = async () => {
  try {
    const depositResponse = await axios.get("http://127.0.0.1:8000/financial/deposit-products/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    depositProducts.value = depositResponse.data;

    const savingResponse = await axios.get("http://127.0.0.1:8000/financial/saving-products/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    savingProducts.value = savingResponse.data;

    const creditloanResponse = await axios.get("http://127.0.0.1:8000/financial/creditloan-products/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    creditloanProducts.value = creditloanResponse.data;
  } catch (error) {
    console.error("Error fetching products:", error);
  }
};

const fetchUserSubscriptions = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/financial/user_subscriptions/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    subscribedProducts.deposits = response.data.deposit_subscriptions;
    subscribedProducts.savings = response.data.saving_subscriptions;
    subscribedProducts.creditloans = response.data.creditloan_subscriptions;
  } catch (error) {
    console.error("Error fetching user subscriptions:", error);
  }
};

const getProductById = (type, productId) => {
  let productList;
  switch (type) {
    case 'deposits':
      productList = depositProducts.value;
      break;
    case 'savings':
      productList = savingProducts.value;
      break;
    case 'creditloans':
      productList = creditloanProducts.value;
      break;
    default:
      productList = [];
  }
  return productList.find(product => product.id === productId);
};

const handleSubmit = async () => {
  if (password1.value && password1.value !== password2.value) {
    passwordError.value = "Passwords do not match.";
    return;
  }
  passwordError.value = '';

  const updatedProfile = {
    phone_number: userProfile.phone_number,
    user_age_group: userProfile.user_age_group,
    service_purpose: userProfile.service_purpose,
    email: userProfile.email,
    asset: userProfile.asset,
  };

  if (password1.value) {
    updatedProfile.password = password1.value;
    updatedProfile.password_confirm = password2.value;
  }

  try {
    await axios.patch(`http://127.0.0.1:8000/users/profile/${userStore.user}/`, updatedProfile, {
      headers: { Authorization: `Token ${token.value}` }
    });
    showToast.value = true;
    setTimeout(() => {
      showToast.value = false;
    }, 3000);
  } catch (error) {
    console.error("Error updating profile:", error);
  }
};
</script>

<style scoped>
img {
  width: 30px;
  height: 30px;
}
.cards {
  display: flex;
  flex-wrap: wrap;
}

.card {
  background-color: #ffffff;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  padding: 10px;
  margin: 10px;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.bank-name {
  margin-left: auto;
  color: grey;
  font-size: 0.9em;
}

span {
  display: inline-flex;
  justify-content: center;
  align-items: center;
}

h2 {
  font-size: 1em;
  margin: auto 20px;
}

.larger {
  display: flex;
  flex-direction: row;
  height: 50%;
}
.smallcontainer {
  height: 90%;
  background-color: #ffffff;
  padding: 20px;
  margin: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  justify-items: center;
  width: 50%;
}

.content {
  font-size: 16px;
  padding: 5px;
  border-radius: 10px;
}

label {
  margin-right: 20px;
  font-size: 15px;
  width: 140px;
  text-align: right;
}

input,
select {
  height: 20px;
  width: 200px;
  margin-right: 10px;
}

.margintop {
  display: flex;
  padding: 5px;
  justify-content: left;
}

.submit-button {
  background-color: white;
  border: 2px solid #828282;
  color: black;
  font-size: 10px;
  cursor: pointer;
}

.submit-button:hover {
  text-decoration: underline;
}

.toast {
  position: fixed;
  bottom: 20%;
  left: 54%;
  transform: translateX(-50%);
  background-color: black;
  color: white;
  padding: 20px 30px;
  border-radius: 5px;
  opacity: 0.9;
  font-size: 1.2em;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
