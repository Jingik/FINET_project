<template>
  <div class="mypage-container">
    <div class="mypage">
      <div class="sidemenu">
      <RouterLink :to="{ name: 'DashBoardPage' }">
        <div class="sidemenu-item3">
          FINET 보드
        </div>
      </RouterLink>
        <RouterLink :to="{ name: 'ProfilePage' }">
        <div class="sidemenu-item3">
          내 활동 로그
        </div>
      </RouterLink>
      <RouterLink :to="{ name: 'EditProfilePage' }">
        <div class="sidemenu-item3">
          내 정보 수정
        </div>
      </RouterLink>
      <RouterLink :to="{ name: 'RecommendPage' }">
        <div class="sidemenu-item1">
          내 맞춤 상품
        </div>
      </RouterLink>
      </div>
      <div class="bigcontainer">  <div class="larger">
      <div class="smallcontainer">
        <span>
          <img src="@/assets/img/user.png" alt="interest">
          <h2>내 기본 정보</h2>
        </span>
        <hr />
<div class="content">
  <div class="margintop">
    <label for="user_age_group">연 령 대</label>
    <div id="user_age_group">{{ userProfile.user_age_group }}</div>
  </div>
  <div class="margintop">
    <label for="service_purpose">서비스 목적</label>
    <div id="service_purpose">{{ userProfile.service_purpose }}</div>
  </div>
  <div class="margintop">
    <label for="assets">자  산</label>
    <div id="assets">{{ userProfile.asset }}</div>
  </div>
</div>

        <!-- <transition name="fade">
          <div v-if="showToast" class="toast">수정이 완료되었습니다.</div>
        </transition> -->
      </div>
      <div class="smallcontainer">
        <span>
          <img src="@/assets/img/deposit.png" alt="interest">
          <h2>추천 예금 상품</h2>
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
          <h2>추천 적금 상품</h2>
        </span>
        <hr />
        <div class="cards">
          <p>내용내용</p>
        </div>
      </div>
      <div class="smallcontainer">
        <span>
          <img src="@/assets/img/loan.png" alt="interest">
          <h2>추천 대출 상품</h2>
        </span>
        <hr />
        <div class="cards">
          <p>내용내용</p>
        </div>
      </div>
    </div>
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
.mypage-container {
  margin : 0px auto;
  align-items: center;
  justify-content: center;
  padding: 20px;
  width: 1920px;
  align-items:center;
  left:50%
}
.smallcontainer{
  height:300px;
}

.mypage {
  margin : 60px auto;
  display: flex;
  flex-direction: row;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  background-color: #0599f1;
  height: 700px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  width: 1500px;
  margin-bottom: 20px;

}
.sidemenu {
  width:10%
}
.sidemenu-item1 {
  text-align: center;
  font-size: px;
  font-weight: bold;
  padding: 10px;
  margin-top: 20px;;
  height:50px;
  background-color: white;
  border-radius: 10px;
}
/* .sidemenu-item2 {
  font-size: 18px;
  box-shadow: 0 15px 30px 0 rgba(0, 0, 0, 0.2);
  text-align: center;
  font-weight: bold;
  padding: 10px;
  margin-top: 20px;;
  height:50px;
  background-color: white;
  border-radius: 10px;
} */

.sidemenu-item3 {
  font-size: 18px;
  box-shadow: 0 15px 30px 0 rgba(0, 0, 0, 0.2);
  text-align: center;
  font-weight: bold;
  padding: 10px;
  margin-top: 20px;;
  height:50px;
  background-color: white;
  border-radius: 10px;
}
.bigcontainer {
  display:flex;
  flex-direction: column;
  height:100%;
  width:90%;
}
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
  font-size: 15px;
  width: 100px;
  text-align: left;
  border:1px solid #ccc;
  text-align: center;
  border-radius: 10px;
  margin-right: 10px;
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
