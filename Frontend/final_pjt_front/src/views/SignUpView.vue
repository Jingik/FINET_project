<template>
  <div id="signup-form">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="id">ID:</label>
        <input type="text" v-model.trim="id" id="id" required>
      </div>
      <div>
        <label for="phone">휴대폰 번호:</label>
        <input type="tel" v-model.trim="phone" id="phone" required>
      </div>
      <div>
        <label for="name">이름:</label>
        <input type="text" v-model.trim="name" id="name" required>
      </div>
      <div>
        <label for="password1">비밀번호:</label>
        <input type="password" v-model.trim="password1" id="password1" required>
      </div>
      <div>
        <label for="password2">비밀번호 재입력:</label>
        <input type="password" v-model.trim="password2" id="password2" required>
      </div>
      <div>
        <label for="age-group">나이 그룹:</label>
        <select v-model="ageGroup" id="age-group" required>
          <option value="10대">10대</option>
          <option value="20대">20대</option>
          <option value="30대">30대</option>
          <option value="40대">40대</option>
          <option value="50대">50대</option>
        </select>
      </div>
      <div>
        <label for="service-purpose">서비스 목적:</label>
        <select v-model="servicePurpose" id="service-purpose" required>
          <option value="A">A</option>
          <option value="B">B</option>
          <option value="C">C</option>
        </select>
      </div>
      <div>
        <label for="email">이메일:</label>
        <input type="email" v-model.trim="email" id="email" required>
      </div>
      <button type="submit">회원가입</button>
    </form>
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
