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
    <RouterLink :to="{ name: 'FindIdView' }">
      <div class="forgot-password">
        <span>계정을 잊으셨나요? </span>
        <span class="forgot-password-link">아이디/비밀번호 찾기</span>
      </div>
    </RouterLink>
    <Modal :show="showModal" title="로그인 실패" message="아이디 또는 비밀번호가 잘못되었습니다." @close="showModal = false" />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import Modal from '@/components/LoginModal.vue'
import { useUserStore } from '@/stores/user';

const username = ref('')
const password = ref('')
const showModal = ref(false)
const router = useRouter()
const userStore = useUserStore()

// Watchers to log the values of username and password
watch(username, (newVal) => {
  console.log('Username:', newVal)
})
watch(password, (newVal) => {
  console.log('Password:', newVal)
})

const logIn = async () => {
  console.log('Username before request:', username.value)
  console.log('Password before request:', password.value)
  try {
    console.log('Username request:', username.value)
    console.log('Password request:', password.value)
    const response = await axios.post('http://127.0.0.1:8000/users/login/', {
      username: username.value,
      password: password.value
    })
    // Handle successful login
    console.log(response.data)
    localStorage.setItem('auth_token', response.data.token)
    axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`
    userStore.token = response.data.token
    console.log('로그인 성공, 토큰:', userStore.token)
    console.log('isLogin:', userStore.isLogin)
    router.push({ name: 'MainLogin' })
  } catch (err) {
    showModal.value = true
    console.error(err)
  }
}

const onButton2Click = () => {
  router.push({ name: 'SignUpView' })
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
  padding: 60px; /* 패딩을 증가 */
  width: 600px; /* 너비를 증가 */
}

.login-header {
  text-align: center;
  margin-bottom: 32px;
}

.login-title {
  font-size: 32px; /* 폰트 크기 증가 */
  font-weight: bold;
  color: #333;
}

.login-subtitle {
  font-size: 20px; /* 폰트 크기 증가 */
  color: #666;
}

.form-group {
  margin-bottom: 24px; /* 간격 증가 */
}

.form-label {
  font-size: 18px; /* 폰트 크기 증가 */
  color: #666;
  margin-bottom: 12px; /* 간격 증가 */
}

.form-input {
  width: 100%; /* 입력 필드가 전체 너비를 차지하도록 설정 */
  padding: 16px; /* 패딩 증가 */
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 18px; /* 폰트 크기 증가 */
}

.form-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 32px; /* 간격 증가 */
}

.login-button,
.signup-button {
  flex: 1;
  padding: 16px 32px; /* 패딩 증가 */
  font-size: 18px; /* 폰트 크기 증가 */
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
  margin-top: 40px; /* 간격 증가 */
  text-align: center;
  position: relative;
  padding: 0 20px;
}

.social-title {
  font-size: 18px; /* 폰트 크기 증가 */
  color: #666;
  margin-bottom: 20px; /* 간격 증가 */
  position: relative;
  z-index: 1;
}

.social-buttons {
  display: flex;
  justify-content: center;
  gap: 24px; /* 간격 증가 */
  position: relative;
  z-index: 1;
}

.social-button {
  display: flex;
  align-items: center;
  background-color: #fff;
  border-radius: 4px;
  padding: 16px 32px; /* 패딩 증가 */
  cursor: pointer;
}

.social-icon {
  width: 32px; /* 아이콘 크기 증가 */
  height: 32px; /* 아이콘 크기 증가 */
  margin-right: 12px; /* 간격 증가 */
}

.social-label {
  font-size: 18px; /* 폰트 크기 증가 */
  color: #333;
}

.forgot-password {
  margin-top: 24px; /* 간격 증가 */
  text-align: center;
  font-size: 16px; /* 폰트 크기 증가 */
  color: #666;
}

.forgot-password-link {
  color: #007bff;
  cursor: pointer;
}

@media (max-width: 480px) {
  .login-frame {
    width: 90%;
    padding: 32px; /* 패딩 증가 */
  }
}
</style>