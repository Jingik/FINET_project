<template>
  <div class="board-item">
    <h4>{{ board.title }}</h4>
    <p>{{ board.content }}</p>
    <router-link :to="{ name: 'DetailView', params: { id: board.id } }">View Details</router-link>
  </div>
</template>

<script setup>
defineProps({
  board: {
    type: Object,
    required: true
  }
});
</script>

<style scoped>
.board-item {
  padding: 10px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
  border-radius: 5px;
}
</style>
