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

</style>
