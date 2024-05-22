import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';
import { useUserStore } from "@/stores/user";

export const usePostStore = defineStore('post', () => {
  const API_URL = 'http://127.0.0.1:8000/posts';
  const useuserstroe = useUserStore()
  const token = computed(()=>{
    return useuserstroe.token
})
  const boards = ref([]);

  // 게시판 목록 가져오기
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

  // 게시판 생성
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

  return { API_URL, boards, fetchBoards, createBoard, token };
}, { persist: true });
