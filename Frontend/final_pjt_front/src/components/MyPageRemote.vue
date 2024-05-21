<template>
  <div class="remocon" >
    <div @click="goToMypage" class="shortcut">
      <img src="/src/assets/img/filledheart.png" alt="Mypage Remocon" class="remocon-image">
      <p>관심목록</p>
    </div>
    <hr>
    <div @click="goToHome" class="shortcut">
      <img src="/src/assets/img/tohome.png" alt="Mypage Remocon" class="remocon-image">
      <p>홈으로</p>
    </div>
    <hr>
    <div @click="goTolounge" class="shortcut">
      <img src="/src/assets/img/community.png" alt="Mypage Remocon" class="remocon-image">
      <p>커뮤니티</p>
    </div>
  </div>

</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

function goToMypage() {
  router.push('/mypage'); 
}

function goToHome() {
  router.push('main'); 
}

function goTolounge() {
  router.push('posts'); 
}
</script>

<style scoped>
.remocon {
  position: fixed;
  right: 50px;
  top: 60%;
  transform: translateY(-50%);
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 10px;
  cursor: pointer;
  z-index: 1000;
  text-align: center;
  border-radius: 30px; /* 알약 모양 디자인 */
  height:300px;
}

.remocon-image {
  width: 30px;
  height: 30px;
  margin-bottom: 5px;
}

.shortcut {
  margin : 15px auto
}
</style>
