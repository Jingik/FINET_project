<template>

    <MainBox />
    <div class="container">
    <LoginBox />
  </div>
</template>

<script setup>
import MainBox from '@/components/MainBoxComponent.vue'
import LoginBox from '@/components/LoginMainBoxComponent.vue'
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}
</style>
