<template>
  <div class="div29">
    <img class="nh-ci-1" alt="" src="@/assets/img/NH농협은행 CI 시그니처_국문 1.png" />
    <img class="png-ai-1-icon" alt="" src="@/assets/img/하나은행_로고_PNG_AI_원본_다운 1.png" />
    <img class="png-ai-1-icon1" alt="" src="@/assets/img/우리은행_로고_PNG_AI_원본_다운 1.png" />
    <img class="png-ai-1-1-icon" alt="" src="@/assets/img/기업은행_로고_PNG_AI_원본_다운1 1.png" />
    <img class="png-ai-1-icon2" alt="" src="@/assets/img/국민은행_로고_PNG_AI_원본_다운 1.png" />
    <img class="png-ai-1-icon3" alt="" src="@/assets/img/신한뱅크_로고_PNG_AI_원본_다운 1.png" />
    <img class="png-ai-1-icon4" alt="" src="@/assets/img/새마을금고_로고_PNG_AI_원본_다운 1.png" />
  </div>
</template>

<script setup>
import { defineComponent } from "vue";
</script>

<style scoped>
.nh-ci-1, .png-ai-1-icon, .png-ai-1-icon1, .png-ai-1-1-icon, .png-ai-1-icon2, .png-ai-1-icon3, .png-ai-1-icon4 {
height: 30px;
object-fit: contain;
max-width: 100%;
}

.div29 {
position: absolute;
top: 899px;
left: 10%;
width: 80%;
display: flex;
flex-wrap: wrap; /* 이미지가 부모 요소 너비에 맞춰서 줄 바꿈되도록 설정 */
justify-content: center; /* 수평 가운데 정렬 */
align-items: center; /* 수직 가운데 정렬 */
gap: 10px; /* 이미지 사이의 간격 */
}

@media (max-width: 768px) {
.div29 {
  top: 950px;
  left: 5%;
  width: 90%;
  flex-direction: column; /* 작은 화면에서는 이미지를 세로로 정렬 */
}
}
</style>
