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
import { useCounterStore } from '@/stores/counter'
import BoardListItem from '@/components/BoardListItem.vue'

const store = useCounterStore()
</script>
