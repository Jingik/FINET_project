import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';
import { useRouter } from 'vue-router';

export const useUserStore = defineStore('user', () => {
  const articles = ref([]);
  const API_URL = 'http://127.0.0.1:8000/users';  // 정확한 API URL 설정
  const token = ref(null)
  const isLogin = computed(() => !!token.value);
  const router = useRouter();

  // 토큰 초기화
  const clearToken = () => {
    token.value = null;
    localStorage.removeItem('auth_token');
    delete axios.defaults.headers.common['Authorization'];
  };

  // 회원가입
  const signUp = async (payload) => {
    const { username, password1, password2, phone_number, name, user_age_group, service_purpose, email, assets } = payload;

    try {
      const response = await axios.post(`${API_URL}/signup/`, {
        username,
        password: password1,
        password_confirm: password2,
        phone_number,
        name,
        user_age_group,
        service_purpose,
        email,
        assets
      });
      console.log('회원가입 성공!');
      await logIn({ username, password: password1 });
    } catch (error) {
      console.error('회원가입 실패:', error);
    }
  };

  // 로그인
  const logIn = async (payload) => {
    const { username, password } = payload;

    try {
      const response = await axios.post(`${API_URL}/login/`, { username, password });
      token.value = response.data.key
      console.log('로그인 성공, 토큰:', token.value);
      console.log('isLogin:', isLogin.value);
      router.push({ name: 'MainLogin' });
    } catch (error) {
      console.error('로그인 실패:', error);
    }
  };

  // 로그아웃
  const logOut = () => {
    clearToken();
    console.log('로그아웃 성공');
    router.push({ name: 'LogInView' });
  };

  // 사용자명 중복 확인
  const checkUsername = async (username) => {
    try {
      const response = await axios.get(`${API_URL}/id_check_exists/`, { params: { username } });
      return { isDuplicate: response.data.exists };
    } catch (error) {
      console.error('사용자명 중복 확인 실패:', error);
      return { isDuplicate: true };
    }
  };

  return {
    articles,
    API_URL,
    signUp,
    logIn,
    logOut,
    token,
    isLogin,
    checkUsername,
    clearToken
  };
}, {
  persist: true
});
