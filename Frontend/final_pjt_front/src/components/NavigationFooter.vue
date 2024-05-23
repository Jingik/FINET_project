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
      <div class="footer-menu">
        <div class="menu-item">
            <span class="menu-title">예금</span>
            <ul>
              <RouterLink :to="{ name: 'DepositView' }"><li>정기예금</li></RouterLink>
              <RouterLink :to="{ name: 'SavingsView' }"><li>정기적금</li></RouterLink>
            </ul>
        </div>
        <div class="menu-item">
            <span class="menu-title">대출</span>
            <ul>
              <RouterLink :to="{ name: 'CreditloanView' }"><li>신용대출</li></RouterLink>
                <li>전세자금대출</li>
                <li>주택담보대출</li>
            </ul>
        </div>
        <div class="menu-item">
            <span class="menu-title">외환/환전</span>
            <ul>
              <RouterLink :to="{ name: 'ExchangeView' }"><li>환전계산기</li></RouterLink>
            </ul>
        </div>
        <div class="menu-item">
            <span class="menu-title">라운지</span>
            <ul>
              <RouterLink :to="{ name: 'maps' }"><li>은행 찾기</li></RouterLink>
                <RouterLink :to="{ name: 'BoardView' }"><li>커뮤니티</li></RouterLink>
            </ul>
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
  .footer-menu {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px; /* 각 부모 요소들 간의 간격 조정 */
}

.menu-item {
    display: flex;
    flex-direction: column;
    font-size: 18px;
    margin-left : 25px;
}

.menu-title {
    font-weight: bold;
    color: black;
    margin-bottom : 5px
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin-bottom: 5px;
    font-size: 16px;
    color: black;
}

</style>
