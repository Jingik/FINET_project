<template>
    <div class="div">
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
    </div>
  </template>
  
  <script setup>
  
  </script>
  
  <style scoped>
  .div {
    width: 100%;
    position: relative;
    background-color: #fff;
    box-sizing: border-box;
    height: 2696px;
    overflow: hidden;
    text-align: left;
    font-size: 16px;
    color: #000;
    font-family: Inter;
  }

  .finet{
    margin: 0;
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
    
    .btn-text, .btn-text1 {
      font-size: 12px;
    }
    
    .button1, .button2 {
      padding: 8px 16px;
    }
    
  }
  </style>
  