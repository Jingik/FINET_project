<template>
  <div>
    <h3 style="margin-bottom: 20px;">▼ 글 목록</h3>
    <div v-if="store.boards.length === 0">첫 게시글을 작성해 주세요.</div>
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
