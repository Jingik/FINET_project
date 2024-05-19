<template>
  <div>
    <h3>Board List</h3>
    <div v-if="store.boards.length === 0">No boards available.</div>
    <div v-else>
      <BoardListItem 
        v-for="board in store.boards"
        :key="board.id"
        :board="board"
      />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { usePostStore } from '@/stores/post';
import BoardListItem from '@/components/BoardListItem.vue';

const store = usePostStore();

onMounted(() => {
  store.fetchBoards();
});
</script>
