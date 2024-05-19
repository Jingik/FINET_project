<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createBoard">
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()

const createBoard = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/posts/create/`,
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then((response) => {
      console.log(response.data)
      router.push({ name: 'BoardView' })
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>

<style>

</style>
