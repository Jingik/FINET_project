<template>
    <div class="child"></div>
    <div class="cards">
      <div class="customer-quote">
        <div class="div17">청년들의 재테크, FiNET이 함께합니다.<br>첫걸음부터 성공을 위한 파트너</div>
        <img class="icon" alt="" src="@/assets/img/제목을 입력해주세요_-005 (2) 1.png" />
      </div>
      <div class="customer-quote">
        <div class="div17">내집마련을 위한 현명한 선택<br> FiNET 대출 비교로 시작하세요</div>
        <img class="icon1" alt="" src="@/assets/img/제목을 입력해주세요_-001 (2) 1.png" />
      </div>
      <div class="customer-quote">
        <div class="div17">신혼여행을 더욱 달콤하게,<br>FINET으로 완벽한 여행을 계획하세요</div>
        <img class="icon2" alt="" src="@/assets/img/제목을 입력해주세요_-003 (1) 1.png" />
      </div>
    </div>
    <div class="heading">
      <div class="div20">FINET으로 더 나은 미래를 계획하세요</div>
      <div class="div21"></div>
    </div>
    <div class="div26">
      <b class="b">당신의 금융 라이프<br> FiNET이 함께합니다.</b>
      <div class="div27">최고금리 예적금, 최저금리 대출, 최대혜택 카드 비교</div>
      <div class="button3">
        <RouterLink :to="{ name: 'SignUpView' }"
            ><div class="nav-item1">바로 시작하기</div></RouterLink>
      </div>
    </div>

</template>

<script setup>
</script>

<style scoped>
.child {
  position: absolute;
  top: 1100px;
  left: 2%;
  right: 2%;
  background-color: #0d99f1;
  height: 850px;
}

.div17 {
  text-align: center;
  align-self: stretch;
  position: relative;
  line-height: 150%;
  font-weight: 500;
  z-index: 0;
}

.icon,
.icon1,
.icon2 {
  bottom:0%;
  position: absolute;
  /* bottom: 0; 부모 요소의 맨 아래에 배치 */
  width: 100%; /* 부모 요소의 너비에 맞춤 */
  /* height: auto; 비율을 유지하며 높이 조정 */
  max-height:80%;
  max-width: 100%; /* 최대 너비를 부모 요소의 너비로 제한 */
  object-fit: contain; /* 비율을 유지하며 부모 요소에 맞춤 */
  left:0;
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

.customer-quote:hover {
  background-color: #007ace;
  border: #007ace;
}

.cards {
  position: absolute;
  top: 1300px;
  left: 50%;
  transform: translateX(-50%);
  width: 85%;
  height: 580px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
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
  left: 5%; /* 모바일에서 좌우 여백을 조정 */
  width: 90%; /* 모바일에서 좌우 여백을 조정 */
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 8px;
  font-size: 40px;
  color: #fff;
}
.button3 {
  background-color: #0d99f1;
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.05);
  border-radius: 8px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 14px 24px;
  text-align: left;
  font-size: 16px;
  color: white;
  border: 1px solid #000;
}

.button3:hover {
  background-color: #00408b;
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

