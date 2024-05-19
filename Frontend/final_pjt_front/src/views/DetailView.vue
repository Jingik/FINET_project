<template>
  <div>
    <h1>DetailView</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else-if="board">
      <p>ID: {{ board.id }}</p>
      <p>Title: {{ board.title }}</p>
      <p>Content: {{ board.content }}</p>
      <p>Created At: {{ board.created_at }}</p>
      <p>Updated At: {{ board.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRoute } from 'vue-router';

const store = useCounterStore();
const route = useRoute();
const board = ref(null);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    const response = await axios.get(`${store.API_URL}/posts/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    board.value = response.data;
  } catch (err) {
    console.error('An error occurred:', err);
    error.value = 'Failed to load the board details.';
  } finally {
    loading.value = false;
  }
});
</script>

<style>
  /* 게시물 상세보기 스타일 */
  .detail-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
  }

  .detail-container h1 {
    font-size: 24px;
    margin-bottom: 20px;
    color: #333;
  }

  .detail-item {
    margin-bottom: 10px;
  }

  .detail-item p {
    margin: 0;
    font-size: 16px;
    color: #666;
  }

  /* 게시물 내용 스타일 */
  .content {
    margin-top: 20px;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
  }

  .content p {
    margin: 0;
    font-size: 16px;
    line-height: 1.5;
    color: #333;
  }

  /* 날짜 스타일 */
  .date {
    font-style: italic;
    color: #888;
  }
</style>

