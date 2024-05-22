import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';
import { useUserStore } from "@/stores/user";

export const useCounterStore = defineStore('counter', () => {
  const boards = ref([]);
  const currentUser = ref(null);
  const useuserstore = useUserStore();
  const token = computed(() => useuserstore.token);
  const API_URL = 'http://127.0.0.1:8000';

  const getBoards = async () => {
    try {
      const response = await axios.get(`${API_URL}/posts`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      boards.value = response.data;
    } catch (error) {
      console.error('Error fetching boards:', error);
    }
  };

  const fetchCurrentUser = async () => {
    try {
      const response = await axios.get(`${API_URL}/users/me/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      currentUser.value = response.data;
    } catch (error) {
      console.error('An error occurred while fetching the current user:', error);
    }
  };

  
  const subscribeToProduct = async (depositId) => {
    if (!token.value) {
      throw new Error('User not authenticated');
    }
    try {
      // console.log('Attempting to subscribe with token:', token.value);
      const response = await axios.post(
        `${API_URL}/financial/subscribe_deposit/${depositId}/`,
        {},
        {
          headers: {
            Authorization: `Token ${token.value}`
          }
        }
      );
      return response.data;
    } catch (error) {
      if (error.response && error.response.data) {
        throw new Error(error.response.data.detail);
      } else {
        throw new Error('An error occurred while subscribing to the product');
      }
    }
  };

  const isSubscribedToProduct = async (depositId) => {
    if (!token.value) {
      throw new Error('User not authenticated');
    }
    try {
      console.log('Checking subscription status for product:', depositId);
      const response = await axios.get(`${API_URL}/financial/check_subscription/${depositId}/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      console.log('Subscription status response:', response.data);
      return response.data.is_subscribed;
    } catch (error) {
      console.error('Error checking subscription:', error);
      return false;
    }
  };


  const savingsubscribeToProduct = async (savingId) => {
    if (!token.value) {
      throw new Error('User not authenticated');
    }
    try {
      // console.log('Attempting to subscribe with token:', token.value);
      const response = await axios.post(
        `${API_URL}/financial/subscribe_saving/${savingId}/`,
        {},
        {
          headers: {
            Authorization: `Token ${token.value}`
          }
        }
      );
      return response.data;
    } catch (error) {
      if (error.response && error.response.data) {
        throw new Error(error.response.data.detail);
      } else {
        throw new Error('An error occurred while subscribing to the product');
      }
    }
  };

  const savingisSubscribedToProduct = async (savingId) => {
    if (!token.value) {
      throw new Error('User not authenticated');
    }
    try {
      console.log('Checking subscription status for product:', savingId);
      const response = await axios.get(`${API_URL}/financial/check_subscription/${savingId}/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      console.log('Subscription status response:', response.data);
      return response.data.is_subscribed;
    } catch (error) {
      console.error('Error checking subscription:', error);
      return false;
    }
  };


  const creditloansubscribeToProduct = async (creditloanId) => {
    if (!token.value) {
      throw new Error('User not authenticated');
    }
    try {
      // console.log('Attempting to subscribe with token:', token.value);
      const response = await axios.post(
        `${API_URL}/financial/subscribe_creditloan/${creditloanId}/`,
        {},
        {
          headers: {
            Authorization: `Token ${token.value}`
          }
        }
      );
      return response.data;
    } catch (error) {
      if (error.response && error.response.data) {
        throw new Error(error.response.data.detail);
      } else {
        throw new Error('An error occurred while subscribing to the product');
      }
    }
  };

  const creditloanisSubscribedToProduct = async (creditloanId) => {
    if (!token.value) {
      throw new Error('User not authenticated');
    }
    try {
      console.log('Checking subscription status for product:', creditloanId);
      const response = await axios.get(`${API_URL}/financial/check_subscription/${creditloanId}/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      console.log('Subscription status response:', response.data);
      return response.data.is_subscribed;
    } catch (error) {
      console.error('Error checking subscription:', error);
      return false;
    }
  };



  // const fetchProducts = async () => {
  //   try {
  //     const response = await axios.get(`${API_URL}/financial/deposit-products/`);
  //     return response.data;
  //   } catch (error) {
  //     if (error.response && error.response.data) {
  //       throw new Error(error.response.data.detail);
  //     } else {
  //       throw new Error('An error occurred while fetching the products');
  //     }
  //   }
  // };

  return {
    boards,
    currentUser,
    token,
    API_URL,
    getBoards,
    fetchCurrentUser,
    subscribeToProduct,
    // fetchProducts,
    isSubscribedToProduct,
    savingsubscribeToProduct,
    savingisSubscribedToProduct,
    creditloanisSubscribedToProduct,
    creditloansubscribeToProduct,
  };
}, { persist: true });
