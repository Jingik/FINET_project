import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import KakaoView from '@/views/KakaoView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import FindIdView from '@/views/FindIdView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView
    },
    {
      path: "/maps",
      name: "maps",
      component: KakaoView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path:'/users/user_login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path:'/users/findid',
      name: 'FindIdView',
      component: FindIdView
    }

  ]
})

// import { useUserStore } from '@/stores/user'


// router.beforeEach((to, from) => {
//   const store = useUserStore()
//   // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
//   if (to.name === 'ArticleView' && store.isLogin === false) {
//     window.alert('로그인이 필요해요!!')
//     return { name: 'LogInView' }
//   }

//   // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
//   if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
//     window.alert('이미 로그인 했습니다.')
//     return { name: 'ArticleView' }
//   }
// })

export default router
