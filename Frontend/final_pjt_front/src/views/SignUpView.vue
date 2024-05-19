<template>
  <div class="signup-container">
    <div class="signup-frame">
      <div class="signup-header">
        <h1 class="signup-title">FINET</h1>
        <h2 class="signup-subtitle">회원가입</h2>
      </div>
      <div id="signup-form">
        <form @submit.prevent="signUp">
          <label for="username">ID</label>
          <div class="form-inline margintop">
            <input type="text" v-model.trim="username" id="username" required>
            <button class="idcheckbtn" type="button" @click="checkDuplicateUsername">중복확인</button>
          </div>
          <span v-if="isUsernameChecked && isDuplicateUsername" class="error-message">이미 사용 중인 아이디입니다.</span>
          <span v-if="isUsernameChecked && !isDuplicateUsername" class="success-message">사용할 수 있는 아이디입니다.</span>
          <div class="margintop">
            <label for="phone_number">휴대폰 번호</label>
            <input type="tel" v-model.trim="phone_number" id="phone_number" required>
          </div>
          <div class="margintop">
            <label for="name">이름</label>
            <input type="text" v-model.trim="name" id="name" required>
          </div>
          <div class="margintop">
            <label for="password1">비밀번호</label>
            <input type="password" v-model.trim="password1" id="password1" required>
          </div>
          <div class="margintop">
            <label for="password2">비밀번호 재입력</label>
            <input type="password" v-model.trim="password2" id="password2" required>
          </div>
          <div class="margintop">
            <label for="user_age_group">나이 그룹</label>
            <select v-model="user_age_group" id="user_age_group" required>
              <option value="10대">10대</option>
              <option value="20대">20대</option>
              <option value="30대">30대</option>
              <option value="40대">40대</option>
              <option value="50대">50대</option>
            </select>
          </div>
          <div class="margintop">
            <label for="service_purpose">서비스 목적</label>
            <select v-model="service_purpose" id="service_purpose" required>
              <option value="A">A</option>
              <option value="B">B</option>
              <option value="C">C</option>
            </select>
          </div>
          <div class="margintop">
            <label for="email">이메일</label>
            <input type="email" v-model.trim="email" id="email" required>
          </div>
          <div class="margintop">
            <label for="assets">자산</label>
            <input type="number" v-model.trim="assets" id="assets" required>
          </div>
          <button class="signupbtn" type="submit">회원가입</button>
        </form>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const username = ref(null)
const phone_number = ref(null)
const name = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const user_age_group = ref(null)
const service_purpose = ref(null)
const email = ref(null)
const assets = ref(null)

const isDuplicateUsername = ref(false)
const isUsernameChecked = ref(false)

const store = useUserStore()

const checkDuplicateUsername = async () => {
  // Here you should implement the actual logic to check for username duplication.
  // For example, make an API call to check if the username is taken.
  
  isUsernameChecked.value = true
  const response = await store.checkUsername(username.value) // Assume this method exists in your store
  isDuplicateUsername.value = response.isDuplicate
}

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    phone_number: phone_number.value,
    name: name.value,
    user_age_group: user_age_group.value,
    service_purpose: service_purpose.value,
    email: email.value,
    assets: assets.value
  }
  store.signUp(payload)
}
</script>


<style scoped>
.signup-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 80vh; /* 부모 요소의 높이를 채우도록 함 */
  background-color: #ffffff;
  
}

.signup-frame {
  background-color: #fff;
  border-radius: 8px;
  padding: 60px; /* 패딩을 증가 */
  width: 700px; /* 너비를 증가 */
  box-shadow:  0 2px 8px rgba(0, 0, 0, 0.1);

}

.signup-header {
  text-align: center;
  margin-bottom: 32px;
}

.signup-title {
  font-size: 32px; /* 폰트 크기 증가 */
  font-weight: bold;
  color: #333;
}

.signup-subtitle {
  font-size: 20px; /* 폰트 크기 증가 */
  color: #666;
}
  /* 전체 폼 스타일 */
  #signup-form {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
  }

  /* 폼 요소 스타일 */
  #signup-form input, #signup-form select {
    width: 100%;
    padding: 10px;
    /* margin-bottom: 10px; */
    border: 1px solid #ccc;
    border-radius: 3px;
    font-size: 16px;
  }

  .form-inline {
  display: flex;
  align-items: center;
  justify-items: center;
}

.form-inline label,
.form-inline input,
.form-inline button {
  margin-right: 10px;
}

.error-message {
  color: red;
  font-size: 14px;
}

.success-message {
  color: green;
  font-size: 14px;
  display: block;
  margin-top: 5px;
}
.signupbtn {
  margin-top: 30px;
  width: 100%; /* 버튼 너비를 100%로 설정 */
  font-size: 20px;
  height: 40px;
  background-color: #007bff; /* 파란색 계열 */
  color: white; /* 하얀 글씨 */
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.signupbtn:hover {
  background-color: #0056b3; /* 버튼 hover 시 darker blue */
}

.idcheckbtn {
  height: 40px; /* 버튼 높이를 40px로 설정 */
  width: 100px;
  background-color: #007bff; /* 파란색 계열 */
  color: white; /* 하얀 글씨 */
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.idcheckbtn:hover {
  background-color: #0056b3; /* 버튼 hover 시 darker blue */
}

.margintop{
  margin-top: 10px;
}
</style>
