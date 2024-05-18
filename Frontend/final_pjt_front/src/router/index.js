import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import KakaoView from '@/views/KakaoView.vue'
import MainLoginView from '@/views/MainLoginView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import FindIdView from '@/views/FindIdView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import { useUserStore } from '@/stores/user'

const routes = [
  { path: '/', name: 'MainView', component: MainView },
  { path: '/maps', name: 'maps', component: KakaoView },
  {
    path: '/main',
    name: 'MainLogin',
    component: MainLoginView,
    beforeEnter: (to, from) => {
      const userStore = useUserStore()
      if (!userStore.isLogin) {
        alert('로그인 후 이용 가능합니다.')
        return { name: 'LogInView' }
      }
    }
  },
  { path: '/users/signup', name: 'SignUpView', component: SignUpView },
  { path: '/users/login', name: 'LogInView', component: LogInView },
  { path: '/users/findid', name: 'FindIdView', component: FindIdView },
  { path: '/exchange', name: 'ExchangeView', component: ExchangeView },
  {
    path: '/mypage/:username*',
    // 아직 MyPage 구현 안되어 있음 우선 maps로 가게 구현
    // component: MyPageView,
    component: KakaoView,
    name: 'ProfilePage',
    beforeEnter: (to, from) => {
      const userStore = useUserStore()
      if (!userStore.isLogin) {
        alert('로그인 후 이용 가능합니다.')
        return { name: 'LogInView' }
      }
    }
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

// Uncomment and use the below code if you need global navigation guards
// router.beforeEach((to, from, next) => {
//   const store = useUserStore()
//   console.log('라우터 가드에서 isLogin 상태:', store.isLogin) // 디버깅 로그 추가

//   if (to.path === '/') {
//     if (!store.isLogin) {
//       next({ name: 'LogInView' })
//     } else {
//       next({ name: 'MainView' })
//     }
//   } else if (!store.isLogin && to.name !== 'LogInView' && to.name !== 'SignUpView') {
//     window.alert('로그인이 필요합니다!')
//     next({ name: 'LogInView' })
//   } else if (store.isLogin && (to.name === 'LogInView' || to.name === 'SignUpView')) {
//     window.alert('이미 로그인되었습니다.')
//     next({ name: 'MainLogin' })
//   } else {
//     next()
//   }
// })

export default router
