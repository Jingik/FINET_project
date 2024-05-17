<template>
    <div class="child"></div>
    <div class="cards">
      <div class="customer-quote">
        <div class="div17">1번 서비스서비스</div>
        <img class="icon" alt="" src="@/assets/img/제목을 입력해주세요_-005 (2) 1.png" />
      </div>
      <div class="customer-quote">
        <div class="div17">2번 서비스서비스</div>
        <img class="icon1" alt="" src="@/assets/img/제목을 입력해주세요_-001 (2) 1.png" />
      </div>
      <div class="customer-quote">
        <div class="div17">3번 서비스서비스</div>
        <img class="icon2" alt="" src="@/assets/img/제목을 입력해주세요_-003 (1) 1.png" />
      </div>
    </div>
    <div class="heading">
      <div class="div20">우리들의 멋진 서비스</div>
      <div class="div21">이거 안하면 호구임;</div>
    </div>
    <div class="div26">
      <b class="b">이래도 시작 안 할래?</b>
      <div class="div27">최고금리 예적금, 최저금리 대출, 최대혜택 카드</div>
      <div class="button3">
        <div class="nav-item1">바로 시작하기</div>
      </div>
    </div>

</template>

<script setup>
import { defineComponent } from "vue";

</script>

<style scoped>
.child {
position: absolute;
top: 1100px;
left: 2%; /* 왼쪽 끝에서 5% 떨어진 위치에 설정 */
right: 2%; /* 오른쪽 끝에서 5% 떨어진 위치에 설정 */
background-color: #0d99f1;
height: 831px;
}


.div17 {
  align-self: stretch;
  position: relative;
  line-height: 150%;
  font-weight: 500;
  z-index: 0;
}

.icon {
position: absolute;
bottom: 0; /* 부모 요소의 맨 아래에 배치 */
width: 80%; /* 부모 요소의 너비에 맞춤 */
height: auto; /* 비율을 유지하며 높이 조정 */
max-width: 100%; /* 최대 너비를 부모 요소의 너비로 제한 */
object-fit: contain; /* 비율을 유지하며 부모 요소에 맞춤 */
}

.icon1 {
position: absolute;
bottom: 0; /* 부모 요소의 맨 아래에 배치 */
width: 85%; /* 부모 요소의 너비에 맞춤 */
height: auto; /* 비율을 유지하며 높이 조정 */
max-width: 100%; /* 최대 너비를 부모 요소의 너비로 제한 */
object-fit: contain; /* 비율을 유지하며 부모 요소에 맞춤 */
}

.icon2 {
position: absolute;
bottom: 0; /* 부모 요소의 맨 아래에 배치 */
width: 90%; /* 부모 요소의 너비에 맞춤 */
height: auto; /* 비율을 유지하며 높이 조정 */
max-width: 100%; /* 최대 너비를 부모 요소의 너비로 제한 */
object-fit: contain; /* 비율을 유지하며 부모 요소에 맞춤 */
}
.customer-quote {
  align-self: stretch;
  flex: 1;
  box-shadow: -4px 8px 20px rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  background-color: #fff;
  border: 1px solid #f7f7f7;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 32px;
  position: relative;
  gap: 48px;
}
.customer-quote:hover{
  background-color: #007ace;
  border:#007ace;
}
.cards {
position: absolute;
top: 1354px;
left: 50%; /* 부모 요소의 수평 중앙으로 이동 */
transform: translateX(-50%); /* 자신을 수평 중앙으로 이동 */
width: 85%;
height: 486px;
display: flex;
flex-direction: row;
align-items: flex-start;
justify-content: center; /* 카드를 수평 중앙으로 정렬 */
gap: 32px;
font-size: 20px;
flex-wrap: wrap;
}


.div20 {
  align-self: stretch;
  position: relative;
  line-height: 110%;
  font-weight: 600;
}

.div21 {
  width: 625px;
  position: relative;
  font-size: 24px;
  line-height: 150%;
  display: flex;
  align-items: center;
}

.heading {
  position: absolute;
  top: 1191px;
  left: 244px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 8px;
  font-size: 40px;
  color: #fff;
}

.b {
  align-self: stretch;
  position: relative;
  letter-spacing: -0.02em;
}

.div27 {
  align-self: stretch;
  position: relative;
  font-size: 24px;
  line-height: 150%;
  color: #828282;
}

.button3 {
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.05);
  border-radius: 8px;
  background-color: #fff;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 14px 24px;
  text-align: left;
  font-size: 16px;
  color: #000;
  border: 1px solid #000;
}
.button3:hover{
  background-color: #00276c;
  color: #fff;
}
.div26 {
  position: absolute;
  top: 2070px;
  left: 10%;
  width: 80%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 24px;
  text-align: center;
  font-size: 64px;
}

@media (max-width: 768px) {
  
  .heading {
    left: 5%;
    width: 90%;
  }
  
  .cards {
    top: 1500px;
    left: 5%;
    width: 90%;
    flex-direction: column;
    gap: 16px;
  }
  
  .div26 {
    top: 2200px;
    left: 5%;
    width: 90%;
  }
  
}

@media (max-width: 480px) {
  .heading {
    font-size: 32px;
  }
  
  .button3 {
    padding: 10px 20px;
  }
  
  .div26 {
    font-size: 48px;
  }
  
  .div27 {
    font-size: 20px;
  }
}
</style>
