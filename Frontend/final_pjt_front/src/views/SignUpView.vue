<template>
  <div class="signup-container">
    <div class="signup-frame">
      <div class="signup-header">
        <h1 class="signup-title">FINET</h1>
        <h2 class="signup-subtitle">회원가입</h2>
      </div>
  <div id="signup-form">
    <form @submit.prevent="signUp">
      <div>
        <label for="username">ID:</label>
        <input type="text" v-model.trim="username" id="username" required>
      </div>
      <div>
        <label for="phone_number">휴대폰 번호</label>
        <input type="tel" v-model.trim="phone_number" id="phone_number" required>
      </div>
      <div>
        <label for="name">이름</label>
        <input type="text" v-model.trim="name" id="name" required>
      </div>
      <div>
        <label for="password1">비밀번호</label>
        <input type="password" v-model.trim="password1" id="password1" required>
      </div>
      <div>
        <label for="password2">비밀번호 재입력</label>
        <input type="password" v-model.trim="password2" id="password2" required>
      </div>
      <div>
        <label for="user_age_group">나이 그룹</label>
        <select v-model="user_age_group" id="user_age_group" required>
          <option value="10대">10대</option>
          <option value="20대">20대</option>
          <option value="30대">30대</option>
          <option value="40대">40대</option>
          <option value="50대">50대</option>
        </select>
      </div>
      <div>
        <label for="service_purpose">서비스 목적</label>
        <select v-model="service_purpose" id="service_purpose" required>
          <option value="A">A</option>
          <option value="B">B</option>
          <option value="C">C</option>
        </select>
      </div>
      <div>
        <label for="email">이메일</label>
        <input type="email" v-model.trim="email" id="email" required>
      </div>
      <div>
        <label for="assets">자산</label>
        <input type="number" v-model.trim="assets" id="assets" required>
      </div>
      <button type="submit">회원가입</button>
    </form>
  </div>
  </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const username = ref(null) 
const password1 = ref(null)
const password2 = ref(null)
const store = useUserStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

</script>

<style>
.signup-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 120vh; /* 부모 요소의 높이를 채우도록 함 */
  background-color: #ffffff;
}

.signup-frame {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 60px; /* 패딩을 증가 */
  width: 600px; /* 너비를 증가 */
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
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  /* 폼 요소 스타일 */
  #signup-form input, #signup-form select {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 3px;
    font-size: 16px;
  }

  /* 제출 버튼 스타일 */
  #signup-form button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    font-size: 16px;
  }

  #signup-form button:hover {
    background-color: #0056b3;
  }
</style>
