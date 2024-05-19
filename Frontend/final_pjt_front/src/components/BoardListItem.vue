<template>
  <router-link :to="{ name: 'DetailView', params: { id: board.id } }" class="board-item">
    <div class="bubble">
      <h4 class="board-title">{{ board.title }}</h4>
      <p class="board-info">{{ board.user_name }} | {{ formatDate(board.created_at) }}</p>
    </div>
  </router-link>
  <hr>
</template>

<script setup>
defineProps({
  board: {
    type: Object,
    required: true
  }
});

function formatDate(dateString) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString('ko-KR', options);
}
</script>

<style scoped>
.board-item {
  text-decoration: none; /* 링크 스타일 제거 */
}

.bubble {
  position: relative;
  padding: 15px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

.bubble:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.board-title {
  font-size: 1.2rem;
  margin-bottom: 5px;
}

.board-info {
  font-size: 0.9rem;
  color: #666;
}
</style>