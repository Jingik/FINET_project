<template>
  <div class="navigation-footer ">
    <div class="items-parent">
      <div class="items">
        <div class="div1">예적금</div>
        <div class="page">정기예금</div>
        <div class="page">정기적금</div>
        <div class="page">자유입출금</div>
      </div>
      <div class="items">
        <div class="div1">대출</div>
        <div class="page">신용대출</div>
        <div class="page">전세자금대출</div>
        <div class="page">주택담보대출</div>
      </div>
      <div class="items">
        <div class="div1">신용카드</div>
        <div class="page">한눈에 보기</div>
        <div class="page">추천카드</div>
        <div class="page">내게 맞는 카드</div>
      </div>
      <div class="items">
        <div class="div1">외환/환전</div>
        <div class="page">환율조회</div>
        <div class="page">환전계산기</div>
      </div>
      <div class="items">
        <div class="div1">라운지</div>
        <div class="page">Page</div>
        <div class="page">Page</div>
        <div class="page">Page</div>
      </div>
    </div>
    <div class="finet-copyright2008-finet-container">
      <p class="finet">
        <span>FINET</span>
      </p>
      <p class="finet">
        <span>&nbsp;</span>
      </p>
      <p class="copyright2008-finet-all-right">
        <span>Copyrightⓒ2008 FINET All rights reserved.</span>
      </p>
    </div>
    <div class="divider"></div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.navigation-footer {
  width: 100%;
  background-color: #fff;
  color: #454545;
  padding: 20px;
  box-sizing: border-box;
}

.items-parent {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 43px;
  flex-wrap: wrap;
}

.items {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
}

.div1, .page {
  line-height: 150%;
  font-weight: 500;
  color: #000;
}

.finet, .copyright2008-finet-all-right {
  margin: 0;
}

.finet {
  font-size: 25px;
  color: #00408b;
}

.copyright2008-finet-all-right {
  font-size: 20px;
  color: #000;
}

.finet-copyright2008-finet-container {
  text-align: center;
  margin-top: 20px;
}

.divider {
  border-top: 1px solid #00276c;
  margin-top: 20px;
}

@media (max-width: 768px) {
  .items {
    align-items: center;
  }

  .div1, .page {
    text-align: center;
  }
}

@media (max-width: 480px) {
  .div1 {
    font-size: 18px;
  }

  .page {
    font-size: 16px;
  }

  .finet {
    font-size: 20px;
  }

  .copyright2008-finet-all-right {
    font-size: 16px;
  }
}
</style>
