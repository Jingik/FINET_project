import { defineStore } from 'pinia';
import axios from 'axios';
import { ref } from 'vue';

export const useExchangeStore = defineStore('exchange', () => {
    const API_URL = 'http://127.0.0.1:8000';
    const currencies = ['USD', 'JPY', 'EUR', 'GBP', 'CAD', 'CHF', 'HKD', 'AUD', 'CNY', 'SGD', 'NZD', 'THB'];
    const exchangerates = ref([]);
    const selectedExchangeRate = ref(null);

    const getExchange = function () {
        axios.get(`${API_URL}/exchange/`)
          .then(response => {
            exchangerates.value = response.data.map(item => ({
              cur_unit: item.cur_unit,
              ttb: item.ttb,
              tts: item.tts,
              deal_bas_r: item.deal_bas_r
            }));
          })
          .catch(error => {
            console.log(error);
          });
      };
      

    const getExchangeByUnit = function (cur_unit) {
        const exchangeRate = exchangerates.value.find(rate => rate.cur_unit === cur_unit);
        if (exchangeRate) {
            selectedExchangeRate.value = exchangeRate;
        } else {
            selectedExchangeRate.value = null;
        }
    };

    return { currencies, API_URL, getExchange, exchangerates, selectedExchangeRate, getExchangeByUnit };
}, { persist: true });
