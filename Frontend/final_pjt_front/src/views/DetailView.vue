<template>
  <div>
    <h1>DetailView</h1>
    <div v-if="board">
      <p>{{ board.id }}</p>
      <p>{{ board.title }}</p>
      <p>{{ board.content }}</p>
      <p>{{ board.created_at }}</p>
      <p>{{ board.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const board = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/boards/${route.params.id}/`
  })
    .then((response) => {
      console.log(response.data)
      board.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})

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

