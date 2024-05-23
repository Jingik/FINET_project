<template>
  <div class="mypage-container">
    <div class="mypage">
      <div class="sidemenu">
        <RouterLink :to="{ name: 'DashBoardPage' }">
          <div class="sidemenu-item1">FINET 보드</div>
        </RouterLink>
        <RouterLink :to="{ name: 'ProfilePage' }">
          <div class="sidemenu-item1">내 활동 로그</div>
        </RouterLink>
        <RouterLink :to="{ name: 'EditProfilePage' }">
          <div class="sidemenu-item1">내 정보 수정</div>
        </RouterLink>
        <RouterLink :to="{ name: 'RecommendPage' }">
          <div class="sidemenu-item3">내 맞춤 상품</div>
        </RouterLink>
      </div>
      <div class="bigcontainer">
        <div class="larger">
          <div class="smallcontainer">
            <span>
              <img src="@/assets/img/user.png" alt="interest" />
              <h2>내 기본 정보</h2>
              <div class="toggles">
              <button @click="fetchRecommendations('recommend_rating')">Rating</button>
              <button @click="fetchRecommendations('recommend_dot')">Dot</button>
              <button @click="fetchRecommendations('recommend_count')">Count</button>
            </div>
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
                <label for="assets">자 산</label>
                <div id="assets">{{ userProfile.asset }}</div>
              </div>

            </div>

          </div>
          <div class="smallcontainer">
            <span>
              <img src="@/assets/img/deposit.png" alt="interest" />
              <h2>추천 예금 상품</h2>
            </span>
            <hr />
            <div class="cards">
              <div
                v-for="product in recommendations.deposit_recommendations.slice(0, 3)"
                :key="product.id"
                class="card"
              >
                <p>
                  {{ product.fin_prdt_nm }}
                  <span class="bank-name">{{ product.kor_co_nm }}</span>
                </p>
              </div>
              <p v-if="recommendations.deposit_recommendations.length === 0">
                관심 상품이 없습니다.
              </p>
            </div>
          </div>
        </div>
        <div class="larger">
          <div class="smallcontainer">
            <span>
              <img src="@/assets/img/saving.png" alt="interest" />
              <h2>추천 적금 상품</h2>
            </span>
            <hr />
            <div class="cards">
              <div
                v-for="product in recommendations.saving_recommendations.slice(0, 3)"
                :key="product.id"
                class="card"
              >
                <p>
                  {{ product.fin_prdt_nm }}
                  <span class="bank-name">{{ product.kor_co_nm }}</span>
                </p>
              </div>
              <p v-if="recommendations.saving_recommendations.length === 0">
                관심 상품이 없습니다.
              </p>
            </div>
          </div>
          <div class="smallcontainer">
            <span>
              <img src="@/assets/img/loan.png" alt="interest" />
              <h2>추천 대출 상품</h2>
            </span>
            <hr />
            <div class="cards">
              <div
                v-for="product in recommendations.creditloan_recommendations.slice(0, 3)"
                :key="product.id"
                class="card"
              >
                <p>
                  {{ product.fin_prdt_nm }}
                  <span class="bank-name">{{ product.kor_co_nm }}</span>
                </p>
              </div>
              <p v-if="recommendations.creditloan_recommendations.length === 0">
                관심 상품이 없습니다.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();
const token = computed(() => userStore.token);
const userProfile = reactive({
  username: '',
  phone_number: '',
  user_age_group: '',
  service_purpose: '',
  email: '',
  asset: '',
});
const recommendations = reactive({
  deposit_recommendations: [],
  saving_recommendations: [],
  creditloan_recommendations: [],
});
const error = ref(null);

onMounted(async () => {
  await fetchUserProfile();
  await fetchRecommendations('recommend_rating'); // 기본 값은 rating으로 설정
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

const fetchRecommendations = async (type) => {
  let url;
  let requestData = {};

  if (type === 'recommend_rating') {
    url = 'http://127.0.0.1:8000/financial/recommend_rating/';
    requestData = {
      user_age_group: userProfile.user_age_group,
      asset: userProfile.asset,
    };
  } else if (type === 'recommend_count') {
    url = 'http://127.0.0.1:8000/financial/recommend_count/';
  } else if (type === 'recommend_dot') {
    url = 'http://127.0.0.1:8000/financial/recommend_dot/';
    requestData = {
      user_age_group: userProfile.user_age_group,
      asset: userProfile.asset,
      service_purpose: userProfile.service_purpose
    };
  }

  try {
    let response;
    if (type === 'recommend_count') {
      response = await axios.get(url, {
        headers: { Authorization: `Bearer ${token.value}` }
      });
    } else {
      response = await axios.post(url, requestData, {
        headers: { Authorization: `Bearer ${token.value}` }
      });
    }

    recommendations.deposit_recommendations = response.data.deposit_recommendations;
    recommendations.saving_recommendations = response.data.saving_recommendations;
    recommendations.creditloan_recommendations = response.data.creditloan_recommendations;
    error.value = null;
  } catch (err) {
    console.error("Error fetching recommendations:", err);
    recommendations.deposit_recommendations = [];
    recommendations.saving_recommendations = [];
    recommendations.creditloan_recommendations = [];
    error.value = err.response?.data?.error || 'An error occurred';
  }
};
</script>

<style>
.mypage-container {
  margin: 0 auto;
  align-items: center;
  justify-content: center;
  padding: 20px;
  width: 1920px;
  align-items: center;
  left: 50%;
}

.smallcontainer {
  height: 300px;
}

.mypage {
  margin: 60px auto;
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
  width: 10%;
}

.sidemenu-item1,
.sidemenu-item3 {
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  padding: 10px;
  margin-top: 20px;
  height: 50px;
  background-color: white;
  border-radius: 10px;
  transition: background-color 0.3s, transform 0.3s;
}

.sidemenu-item1:hover,
.sidemenu-item3:hover {
  background-color: #0284c7;
  color: white;
  transform: translateY(-2px);
}

.bigcontainer {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 90%;
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
  border-radius: 8px;
  transition: box-shadow 0.3s;
}

.card:hover {
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
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
  font-size: 1.5em;
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
  border: 1px solid #ccc;
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

.toggles {
  display: flex;
  justify-content: flex-end;
  margin-top: -40px; /* Adjust as needed to align with the heading */
}

.toggles button {
  background-color: #ffffff;
  border: 2px solid #0284c7;
  color: #0284c7;
  font-size: 14px;
  padding: 10px 20px;
  margin: 0 10px;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s, transform 0.3s;
}

.toggles button:hover {
  background-color: #0284c7;
  color: white;
  transform: translateY(-2px);
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