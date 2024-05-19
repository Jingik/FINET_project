import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const usePostStore = defineStore('post', () => {
  // const boards = ref([])
  const API_URL = 'http://127.0.0.1:8000';
  const token = ref(localStorage.getItem('auth_token') || null);
    // const getBoards = function () {
    // axios({
    //   method: 'get',
    //   url: `${API_URL}/api/v1/posts/`
    // })
    //   .then(response => {
    //     console.log(response)
    //     console.log(response.data)
    //     boards.value = response.data
    //   })
    //   .catch(error => {
    //     console.log(error)
    //   })
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

  return { API_URL, createBoard, token }; //getBoards 추가
}, { persist: true });
