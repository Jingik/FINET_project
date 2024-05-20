// src/stores/depositProducts.js
import { defineStore } from 'pinia';
import axios from 'axios';

  export const useSavingProductsStore = defineStore('savingProducts', {
    state: () => ({
      savings: [],
      loading: false,
      error: null,
    }),
    actions: {
      async fetchSavingsProducts() {
        this.loading = true;
        this.error = null;
        try {
          const response = await axios.get('http://127.0.0.1:8000/financial/saving-products/');
          this.products = response.data;
        } catch (error) {
          this.error = error.message || 'Something went wrong';
        } finally {
          this.loading = false;
        }
      },
  },
});
