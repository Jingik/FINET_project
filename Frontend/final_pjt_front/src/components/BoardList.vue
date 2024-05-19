<template>
  <div>
    <h3>Board List</h3>
    <BoardListItem 
      v-for="board in store.boards"
      :key="board.id"
      :board="board"
    />
  </div>
</template>

<script setup>
import { usePostStore } from '@/stores/post'
import BoardListItem from '@/components/BoardListItem.vue'

const store = usePostStore()
</script>
