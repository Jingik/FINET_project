<template>
  <div class="login-container">
    <div class="login-frame">
      <div class="login-header">
        <h3 class="login-title">FINET</h3>
        <div class="login-subtitle">당신의 금융파트너, 피넷</div>
      </div>
      <div class="login-form">
        <form @submit.prevent="logIn">
          <div class="form-group">
            <label for="username" class="form-label">아이디</label>
            <input type="text" v-model.trim="username" id="username" class="form-input" placeholder="아이디를 입력하세요">
          </div>
          <div class="form-group">
            <label for="password" class="form-label">비밀번호</label>
            <input type="password" v-model.trim="password" id="password" class="form-input" placeholder="비밀번호를 입력하세요">
          </div>
          <div class="form-actions">
            <button type="submit" class="login-button">로그인</button>
          </div>
          <div class="form-actions">
            <button type="button" class="signup-button" @click="onButton2Click">회원가입</button>
          </div>
        </form>
      </div>
    </div>
    <div class="social-login">
      <div class="social-title">-간편 로그인-</div>
      <div class="social-buttons">
        <button class="social-button">
          <img class="social-icon" src="../assets/img/naverLoginLogo.png" alt="Naver">
          <div class="social-label">네이버 로그인</div>
        </button>
        <button class="social-button">
          <img class="social-icon" src="../assets/img/kakaoLoginLogo.png" alt="Kakao">
          <div class="social-label">카카오 로그인</div>
        </button>
      </div>
    </div>
    <RouterLink :to="{ name: 'FindIdView' }"><div class="forgot-password">
      <span>계정을 잊으셨나요? </span>
      <span class="forgot-password-link">아이디/비밀번호 찾기</span>
    </div></RouterLink>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { RouterView, RouterLink } from 'vue-router'


const username = ref(null)
const password = ref(null)
const store = useUserStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style scoped>  
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh; /* 부모 요소의 높이를 채우도록 함 */
  background-color: #ffffff;
  
}

.login-frame {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 40px;
  width: 400px;
}

.login-header {
  text-align: center;
  margin-bottom: 24px;
}

.login-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.login-subtitle {
  font-size: 16px;
  color: #666;
}

.form-group {
  margin-bottom: 16px;
}

.form-label {
  font-size: 14px;
  color: #666;
  margin-bottom: 8px;
}

.form-input {
  width: 375px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

.form-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 24px;
}

.login-button,
.signup-button {
  flex: 1;
  padding: 12px 24px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
}

.login-button {
  background-color: #007bff;
  color: #fff;
  border: none;
}

.signup-button {
  background-color: #f0f0f0;
  color: #333;
  border: none;
}

.social-login {
  margin-top: 32px;
  text-align: center;
  position: relative;
  padding: 0 20px;
}

.social-title {
  font-size: 16px;
  color: #666;
  margin-bottom: 16px;
  position: relative; /* 이 부분을 추가합니다 */
  z-index: 1; /* 이 부분을 추가합니다 */
}

.social-buttons {
  display: flex;
  justify-content: center;
  gap: 16px;
  position: relative; /* 이 부분을 추가합니다 */
  z-index: 1; /* 이 부분을 추가합니다 */
}

.social-button {
  display: flex;
  align-items: center;
  background-color: #fff;
  border-radius: 4px;
  padding: 12px 24px;
  cursor: pointer;
}

.social-icon {
  width: 24px;
  height: 24px;
  margin-right: 8px;
}

.social-label {
  font-size: 16px;
  color: #333;
}

.forgot-password {
  margin-top: 16px;
  text-align: center;
  font-size: 14px;
  color: #666;
}

.forgot-password-link {
  color: #007bff;
  cursor: pointer;
}

@media (max-width: 480px) {
  .login-frame {
    width: 90%;
    padding: 24px;
  }
}

</style>
