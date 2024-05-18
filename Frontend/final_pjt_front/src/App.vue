<template>
  <div id="app">
    <div class="header">
    <NavigationHeader />
    </div>
    <div class="content">
      <RouterView />
    </div>
    <div class ="footer">
      <NavigationFooter />
    </div>
  </div>
</template>

<script setup>
import NavigationHeader from '@/components/NavigationHeader.vue'
import NavigationFooter from '@/components/NavigationFooter.vue'
import { RouterView } from 'vue-router'
</script>

<style src="@/assets/global.css"></style>
<style scoped>

.content {
  padding-top: 0px; /* Adjust to match the height of your header */
}
.footer {
  width: 83.33%; /* 화면 너비의 10/12를 차지 */
  margin: 0 auto; /* 중앙 정렬 */
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  /* gap: var(--gap-11xl); */
  max-width: 100%;
  text-align: left;
  font-size: var(--font-size-6xl);
  color: var(--color4);
  font-family: var(--small-text);
  position: relative; /* 수정: absolute에서 relative로 변경 */
}
</style>