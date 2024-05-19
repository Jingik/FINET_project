import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const boards = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getBoards = function () {
    axios({
      method: 'get',
      url: `${API_URL}/posts`
    })
      .then(response => {
        console.log(response)
        console.log(response.data)
        boards.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
  return { boards, API_URL, getBoards }
}, { persist: true })
