<template>
  <div class="header">
    <div class="span">
      <div class="p4">FINET</div>
      <img class="img-icon1" alt="" src="@/assets/img/img (1).png" />
    </div>
    <div class="nav">
      <div class="nav-item1" @mouseover="showDropdown('deposit')" @mouseleave="hideDropdown('deposit')">
        예적금
        <div v-if="dropdownVisible.deposit" class="dropdown-content">
          <div class="dropdown-item">정기예금</div>
          <div class="dropdown-item">정기적금</div>
          <div class="dropdown-item">자유입출금</div>
        </div>
      </div>
      <div class="nav-item1" @mouseover="showDropdown('loan')" @mouseleave="hideDropdown('loan')">
        대출
        <div v-if="dropdownVisible.loan" class="dropdown-content">
          <div class="dropdown-item">신용대출</div>
          <div class="dropdown-item">전세자금대출</div>
          <div class="dropdown-item">주택담보대출</div>
        </div>
      </div>
      <div class="nav-item1" @mouseover="showDropdown('creditCard')" @mouseleave="hideDropdown('creditCard')">
        신용카드
        <div v-if="dropdownVisible.creditCard" class="dropdown-content">
          <div class="dropdown-item">전체카드조회</div>
          <div class="dropdown-item">추천카드</div>
          <div class="dropdown-item">내게 맞는 카드</div>
        </div>
      </div>
      <div class="nav-item1" @mouseover="showDropdown('exchange')" @mouseleave="hideDropdown('exchange')">
        외환/환전
        <div v-if="dropdownVisible.exchange" class="dropdown-content">
          <div class="dropdown-item">환율조회</div>
          <div class="dropdown-item">환전계산기</div>
        </div>
      </div>
      <div class="nav-item1" @mouseover="showDropdown('lounge')" @mouseleave="hideDropdown('lounge')">
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
      <div class="button">
        <div class="nav-item1">로그인/회원가입</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const dropdownVisible = ref({
  deposit: false,
  loan: false,
  creditCard: false,
  exchange: false,
  lounge: false,
});

const showDropdown = (key) => {
  dropdownVisible.value[key] = true;
};

const hideDropdown = (key) => {
  dropdownVisible.value[key] = false;
};
</script>

<style scoped>
.header {
  position: absolute;
  top: 0;
  left: 80px;
  width: calc(100% - 160px);
  height: 86px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  font-size: 25px;
  color: #00408b;
  padding: 0 10px;
}

.span {
  display: flex;
  align-items: center;
  gap: 10px;
}

.p4 {
  line-height: 150%;
  font-weight: 500;
  display: flex;
  align-items: center;
}

.img-icon1 {
  width: 86px;
  height: 86px;
  object-fit: contain;
}

.nav {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-end;
  gap: 20px;
  font-size: 20px;
  color: #828282;
  flex-wrap: wrap;
}

.nav-item1 {
  position: relative;
  line-height: 150%;
  font-weight: 500;
  white-space: nowrap;
  cursor: pointer;
}

.input-typetext {
  width: 200px;
  border-radius: 6px;
  border: 1px solid rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  padding: 8px;
  gap: 4px;
  font-size: 14px;
  color: rgba(0, 0, 0, 0.5);
  font-family: Roboto;
}

.button-typesubmit-icon {
  width: 20px;
  height: 20px;
}

.button {
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.05);
  border-radius: 8px;
  background-color: #005cac;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  white-space: nowrap;
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
  .nav {
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
  }

  .span {
    width: 100%;
    justify-content: space-between;
    padding: 10px 0;
  }

  .nav {
    width: 100%;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }

  .input-typetext {
    width: 100%;
  }
}

@media (max-width: 480px) {
  .header {
    padding: 0 5px;
  }

  .p4 {
    font-size: 20px;
  }

  .nav-item1 {
    font-size: 18px;
  }

  .input-typetext {
    font-size: 12px;
  }

  .button {
    font-size: 14px;
  }
}
</style>
