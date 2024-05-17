import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import KakaoView from '@/views/KakaoView.vue'
import MainLoginView from '@/views/MainLoginView.vue'
import MainLogin from '@/components/LoginMainBoxComponent.vue'
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
      path: "/main",
      name: "MainLogin",
      component: MainLoginView
    },
    {
      path: "/box",
      name: "MainLogin2",
      component: MainLogin
    },

  ]
})


export default router
