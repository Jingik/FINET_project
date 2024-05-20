import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const boards = ref([])
  const currentUser = ref(null)
  const token = ref(null)
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

  const fetchCurrentUser = async function () {
    try {
      const response = await axios.get(`${API_URL}/users/me/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      currentUser.value = response.data
    } catch (err) {
      console.error('An error occurred while fetching the current user:', err)
    }
  }

  const setToken = function (newToken) {
    token.value = newToken
  }

  return { boards, currentUser, token, API_URL, getBoards, fetchCurrentUser, setToken }
}, { persist: true })
