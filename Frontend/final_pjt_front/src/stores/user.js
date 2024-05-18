import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';
import { useRouter } from 'vue-router';

export const useUserStore = defineStore('user', () => {
  const articles = ref([]);
  const API_URL = 'http://127.0.0.1:8000';
  const token = ref(localStorage.getItem('auth_token') || null);
  const isLogin = computed(() => !!token.value);
  const router = useRouter();

  const getArticles = async function () {
    try {
      const response = await axios.get(`${API_URL}/api/v1/articles/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      articles.value = response.data;
    } catch (error) {
      console.log(error);
    }
  };

  const signUp = async function (payload) {
    const { username, password1, password2 } = payload;

    try {
      const response = await axios.post(`${API_URL}/accounts/signup/`, {
        username, password1, password2
      });
      console.log('회원가입 성공!');
      const password = password1;
      await logIn({ username, password });
    } catch (error) {
      console.log(error);
    }
  };

  const logIn = async function (payload) {
    const { username, password } = payload;

    try {
      const response = await axios.post(`${API_URL}/accounts/login/`, { username, password });

      token.value = response.data.token;  // Assuming the response contains a field 'token'
      localStorage.setItem('auth_token', response.data.token);
      axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`;

      console.log('로그인 성공, 토큰:', token.value);  // 로그인 상태 확인
      console.log('isLogin:', isLogin.value);

      // 디버깅 로그 추가
      console.log('라우터로 이동 시도');
      router.push({ name: 'MainLogin' });
      console.log('라우터로 이동 완료');
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  const logOut = function () {
    token.value = null;
    localStorage.removeItem('auth_token');
    delete axios.defaults.headers.common['Authorization'];
    console.log('로그아웃 성공');
    router.push({ name: 'LogInView' });
  };

  return { articles, API_URL, getArticles, signUp, logIn, logOut, token, isLogin };
}, { persist: true });
