import { createApp } from 'vue';
import { createPinia } from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate';
import App from './App.vue';
import router from './router';
import "@/assets/global.css";
import "@/assets/styleguide.css";
import axios from 'axios';

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

const app = createApp(App);

// Axios 요청 인터셉터 추가
axios.interceptors.request.use(
  config => {
    const token = localStorage.getItem('auth_token');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    return config;
  },
  error => Promise.reject(error)
);

app.use(pinia);
app.use(router);
app.mount('#app');
