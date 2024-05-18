<template>
  <div class="header">
    <div class="span">
      <div class="p4">FINET</div>
      <img class="img-icon1" alt="" src="@/assets/img/img (1).png" />
    </div>
    <div class="navbar">
      <div class="nav" @mouseover="showDropdown('deposit')" @mouseleave="hideDropdown('deposit')">
        예적금
        <div v-if="dropdownVisible.deposit" class="dropdown-content">
          <div class="dropdown-item">정기예금</div>
          <div class="dropdown-item">정기적금</div>
          <div class="dropdown-item">자유입출금</div>
        </div>
      </div>
      <div class="nav" @mouseover="showDropdown('loan')" @mouseleave="hideDropdown('loan')">
        대출
        <div v-if="dropdownVisible.loan" class="dropdown-content">
          <div class="dropdown-item">신용대출</div>
          <div class="dropdown-item">전세자금대출</div>
          <div class="dropdown-item">주택담보대출</div>
        </div>
      </div>
      <div class="nav" @mouseover="showDropdown('creditCard')" @mouseleave="hideDropdown('creditCard')">
        신용카드
        <div v-if="dropdownVisible.creditCard" class="dropdown-content">
          <div class="dropdown-item">전체카드조회</div>
          <div class="dropdown-item">추천카드</div>
          <div class="dropdown-item">내게 맞는 카드</div>
        </div>
      </div>
      <div class="nav" @mouseover="showDropdown('exchange')" @mouseleave="hideDropdown('exchange')">
        외환/환전
        <div v-if="dropdownVisible.exchange" class="dropdown-content">
          <RouterLink :to="{ name: 'ExchangeView' }"><div class="dropdown-item">환율조회</div></RouterLink>
          <div class="dropdown-item">환전계산기</div>
        </div>
      </div>
      <div class="nav" @mouseover="showDropdown('lounge')" @mouseleave="hideDropdown('lounge')">
        라운지
        <div v-if="dropdownVisible.lounge" class="dropdown-content">
          <div class="dropdown-item">입주가능 주택찾기</div>
          <div class="dropdown-item">금융상품후기</div>
          <div class="dropdown-item">서비스 3</div>
          <div class="dropdown-item">서비스 4</div>
        </div>
      </div>
      <div class="input-typetext">
        <div class="label">검색어를 입력해주세요.</div>
        <img class="button-typesubmit-icon" alt="" src="@/assets/img/button type=submit.svg" />
      </div>
      <RouterLink :to="isLoggedIn ? { name: 'ProfilePage' } : { name: 'LogInView' }">
        <div class="button">
          <div class="nav">{{ isLoggedIn ? '마이페이지 가기' : '로그인/회원가입' }}</div>
        </div>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router'

const dropdownVisible = ref({
  deposit: false,
  loan: false,
  creditCard: false,
  exchange: false,
  lounge: false,
});

// Simulated login state; replace with actual login logic
const isLoggedIn = ref(false);

const showDropdown = (key) => {
  dropdownVisible.value[key] = true;
};

const hideDropdown = (key) => {
  dropdownVisible.value[key] = false;
};
</script>

<style scoped>
.header {
  align-items: flex-start;
  display: flex;
  gap: 10px;
  height: 86px;
  width: 83.33%;
  margin: 0 auto;
  top: 0;
}

.header .span {
  height: 107px;
  margin-bottom: -21px;
  position: relative;
  width: 162px;
}

.header .p4 {
  color: var(--x1-3);
  font-family: "Inter", Helvetica;
  font-size: 25px;
  font-weight: 500;
  height: 38px;
  left: 86px;
  letter-spacing: 0;
  line-height: 37.5px;
  position: absolute;
  top: 31px;
  white-space: nowrap;
  width: 74px;
}

.header .img-icon1 {
  height: 107px;
  left: 0;
  object-fit: cover;
  position: absolute;
  top: 0;
  width: 86px;
}

.header .navbar {
  align-items: center;
  display: flex;
  gap: var(--variable-collection-spacing-m);
  height: 86px;
  justify-content: flex-end;
  margin-left: auto;
}

.header .nav {
  color: #828282;
  font-family: var(--body-text-font-family);
  font-size: var(--body-text-font-size);
  font-style: var(--body-text-font-style);
  font-weight: var(--body-text-font-weight);
  letter-spacing: var(--body-text-letter-spacing);
  line-height: var(--body-text-line-height);
  position: relative;
  white-space: nowrap;
  width: fit-content;
}

.header .input-type-text {
  align-items: center;
  border: 1px solid;
  border-color: #0000001a;
  border-radius: 6px;
  display: flex;
  gap: 4px;
  justify-content: flex-end;
  padding: 8px;
  position: relative;
  width: 200px;
}

.header .label {
  color: #00000080;
  flex: 1;
  font-family: "Roboto", Helvetica;
  font-size: 14px;
  font-weight: 400;
  letter-spacing: 0;
  line-height: 20px;
  margin-top: -1px;
  position: relative;
}

.header .button-typesubmit-icon {
  height: 20px;
  position: relative;
  width: 20px;
}

.header .button-2 {
  all: unset;
  align-items: center;
  background-color: #edf0f3;
  border: 1px solid;
  border-color: #c2b3b3;
  border-radius: 8px;
  box-shadow: var(--button-shadow);
  box-sizing: border-box;
  display: flex;
  gap: 8px;
  justify-content: center;
  padding: 14px 24px;
  position: relative;
  width: 104px;
}

.header .text-wrapper-3 {
  color: #565454;
  font-family: var(--small-text-font-family);
  font-size: var(--small-text-font-size);
  font-style: var(--small-text-font-style);
  font-weight: var(--small-text-font-weight);
  letter-spacing: var(--small-text-letter-spacing);
  line-height: var(--small-text-line-height);
  margin-left: -1.5px;
  margin-right: -1.5px;
  margin-top: -1px;
  position: relative;
  white-space: nowrap;
  width: fit-content;
}

.dropdown-content {
  position: absolute;
  top: 100%;
  left: 0;
  background-color: white;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  z-index: 1;
  display: flex;
  flex-direction: column;
}

.dropdown-item {
  padding: 12px 16px;
  cursor: pointer;
  white-space: nowrap;
}

.dropdown-item:hover {
  background-color: #f1f1f1;
}

@media (max-width: 1024px) {
  .navbar {
    gap: 10px;
  }

  .input-typetext {
    width: 150px;
  }

  .button {
    padding: 8px 16px;
    font-size: 14px;
  }
}

@media (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
    height: auto;
    padding: 10px;
    width: 90%;
  }

  .header .navbar {
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
  }

  .header .nav {
    width: 100%;
    padding: 10px 0;
  }

  .header .input-type-text {
    width: 100%;
  }
}

@media (max-width: 480px) {
  .header {
    padding: 0 5px;
  }

  .header .p4 {
    font-size: 20px;
  }

  .header .nav {
    font-size: 18px;
  }

  .header .input-type-text {
    font-size: 12px;
  }

  .header .button {
    font-size: 14px;
  }
}
</style>
