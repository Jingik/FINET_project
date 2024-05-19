import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';
import { useRouter } from 'vue-router';

export const useUserStore = defineStore('user', () => {
  const articles = ref([]);
  const API_URL = 'http://127.0.0.1:8000/users';  // 여기서 API URL을 정확하게 설정합니다.
  const token = ref(localStorage.getItem('auth_token') || null);
  const isLogin = computed(() => !!token.value);
  const router = useRouter();

  const getArticles = async function () {
    try {
      const response = await axios.get(`${API_URL}/api/v1/posts/`, {
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
    const { username, password1, password2, phone_number, name, user_age_group, service_purpose, email, assets } = payload;

    try {
      const response = await axios.post(`${API_URL}/signup/`, {
        username, password: password1, password_confirm: password2, phone_number, name, user_age_group, service_purpose, email, assets
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
      const response = await axios.post(`${API_URL}/login/`, { username, password });

      token.value = response.data.token;  // Assuming the response contains a field 'token'
      localStorage.setItem('auth_token', response.data.token);
      axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`;

      console.log('로그인 성공, 토큰:', token.value);  // 로그인 상태 확인
      console.log('isLogin:', isLogin.value);

      router.push({ name: 'MainLogin' });
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

  const checkUsername = async function (username) {
    try {
      const response = await axios.get(`${API_URL}/id_check_exists/`, { params: { username } });
      return { isDuplicate: response.data.exists };
    } catch (error) {
      console.error('Username check failed:', error);
      return { isDuplicate: true };
    }
  };

  return { articles, API_URL, getArticles, signUp, logIn, logOut, token, isLogin, checkUsername };
}, { persist: true });
