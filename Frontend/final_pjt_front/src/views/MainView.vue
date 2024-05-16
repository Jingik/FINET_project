<template>
  <div>
    <!-- <h1>Main Page</h1> -->
    <!-- <RouterLink :to="{ name: 'CreateView' }">
      [CREATE]
    </RouterLink> -->
    <Main />
  </div>
</template>

<script setup>
import Main from '@/components/MainVue.vue'
// Vue Router에서 RouterLink를 가져올 필요가 없습니다.
// import { RouterLink } from 'vue-router'

// onMounted 훅을 사용하여 데이터 로드 등의 작업을 수행할 수 있습니다.
// onMounted(() => {
//   store.getArticles()
// })

</script>

<style>
/* 필요한 스타일을 추가하세요 */
</style>
