import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const usePostStore = defineStore('post', () => {
  const API_URL = 'http://127.0.0.1:8000';
  const token = ref(localStorage.getItem('auth_token') || null);

  const createBoard = async (title, content) => {
    try {
      const response = await axios.post(`${API_URL}/posts/create/`, {
        title: title,
        content: content
      }, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      return response.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  return { API_URL, createBoard, token };
}, { persist: true });
