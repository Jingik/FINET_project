<template>
  <div class="div">
    <div class="main">
      <div class="container">
        <div class="heading1">
          <p class="finet">모든 금융 정보를 하나로</p>
          <p class="finet">FINET</p>
        </div>
        <div class="p1">
          <p class="finet">FINET은 흩어진 금융 정보를 하나의 네트워크로 연결하여</p>
          <p class="finet">사회초년생, 취업준비생, 신혼부부 등 청년들을 위한 </p>
          <p class="finet">종합금융서비스를 제공합니다</p>
        </div>
        <div class="container1">
          <RouterLink :to="{ name: 'DepositView' }"><div class="button1">
            <b class="btn-text">상품 비교하기</b>
          </div></RouterLink>
          <RouterLink :to="{ name: 'SignUpView' }"><div class="button2">
            <b class="btn-text1">회원가입</b>
          </div></RouterLink>
        </div>
      </div>
      <img class="img-icon" alt="" src="@/assets/img/img.png" />
    </div>
    <div class="quick-menu-container">
      <RouterLink :to="{ name: 'DepositView' }">
        <div class="card3">
          <div class="div22">
            <img class="icon1" alt="" src="@/assets/img/saverate.png" />
            <h3>최고금리 예적금 찾기</h3>
            <div class="paragraph">
              <p class="finet">각 은행 최고 금리 상품을</p>
              <p class="finet">빠르고 쉽게 찾아보세요</p>
            </div>
          </div>
        </div>
      </RouterLink>
      <RouterLink :to="{ name: 'SavingsView' }">
      <div class="card3">
        <div class="div22">
          <img class="icon1" alt="" src="@/assets/img/loanrate.png" />
          <h3>내집마련 전세대출 찾기</h3>
          <div class="paragraph">
            <p class="finet">내집 마련을 위한 최저 금리 대출</p>
            <p class="finet">지금 바로 확인하세요</p>
          </div>
        </div>
      </div>
      </RouterLink>
      <RouterLink :to="{ name: 'ExchangeView' }">
      <div class="card3">
        <div class="div22">
          <img class="icon1" alt="" src="@/assets/img/exchange.png" />
          <h3>신혼여행 환전 계산기</h3>
          <div class="paragraph2">
            <p class="finet">설레는 신혼여행 전 미리미리</p>
            <p class="finet">환율을 계산해보세요</p>
          </div>
        </div>
      </div>
    </RouterLink>
      <RouterLink :to="{ name: 'maps' }">
      <div class="card3">
        <div class="div22">
          <img class="icon1" alt="" src="@/assets/img/commu.png" />
          <h3>상품 후기 커뮤니티</h3>
          <div class="paragraph2">
            <p class="finet">다양한 상품에 대한 후기를</p>
            <p class="finet">커뮤니티에서 확인해 보세요</p>
          </div>
        </div>
      </div>
    </RouterLink>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.icon1 {
  height: 40px;
  width: 40px;
}
.div {
  width: 100%;
  position: relative;
  background-color: #fff;
  box-sizing: border-box;
  height: 900px;
  overflow: hidden;
  text-align: left;
  font-size: 16px;
  color: #000;
  font-family: Inter;
}

.finet {
  margin: 0;
}

h3 {
  font-size: 30;
}

.divider {
  position: absolute;
  top: 0.5px;
  left: 79.5px;
  border-top: 1px solid #00276c;
  box-sizing: border-box;
  width: 1761px;
  height: 1px;
}

.heading1 {
  width: 100%;
  position: relative;
  letter-spacing: 0.15px;
  line-height: 60.29px;
  font-weight: 800;
  display: inline-block;
  height: auto;
  flex-shrink: 0;
}

.p1 {
  width: 100%;
  position: relative;
  font-size: 15.07px;
  letter-spacing: 0.15px;
  line-height: 22.61px;
  font-weight: 500;
  display: inline-block;
  height: auto;
  flex-shrink: 0;
}

.btn-text,
.btn-text1 {
  position: relative;
  letter-spacing: 0.15px;
  line-height: 16.58px;
  display: inline-block;
  flex-shrink: 0;
}

.button1,
.button2 {
  border-radius: 27.88px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 11.3px 27.1px;
  background-color: #fff;
  border: 1px solid #fff;
}

.button1:hover,
.button2:hover {
  background-color: #007ace;
  border: #007ace;
  /* color: #fff; 텍스트 색상도 변경하려면 추가 */
}

.container1 {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 7.5px;
  text-align: center;
  font-size: 10.55px;
  color: #1f1212;
}

.container {
  position: absolute;
  top: 115px;
  left: 15%;
  width: 80%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 26.4px;
}

.img-icon {
  position: absolute;
  bottom:0;
  right: 8%;
  height: 90%;
  object-fit: cover;
}

.main {
  position: absolute;
  top: 100px;
  left: 10%;
  background-color: #0d99f1;
  width: 80%;
  height: 531px;
  overflow: hidden;
  font-size: 43.71px;
  color: #fff;
  font-family: Montserrat;
}

.h3-feature-title1,
.h3-feature-title2,
.h3-feature-title3 {
  position: relative;
  letter-spacing: 0.08px;
  line-height: 24.11px;
  display: inline-block;
  height: 24.1px;
  font-size: 17px;
  flex-shrink: 0;
}

.h3-feature-title1 {
  width: 180.9px;
}

.h3-feature-title2 {
  width: 185px;
}

.h3-feature-title3 {
  width: 209px;
}

.paragraph,
.paragraph2 {
  width: 160.5px;
  position: relative;
  font-size: 10.55px;
  letter-spacing: 0.15px;
  line-height: 15.07px;
  font-weight: 500;
  display: inline-block;
  height: 30.1px;
  flex-shrink: 0;
}

.div22 {
  width: 100%;
  box-shadow: 0px 9.79669189453125px 14.32px rgba(0, 0, 0, 0.07);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 26.4px 30.1px;
  box-sizing: border-box;
  gap: 7.5px;
  background-color: #fff;
  transition: background-color 0.3s, color 0.3s; /* 애니메이션 추가 */
}

.card1,
.card2,
.card3 {
  width: 300px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}
.div22:hover {
  background-color: #007ace;
}

.quick-menu-container {
  position: absolute;
  top: 550px;
  left: 5%;
  width: 90%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 22.6px;
  font-size: 18.09px;
  color: #252b42;
  font-family: Montserrat;
  flex-wrap: wrap;
}

@media (max-width: 768px) {
  .container {
    top: 90px;
    left: 5%;
    width: 90%;
  }

  .main {
    left: 5%;
    width: 90%;
  }

  .img-icon {
    width: 100%;
    height: auto;
    top: 100px;
    left: 50%;
    transform: translateX(-50%);
  }

  .quick-menu-container {
    flex-direction: column;
    gap: 16px;
  }
}

@media (max-width: 480px) {
  .heading1 {
    font-size: 24px;
    line-height: 32px;
  }

  .p1 {
    font-size: 12px;
    line-height: 16px;
  }

  .btn-text,
  .btn-text1 {
    font-size: 12px;
  }

  .button1,
  .button2 {
    padding: 8px 16px;
  }
}
</style>
