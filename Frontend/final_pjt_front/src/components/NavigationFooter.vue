<template>
  <footer class="divider-parent">
    <div class="divider" />
    <div class="finet-copyright2008-finet-all-parent">
      <div class="finet-copyright2008-finet-container">
        <span>
          <p class="finet">
            <span>
              <br>
              <span>FINET</span>
              <br>
            </span>
          </p>
          <p class="blank-line">
            <span>
              <span>&nbsp;</span>
            </span>
          </p>
          <p class="copyright2008-finet-all-right">
            <span>
              <span>Copyrightⓒ2024 FINET All rights reserved.</span>
            </span>
          </p>
        </span>
      </div>
      <div class="frame-wrapper">
        <div class="frame-parent">
          <div class="parent">
            <div class="div1">예적금</div>
            <div class="div2">정기예금</div>
            <div class="div3">정기적금</div>
            <div class="div4">자유입출금</div>
          </div>
          <div class="group">
            <div class="div5">대출</div>
            <div class="div6">신용대출</div>
            <div class="div7">전세자금대출</div>
            <div class="div8">주택담보대출</div>
          </div>
          <div class="finance-menu">
            <div class="container">
              <div class="div9">신용카드</div>
              <div class="div10">외환/환전</div>
            </div>
            <div class="frame-div">
              <div class="div11">한눈에 보기</div>
              <div class="div12">환전계산기</div>
            </div>
            <div class="frame-group">
              <div class="parent1">
                <div class="div13">추천카드</div>
              </div>
              <div class="div15">내게 맞는 카드</div>
            </div>
          </div>
          <div class="parent2">
            <div class="div16">라운지</div>
            <div class="page"> 은행 찾기</div>
            <div class="page1">커뮤니티</div>
            <div class="page2">Page</div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
<script setup>
</script>
<style scoped>
  .divider {
    align-self: stretch;
    height: 1px;
    position: relative;
    border-top: 1px solid var(--color1);
    box-sizing: border-box;
  }
  .finet {
    margin: 0;
  }
  .blank-line {
    margin: 0;
  }
  .copyright2008-finet-all-right {
    margin: 0;
    font-size: var(--body-text-size);
    color: var(--color-black);
  }
  .finet-copyright2008-finet-container {
    height: 104px;
    position: relative;
    line-height: 150%;
    display: flex;
    align-items: center;
    max-width: 100%;
  }
  .div1 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
    color: var(--color-black);
  }
  .div2 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  .div3 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  .div4 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  .parent {
    width: 100px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-5xl);
  }
  .div5 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
    color: var(--color-black);
  }
  .div6 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  .div7 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  .div8 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  .group {
    width: 100px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-5xl);
  }
  .div9 {
    width: 100px;
    position: relative;
    line-height: 150%;
    font-weight: 500;
    display: flex;
    align-items: center;
    flex-shrink: 0;
  }
  .div10 {
    width: 100px;
    position: relative;
    line-height: 150%;
    font-weight: 500;
    display: flex;
    align-items: center;
    flex-shrink: 0;
  }
  .container {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: space-between;
    gap: var(--gap-xl);
    color: var(--color-black);
  }
  .div11 {
    width: 100px;
    position: relative;
    line-height: 150%;
    font-weight: 500;
    display: flex;
    align-items: center;
    flex-shrink: 0;
  }
  .div12 {
    width: 100px;
    position: relative;
    line-height: 150%;
    font-weight: 500;
    display: flex;
    align-items: center;
    flex-shrink: 0;
  }
  .frame-div {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: space-between;
    gap: var(--gap-xl);
  }
  .div13 {
    width: 100px;
    position: relative;
    line-height: 150%;
    font-weight: 500;
    display: flex;
    align-items: center;
    flex-shrink: 0;
  }
  .div14 {
    width: 100px;
    position: relative;
    line-height: 150%;
    font-weight: 500;
    display: flex;
    align-items: center;
    flex-shrink: 0;
  }
  .parent1 {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: space-between;
    gap: var(--gap-xl);
  }
  .div15 {
    position: relative;
    line-height: 150%;
    font-weight: 500;
    display: inline-block;
    min-width: 100px;
  }
  .frame-group {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-5xl);
  }
  .finance-menu {
    width: 243px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-5xl);
  }
  .div16 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
    color: var(--color-black);
  }
  .page {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  .page1 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  .page2 {
    align-self: stretch;
    position: relative;
    line-height: 150%;
    font-weight: 500;
  }
  .parent2 {
    width: 100px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-5xl);
  }
  .frame-parent {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-24xl);
  }
  .frame-wrapper {
    width: 672px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-xs) 0px 0px;
    box-sizing: border-box;
    max-width: 100%;
    font-size: var(--small-text-size);
    color: var(--color-darkslategray-100);
  }
  .finet-copyright2008-finet-all-parent {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: space-between;
    max-width: 100%;
    gap: var(--gap-xl);
  }
  .divider-parent {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 1920px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-11xl);
    max-width: 100%;
    text-align: left;
    font-size: var(--font-size-6xl);
    color: var(--color4);
    font-family: var(--small-text);
  }

  @media screen and (max-width: 1225px) {
    .finet-copyright2008-finet-all-parent {
      flex-wrap: wrap;
    }
  }
  @media screen and (max-width: 750px) {
    .frame-parent {
      flex-wrap: wrap;
    }
  }
  @media screen and (max-width: 450px) {
    .finet-copyright2008-finet-container {
      font-size: var(--small-text-size);
      line-height: 30px;
    }
  }
</style>
