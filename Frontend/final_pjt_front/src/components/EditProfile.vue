<template>
  <div class="larger">
  <div class="smallcontainer">
    <span>
      <img src="@/assets/img/user.png" alt="interest">
      <h2>내 정보 수정</h2>
    </span>
    <hr />
    <div class="content">
      <div class="margintop">
        <label for="phone_number">휴대폰 번호</label>
        {{ user_name }}
        <input type="tel" v-model.trim="phone_number" id="phone_number" required> <button @click="handleSubmit" class="submit-button">수정완료</button>
      </div>
      <div class="margintop">
        <label for="password1">새 비밀번호</label>
        <input type="password" v-model.trim="password1" id="password1" required>
      </div>
      <div class="margintop">
        <label for="password2">새 비밀번호 재입력</label>
        <input type="password" v-model.trim="password2" id="password2" required> <button @click="handleSubmit" class="submit-button">수정완료</button>
      </div>
      <div v-if="passwordError" class="error-message">{{ passwordError }}</div>
      <div class="margintop">
        <label for="user_age_group">연령대</label>
        <select v-model="user_age_group" id="user_age_group" required>
          <option value="10s">10대</option>
          <option value="20s">20대</option>
          <option value="30s">30대</option>
          <option value="40s">40대</option>
          <option value="50s">50대</option>
        </select>  <button @click="handleSubmit" class="submit-button">수정완료</button>
      </div>
      <div class="margintop">
        <label for="service_purpose">서비스 목적</label>
        <select v-model="service_purpose" id="service_purpose" required>  <button @click="handleSubmit" class="submit-button">수정완료</button>
          <option value="A">A</option>
          <option value="B">B</option>
          <option value="C">C</option>
        </select> <button @click="handleSubmit" class="submit-button">수정완료</button>
      </div>
      <div class="margintop">
        <label for="email">이메일</label>
        <input type="email" v-model.trim="email" id="email" required>  <button @click="handleSubmit" class="submit-button">수정완료</button>
      </div>
      <div class="margintop">
        <label for="assets">자산</label>
        <input type="number" v-model.trim="assets" id="assets" required> <button @click="handleSubmit" class="submit-button">수정완료</button>
      </div>
    </div>
    <transition name="fade">
      <div v-if="showToast" class="toast">수정이 완료되었습니다.</div>
    </transition>
  </div>
  <div class="smallcontainer">
    <span>
      <img src="@/assets/img/deposit.png" alt="interest">
      <h2> 내 예금 상품</h2>
    </span>
    <hr />
  </div>
</div>
<div class="larger">
  <div class="smallcontainer">
    <span>
      <img src="@/assets/img/saving.png" alt="interest">
      <h2> 내 적금 상품</h2>
    </span>
    <hr />  </div>  <div class="smallcontainer">
      <span>
      <img src="@/assets/img/loan.png" alt="interest">
      <h2> 내 대출 상품</h2>
    </span>
    <hr />  </div>
</div>
</template>
<script setup>
import { ref } from "vue";

const phone_number = ref('');
const name = ref('');
const password1 = ref('');
const password2 = ref('');
const user_age_group = ref('');
const service_purpose = ref('');
const email = ref('');
const assets = ref('');
const passwordError = ref('');
const showToast = ref(false);

const handleSubmit = () => {
  // 여기에 폼 제출 로직 추가
  showToast.value = true;
  setTimeout(() => {
    showToast.value = false;
  }, 1000); // 3초 후에 토스트 메시지를 숨깁니다.
};
</script>
<style scoped>
img {
  width: 30px;
  height: 30px;
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

.larger{
  display:flex;
  flex-direction: row;
  height:50%
}
.smallcontainer {
  height: 90%;
  background-color: #ffffff;
  padding: 20px;
  margin: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  justify-items: center;
  width:50%;
}

.content {
  font-size: 16px;
  padding: 5px;
  border-radius: 10px;
}

label {
  margin-right: 20px;
  font-size:15px;
  width : 140px;
  text-align: right;
}

input, select {
  height: 20px;
  width: 200px;
  margin-right : 10px;
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
  background-color: #black;
  color: white;
  padding: 20px 30px;
  border-radius: 5px;
  opacity: 0.9;
  font-size: 1.2em;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
