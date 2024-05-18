import { createRouter, createWebHistory } from 'vue-router';
import MainView from '@/views/MainView.vue';
import KakaoView from '@/views/KakaoView.vue';
import MainLoginView from '@/views/MainLoginView.vue';
import LogInView from '@/views/LogInView.vue';
import SignUpView from '@/views/SignUpView.vue';
import FindIdView from '@/views/FindIdView.vue';
import ExchangeView from '@/views/ExchangeView.vue';
import { useUserStore } from '@/stores/user';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView,
    },
    {
      path: '/maps',
      name: 'maps',
      component: KakaoView,
    },
    {
      path: '/main',
      name: 'MainLogin',
      component: MainLoginView,
    },
    {
      path: '/users/signup',
      name: 'SignUpView',
      component: SignUpView,
    },
    {
      path: '/users/login',
      name: 'LogInView',
      component: LogInView,
    },
    {
      path: '/users/findid',
      name: 'FindIdView',
      component: FindIdView,
    },
    {
      path: '/exchange',
      name: 'ExchangeView',
      component: ExchangeView,
    },
  ],
});

router.beforeEach((to, from, next) => {
  const store = useUserStore();

  // 인증되지 않은 사용자는 보호된 페이지에 접근할 수 없음
  if (to.name === 'MainLogin' && !store.isLogin) {
    window.alert('로그인이 필요합니다!');
    next({ name: 'LogInView' });
  }
  // 인증된 사용자는 회원가입과 로그인 페이지에 접근할 수 없음
  else if ((to.name === 'SignUpView' || to.name === 'LogInView') && store.isLogin) {
    window.alert('이미 로그인되었습니다.');
    next({ name: 'MainView' });
  } 
  else {
    next();
  }
});

export default router;
