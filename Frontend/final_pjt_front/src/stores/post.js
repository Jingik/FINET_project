import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const usePostStore = defineStore('post', () => {
  const API_URL = 'http://127.0.0.1:8000/posts';
  const token = ref(localStorage.getItem('auth_token') || null);
  const boards = ref([]);

  const setToken = (newToken) => {
    token.value = newToken;
    localStorage.setItem('auth_token', newToken);
  };

  const clearToken = () => {
    token.value = null;
    localStorage.removeItem('auth_token');
  };

  const fetchBoards = async () => {
    try {
      const response = await axios.get(API_URL, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      boards.value = response.data.results; // Adjust if the response structure is different
    } catch (error) {
      console.error('Error fetching boards:', error);
    }
  };

  const createBoard = async (title, content) => {
    try {
      const response = await axios.post(`${API_URL}/create/`, {
        title,
        content
      }, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      return response.data;
    } catch (error) {
      console.error('Error creating board:', error);
      throw error;
    }
  };

  return { API_URL, boards, fetchBoards, createBoard, token, setToken, clearToken };
}, { persist: true });
