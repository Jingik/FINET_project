<template>
  <MainBox />
  <div class="container">
    <LoginBox />
    <div class="bank">
      <MainBank />
    </div>
  </div>
</template>

<script setup>
import MainBox from '@/components/MainBoxComponent.vue'
import LoginBox from '@/components/LoginMainBoxComponent.vue'
import MainBank from '@/components/BankComponent.vue'
</script>

<style scoped>
html, body, #app {
  height: 100%;
  margin: 0;
  padding: 0;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  position: relative;
}

.bank {
  position: fixed;
  height: 100px;
  bottom: 100px; /* 아래 여백을 100px로 설정 */
  left: 0;
  width: 100%;
  justify-content: center;
  display: flex;
}
</style>
