<template>
  <div class="exchange-rates-container">
    <h1 class="title">국가별 환전 계산기</h1>
    <ul class="cny">
      <li>
        '최종고시환율'은 오늘 기준 가장 최근 고시된 환율정보를 나타내며,
        은행의 환율고시가 종료되지 않은 상태일 수 있습니다.
      </li>
      <li>
        중국 위안화(CNY)는 홍콩 외환시장에서 거래되는 위안화
        환율정보(CNH)를 고시합니다.
      </li>
      <li>일본은 100엔을 기준으로 합니다.</li>
    </ul>
    <div class="button-container">
<div class="currency-buttons">
  <div v-for="(currency, index) in currencies" :key="currency">
    <img 
      @click="fetchExchangeRate(currency, currencyUnits[currency])"
      :src="'/src/assets/img/' + currency + '.png'" 
      alt="Currency Image" 
      style="cursor: pointer; margin-right: 20px;">
  </div>
</div>


    </div>
    <div v-if="selectedExchangeRate" class="exchange-rate-details">
      <h2 class="currency-title">{{ selectedExchangeRate.cur_unit }}</h2>
      <div class="exchange-rate-row">
        <div class="exchange-rate-item">
          <span class="label">송금 받을 때</span>
          <span class="value">{{ selectedExchangeRate.ttb }}</span>
        </div>
        <div class="exchange-rate-item">
          <span class="label">송금 보낼 때</span>
          <span class="value">{{ selectedExchangeRate.tts }}</span>
        </div>
        <div class="exchange-rate-item">
          <span class="label">매매기준율</span>
          <span class="value">{{ selectedExchangeRate.deal_bas_r }}</span>
        </div>
      </div>
      <div class="calculation-container">
        <div class="input-container">
          <label for="amount" class="input-label">사시는 금액(외화)</label>
          <div class="input-box-with-unit">
            <input type="number" v-model="wanttobuy" id="amount" class="input-box" />
            <p class="currency-unit">{{ selectedCurrencyUnit }}</p>
          </div>
        </div>
        <div class="input-container">
          <label for="calculationMethod" class="input-label">계산방식</label>
          <select v-model="calculationMethod" id="calculationMethod" class="input-box">
            <option value="deal_bas_r">매매기준율</option>
            <option value="ttb">송금 받을 때</option>
            <option value="tts">송금 보낼 때</option>
          </select>
        </div>
        <div class="result-container">
          <span class="label">결제금액(원화)</span>
          <span class="value">{{ formattedResult }}원</span>
        </div>
      </div>
    </div>
    <div v-if="error" class="error-message">
      <p>{{ error }}</p>
    </div>
    <div v-if="loading" class="loading-indicator">
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import axios from 'axios';

const currencies = [
  'USD', 'JPY(100)', 'EUR', 'GBP', 'CAD', 'CHF', 'HKD', 'AUD', 'CNH', 'SGD', 'NZD', 'THB'
];

const currencyname = [
  '미국달러', '일본엔', '유럽유로', '영국파운드', '캐나다달러', '스위스프랑', '홍콩달러', '호주달러', '중국위안', '싱가폴달러', '뉴질랜드달러', '태국바트'
];

const currencyUnits = {
  'USD': '달러',
  'JPY(100)': '백엔',
  'EUR': '유로',
  'GBP': '파운드',
  'CAD': '캐나다 달러',
  'CHF': '스위스 프랑',
  'HKD': '홍콩 달러',
  'AUD': '호주 달러',
  'CNH': '위안',
  'SGD': '싱가포르 달러',
  'NZD': '뉴질랜드 달러',
  'THB': '바트'
};

const selectedExchangeRate = ref(null);
const selectedCurrencyUnit = ref('');
const error = ref(null);
const loading = ref(false);
const wanttobuy = ref(null); // null로 초기화
const calculationMethod = ref('deal_bas_r');

const fetchExchangeRate = async (curUnit, curUnitName) => {
  loading.value = true;
  error.value = null;
  selectedExchangeRate.value = null;
  selectedCurrencyUnit.value = curUnitName;

  try {
    const response = await axios.get(`http://127.0.0.1:8000/exchange/${curUnit}/`);
    selectedExchangeRate.value = response.data;
  } catch (err) {
    error.value = '데이터를 가져오는 중 오류가 발생했습니다.';
    console.error(err);
  } finally {
    loading.value = false;
  }
};

const calculateResult = () => {
  if (!selectedExchangeRate.value || !wanttobuy.value) return 0; // 값이 null이면 계산하지 않음
  const rate = Number(selectedExchangeRate.value[calculationMethod.value].replace(/,/g, '')); // 콤마 제거 후 숫자로 변환
  const amount = parseFloat(wanttobuy.value); // 입력된 값이 숫자인지 확인
  if (isNaN(amount)) { // 숫자가 아닌 경우
    error.value = '올바른 숫자를 입력하세요.'; // 오류 메시지 표시
    return 0;
  }
  return rate * amount;
};

const formattedResult = computed(() => {
  const result = calculateResult();
  return new Intl.NumberFormat().format(result);
});
</script>

<style scoped>
.exchange-rates-container {
  max-width: 1800px;
  margin: 100px auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  align-items: center;
}

.title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  text-align: center;
}

.cny {
  margin: 30px auto;
  text-align: center;
}

.button-container {
  display: block;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 100px;
  width:1200px;
  margin-bottom: 50px;
  margin: auto;
}

.currency-buttons {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  margin: 20px auto; /* 필요에 따라 조절 */
  justify-content: center; /* 가로 중앙 정렬 */

}

.currency-button {
  flex: 0 0 calc(16.666% - 10px); /* 6개씩 나누어 출력되도록 함 */
  margin-bottom: 30px; /* 내부 요소들 사이의 간격 조절 */
}


.currency-button:hover {
  background-color: #0056b3;
}

.exchange-rate-details {
  margin-top: 40px;
  background-color: #f4f4f4;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.exchange-rate-row {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-bottom: 1.5rem;
}

.exchange-rate-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.label {
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.value {
  font-size: 1.2rem;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 0.5rem;
  width: 200px;
  text-align: center;
}

.calculation-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 100%;
}

.input-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 1.5rem;
  position: relative;
}

.input-box-with-unit {
  display: flex;
  align-items: center;
  position: relative;
}

.input-label {
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.input-box {
  font-size: 1.2rem;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 200px;
  text-align: center;
}

.currency-unit {
  font-size: 0.8rem;
  font-weight: bold;
  position: absolute;
  right: 10px;
  bottom: -20px;
}

.result-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 1.5rem;

}

.result-container .label {
  font-weight: bold;
  margin-bottom: 0.5rem;
}


.result-container .value {
  font-size: 1.2rem;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 0.5rem;
  min-width: 200px;
}
</style>