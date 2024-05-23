<template>
  <div class="div">
    <MainBox />
  </div>
  <!-- <div class="bank">
    <MainBank />
  </div> -->
  <div class="container">
    <LoginBox />
  </div>

</template>

<script setup>
import MainBox from '@/components/MainBoxComponent.vue'
import LoginBox from '@/components/LoginMainBoxComponent.vue'
import MainBank from '@/components/BankComponent.vue'
</script>

<style scoped>
.div {
    width: 100%;
    position: relative;
    /* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25); */
    background-color: #fff;
    /* border: 1px solid #000; */
    box-sizing: border-box;
    height: 850px;
    overflow: hidden;
    text-align: left;
    font-size: 16px;
    color: #000;
    font-family: Inter;
  }

/* html, body, #app {
  height: 100%;
  margin: 0;
  padding: 0;
} */
.bank {
  position: absolute;
  height: 80px; /* 아래 여백을 100px로 설정 */
  left: 0;
  width: 100%;
  top : 100%;
  display: flex;
}
/* .container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  position: relative;
} */


</style>
