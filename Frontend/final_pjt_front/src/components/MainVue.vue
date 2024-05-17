<template>
    <div class="div">
      <NavigationHeader/>
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
      <div class="main">
        <div class="container">
          <div class="heading1">
            <p class="finet">너만 모르고 있던</p>
            <p class="finet">개꿀사이트 FINET</p>
          </div>
          <div class="p1">
            <p class="finet">이제라도 안게 어디야 얼른 시작해보자</p>
            <p class="finet">라떼는 이런거 없었어</p>
          </div>
          <div class="container1">
            <div class="button1">
              <b class="btn-text">상품 비교하기</b>
            </div>
            <div class="button2">
              <b class="btn-text1">회원가입</b>
            </div>
          </div>
        </div>
        <img class="img-icon" alt="" src="@/assets/img/img.png" />
      </div>
      <div class="quick-menu-container">
        <div class="card1">
          <div class="div22">
            <img class="icn-resize-icn-md" alt="" src="@/assets/img/icn resize icn-md.svg" />
            <b class="h3-feature-title1">최고금리 예적금 찾기</b>
            <div class="paragraph">
              <p class="finet">the quick fox jumps over the</p>
              <p class="finet">lazy dog</p>
            </div>
          </div>
        </div>
        <div class="card2">
          <div class="div22">
            <img class="icn-resize-icn-md" alt="" src="@/assets/img/icn resize icn-md.svg" />
            <b class="h3-feature-title2">내집마련 전세대출 찾기</b>
            <div class="paragraph">
              <p class="finet">the quick fox jumps over the</p>
              <p class="finet">lazy dog</p>
            </div>
          </div>
        </div>
        <div class="card3">
          <div class="div22">
            <img class="icn-resize-icn-md" alt="" src="@/assets/img/icn resize icn-md.svg" />
            <b class="h3-feature-title3">내 소비내역 맞춤 카드 찾기</b>
            <div class="paragraph2">
              <p class="finet">the quick fox jumps over the</p>
              <p class="finet">lazy dog</p>
            </div>
          </div>
        </div>
      </div>
      <div class="div26">
        <b class="b">이래도 시작 안 할래?</b>
        <div class="div27">최고금리 예적금, 최저금리 대출, 최대혜택 카드</div>
        <div class="button3">
          <div class="nav-item1">바로 시작하기</div>
        </div>
      </div>
      <div class="div29">
        <img class="nh-ci-1" alt="" src="@/assets/img/NH농협은행 CI 시그니처_국문 1.png" />
        <img class="png-ai-1-icon" alt="" src="@/assets/img/하나은행_로고_PNG_AI_원본_다운 1.png" />
        <img class="png-ai-1-icon1" alt="" src="@/assets/img/우리은행_로고_PNG_AI_원본_다운 1.png" />
        <img class="png-ai-1-1-icon" alt="" src="@/assets/img/기업은행_로고_PNG_AI_원본_다운1 1.png" />
        <img class="png-ai-1-icon2" alt="" src="@/assets/img/국민은행_로고_PNG_AI_원본_다운 1.png" />
        <img class="png-ai-1-icon3" alt="" src="@/assets/img/신한뱅크_로고_PNG_AI_원본_다운 1.png" />
        <img class="png-ai-1-icon4" alt="" src="@/assets/img/새마을금고_로고_PNG_AI_원본_다운 1.png" />
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineComponent } from "vue";
  import NavigationHeader from '@/components/NavigationHeader.vue'
  
  </script>
  
  <style scoped>
  .div {
    width: 100%;
    position: relative;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    background-color: #fff;
    border: 1px solid #000;
    box-sizing: border-box;
    height: 2696px;
    overflow: hidden;
    text-align: left;
    font-size: 16px;
    color: #000;
    font-family: Inter;
  }
  
  .div1, .page {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  
  .items {
    width: 100px;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;
    gap: 24px;
  }
  
  .items-parent {
    position: absolute;
    top: 44px;
    left: 1168px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 43px;
  }
  
  .finet, .copyright2008-finet-all-right {
    margin: 0;
  }
  
  .copyright2008-finet-all-right {
    font-size: 20px;
    color: #000;
  }
  
  .finet-copyright2008-finet-container {
    position: absolute;
    top: 32px;
    left: 80px;
    line-height: 150%;
    font-size: 25px;
    color: #00408b;
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
  
  .child {
  position: absolute;
  top: 1101px;
  left: 7%; /* 왼쪽 끝에서 5% 떨어진 위치에 설정 */
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
  
  .icon, .icon1, .icon2 {
    position: absolute;
    margin: 0 !important;
    object-fit: cover;
    z-index: 1;
  }
  
  .icon {
    width: 401px;
    top: 85px;
    left: 32px;
    height: 401px;
  }
  
  .icon1 {
    width: 439px;
    top: 206px;
    left: 13.33px;
    height: 280px;
  }
  
  .icon2 {
    width: 465px;
    top: 192px;
    left: 0.67px;
    border-radius: 12px;
    height: 294px;
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
    left: 231px;
    width: 85%;
    height: 486px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
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
  
  .btn-text, .btn-text1 {
    position: relative;
    letter-spacing: 0.15px;
    line-height: 16.58px;
    display: inline-block;
    flex-shrink: 0;
  }
  
  .button1, .button2 {
    border-radius: 27.88px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 11.3px 27.1px;
    background-color: #fff;
    border: 1px solid #fff;
  }
  
  .button1:hover, .button2:hover{
  background-color: #007ace;
  border:#007ace;
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
    left: 10%;
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
    top: -66px;
    left: 823px;
    width: 620px;
    height: 620px;
    object-fit: cover;
  }
  
  .main {
    position: absolute;
    top: 145px;
    left: 10%;
    background-color: #0d99f1;
    width: 80%;
    height: 531px;
    overflow: hidden;
    font-size: 43.71px;
    color: #fff;
    font-family: Montserrat;
  }
  
  .icn-resize-icn-md {
    width: 36.2px;
    position: relative;
    height: 29.8px;
    overflow: hidden;
    flex-shrink: 0;
  }
  
  .h3-feature-title1, .h3-feature-title2, .h3-feature-title3 {
    position: relative;
    letter-spacing: 0.08px;
    line-height: 24.11px;
    display: inline-block;
    height: 24.1px;
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
  
  .paragraph, .paragraph2 {
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
  
  .div22{
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
  
  .card1, .card2, .card3 {
    width: 300px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
  }
  .div22:hover{
  background-color: #007ace;
}

  
  .quick-menu-container {
    position: absolute;
    top: calc(50% - 739px);
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
  
  .label {
    flex: 1;
    position: relative;
    line-height: 20px;
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
    background-color: #00276c;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 14px 24px;
    text-align: left;
    font-size: 16px;
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
  
  .nh-ci-1, .png-ai-1-icon, .png-ai-1-icon1, .png-ai-1-1-icon, .png-ai-1-icon2, .png-ai-1-icon3, .png-ai-1-icon4 {
    position: relative;
    height: 30px;
    object-fit: cover;
  }
  
  .nh-ci-1 {
    width: 212.9px;
  }
  
  .png-ai-1-icon {
    width: 153px;
  }
  
  .png-ai-1-icon1 {
    width: 124.4px;
  }
  
  .png-ai-1-1-icon {
    width: 136.3px;
  }
  
  .png-ai-1-icon2 {
    width: 180.3px;
  }
  
  .png-ai-1-icon3 {
    width: 129.7px;
  }
  
  .png-ai-1-icon4 {
    width: 167.5px;
  }
  
  .div29 {
    position: absolute;
    top: 899px;
    left: 10%;
    width: 80%;
    height: 30px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
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
    
    .quick-menu-container {
      flex-direction: column;
      gap: 16px;
    }
    
    .div26 {
      top: 2200px;
      left: 5%;
      width: 90%;
    }
    
    .div29 {
      top: 950px;
      left: 5%;
      width: 90%;
      flex-direction: column;
      gap: 10px;
    }
  }
  
  @media (max-width: 480px) {
    .heading {
      font-size: 32px;
    }
    
    .heading1 {
      font-size: 24px;
      line-height: 32px;
    }
    
    .p1 {
      font-size: 12px;
      line-height: 16px;
    }
    
    .btn-text, .btn-text1 {
      font-size: 12px;
    }
    
    .button1, .button2 {
      padding: 8px 16px;
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
  