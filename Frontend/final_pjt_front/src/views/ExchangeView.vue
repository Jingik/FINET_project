<template>
  <div class="exchange-rates-container">
    <h1 class="title">국가별 환율 조회</h1>
    <ul class="cny">
      <li>
        '최종고시환율'은 오늘 기준 가장 최근 고시된 환율정보를 나타내며,
        은행의 환율고시가 종료되지 않은 상태일 수 있습니다.
      </li>
      <li>
        중국 위안화(CNY)는 홍콩 외환시장에서 거래되는 위안화
        환율정보(CNH)를 고시합니다.
      </li>
      <li>일본- 100엔, 베트남 - 100동을 기준으로 합니다.</li>
    </ul>
    <div class="button-container">
      <div class="currency-buttons">
        <button
          v-for="(currency, index) in currencies"
          :key="currency"
          class="currency-button"
          @click="fetchExchangeRate(currency)"
        >
          {{ currencyname[index] }}
        </button>
      </div>
    </div>
    <div v-if="selectedExchangeRate" class="exchange-rate-details">
      <h2 class="currency-title">{{ selectedExchangeRate.cur_unit }}</h2>
      <div class="exchange-rate-item">
        <span class="label">송금 받을 때:</span>
        <span class="value">{{ selectedExchangeRate.ttb }}</span>
      </div>
      <div class="exchange-rate-item">
        <span class="label">송금 보낼 때:</span>
        <span class="value">{{ selectedExchangeRate.tts }}</span>
      </div>
      <div class="exchange-rate-item">
        <span class="label">매매기준율:</span>
        <span class="value">{{ selectedExchangeRate.deal_bas_r }}</span>
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

<script>
import axios from 'axios';

export default {
  data() {
    return {
      currencies: ['USD', 'JPY', 'EUR', 'GBP', 'CAD', 'CHF', 'HKD', 'AUD', 'CNY', 'SGD', 'NZD', 'THB', 'VND', 'TWD', 'PHP'],
      currencyname: ['미국달러', '일본엔', '유럽유로', '영국파운드', '캐나다달러', '스위스프랑', '홍콩달러', '호주달러', '중국위안', '싱가폴달러', '뉴질랜드달러', '태국바트', '베트남동', '대만달러', '필리핀페소'],
      selectedExchangeRate: null,
      error: null,
      loading: false
    };
  },
  methods: {
    fetchExchangeRate(curUnit) {
      this.loading = true;
      axios.get(`/exchange/${curUnit}/`)
        .then(response => {
          this.selectedExchangeRate = {
            cur_unit: response.data.cur_unit,
            ttb: response.data.ttb,
            tts: response.data.tts,
            deal_bas_r: response.data.deal_bas_r
          };
          this.loading = false;
        })
        .catch(error => {
          this.error = '데이터를 가져오는 중 오류가 발생했습니다.';
          this.loading = false;
          console.log(error);
        });
    }
  }
};
</script>


<style>
.exchange-rates-container {
  max-width: 1800px;
  margin: 100pxs auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
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
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: #f4f4f4;
  height:100px
}
.currency-buttons {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;

}

.currency-button {
  padding: 0.75rem 1.5rem;
  margin: 0.5rem;
  background-color: #007ACE;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.currency-button:hover {
  background-color: #0056b3;
}

.exchange-rate-details {
  background-color: #fff;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.currency-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.exchange-rate-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.label {
  font-weight: bold;
  margin-right: 1rem;
}

.value {
  font-size: 1.2rem;
}
</style>
s