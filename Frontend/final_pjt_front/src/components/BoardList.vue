<template>
  <div class="board-list">
    <div v-if="boards.length > 0">
      <div v-for="board in boards" :key="board.id" class="board-item">
        <RouterLink :to="{ name: 'DetailView', params: { id: board.id } }">
          <h3>{{ board.title }}</h3>
          <p>{{ board.user.name }}</p>
          <p>{{ board.content }}</p>
        </RouterLink>
      </div>
      <div class="pagination">
        <button @click="fetchBoards(prevPageUrl)" :disabled="!prevPageUrl">Previous</button>
        <button @click="fetchBoards(nextPageUrl)" :disabled="!nextPageUrl">Next</button>
      </div>
    </div>
    <div v-else>
      <p>첫 번째 글을 작성해 주세요.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const boards = ref([])
const nextPageUrl = ref(null)
const prevPageUrl = ref(null)

const fetchBoards = async (url = `${store.API_URL}/posts/`) => {
  try {
    const response = await axios.get(url)
    boards.value = response.data.results
    nextPageUrl.value = response.data.next
    prevPageUrl.value = response.data.previous
  } catch (error) {
    console.error('Error fetching boards:', error)
  }
}

onMounted(() => {
  fetchBoards()
})
</script>

<style scoped>
.board-list {
  display: flex;
  flex-direction: column;
}

.board-item {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.board-item h3 {
  margin: 0;
  font-size: 1.2em;
  color: #333;
}

.board-item p {
  margin: 0;
  color: #666;
}

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.pagination button {
  margin: 0 5px;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.pagination button:hover:not(:disabled) {
  background-color: #0056b3;
}
</style>
