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
import { ref } from 'vue'
import { usePostStore } from '@/stores/post'
import { useRouter } from 'vue-router'

const store = usePostStore()
const title = ref('')
const content = ref('')
const router = useRouter()

const createBoard = async () => {
  try {
    const response = await store.createBoard(title.value, content.value)
    console.log(response)
    router.push({ name: 'BoardView' })
  } catch (error) {
    console.log(error)
  }
}
</script>

<style scoped>
/* 스타일을 여기에 추가하세요 */
</style>
