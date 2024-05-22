import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import MainLoginView from '@/views/MainLoginView.vue'
// 회원가입, 로그인
import LogInView from '@/views/LogInView.vue'
import FindIdView from '@/views/FindIdView.vue'
import SignUpView from '@/views/SignUpView.vue'
// 환전
import ExchangeView from '@/views/ExchangeView.vue'
// 금융상품 후기 게시판
import BoardView from '@/views/BoardView.vue'
import CreateView from '@/views/CreateView.vue'
import DetailView from '@/views/DetailView.vue'
import EditBoardView from '@/views/EditBoardView.vue'
// 지역 은행 찾기
import KakaoView from '@/views/KakaoView.vue'
//예적금 조회
import DepositView from '@/views/DepositView.vue'
import SavingsView from '@/views/SavingsView.vue'
import CreditloanView from '@/views/CreditloanView.vue'
//마이페이지
import MyPageView from '@/views/MyPageView.vue'
import EditProfilePage from '@/views/EditProfilePage.vue'
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
  },
  {
    path: '/posts',
    name: 'BoardView',
    component: BoardView
  },
  {
    path: '/posts/:id',
    name: 'DetailView',
    component: DetailView
  },
  {
    path: '/posts/create',
    name: 'CreateView',
    component: CreateView
  },
  {
    path: '/posts/:id/update',
    name: 'EditBoardView',
    component: EditBoardView
  },
  {
    path: '/deposit',
    name: 'DepositView',
    component: DepositView
  },

  {
    path: '/savings',
    name: 'SavingsView',
    component: SavingsView
  },
  {
    path: '/creditloan',
    name: 'CreditloanView',
    component: CreditloanView
  },
  {
    path: '/mypage',
    name: 'ProfilePage',
    component: MyPageView
  },
  {
    path: '/editprofile',
    name: 'EditProfilePage',
    component: EditProfilePage
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
