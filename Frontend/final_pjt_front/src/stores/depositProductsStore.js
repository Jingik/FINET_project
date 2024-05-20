// src/stores/depositProducts.js
import { defineStore } from 'pinia';
import axios from 'axios';

export const useDepositProductsStore = defineStore('depositProducts', {
  state: () => ({
    products: [],
    loading: false,
    error: null,
  }),
  actions: {
    async fetchDepositProducts() {
      this.loading = true;
      this.error = null;
      try {
        const response = await axios.get('http://127.0.0.1:8000/financial/save-deposit-products/');
        this.products = response.data;
      } catch (error) {
        this.error = error.message || 'Something went wrong';
      } finally {
        this.loading = false;
      }
    },
  },
});
