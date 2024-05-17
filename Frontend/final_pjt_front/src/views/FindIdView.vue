<template>
  <div class="id-find-container">
    <h2 class="login-find-title">FINET</h2>
    <h3 class="login-find-subtitle">아이디 찾기</h3>
    <form class="id-find-form" @submit.prevent="findUserId">
      <div class="form-group">
        <input type="text" id="name" name="name" v-model="name" placeholder="이름을 입력하세요" required>
      </div>
      <div class="form-group">
        <input type="email" id="email" name="email" v-model="email" placeholder="이메일 주소를 입력하세요" required>
      </div>
      <button type="submit" class="btn btn-primary">아이디 찾기</button>
    </form>
    <div class="password-find-link">
      <span>비밀번호를 잊으셨나요? </span><a href="#">비밀번호 찾기</a>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const name = ref('');
const email = ref('');
const userId = ref('');

async function findUserId() {
  try {
    const response = await axios.post('/api/find-user-id/', {
      name: name.value,
      email: email.value
    });
    userId.value = response.data.user_id;
  } catch (error) {
    console.error('Error finding user ID:', error);
  }
}
</script>

<style scoped>
.id-find-container {
  margin: 300px auto 0;
  max-width: 400px;
  padding: 40px;
  background-color: #fff;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.login-find-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  text-align: center;
}

.login-find-subtitle {
  font-size: 16px;
  color: #666;
  text-align: center;
}
.id-find-form .form-group {
  margin-bottom: 20px;
}

.id-find-form label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

.id-find-form input {
  width: 375px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.id-find-form .btn {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.password-find-link {
  margin-top: 20px;
  text-align: right;
}

.password-find-link a {
  color: #007bff;
  text-decoration: none;
}

.password-find-link a:hover {
  text-decoration: underline;
}
</style>