<template>
  <div class="container">
    <h1>Edit Board</h1>
    <form @submit.prevent="updateBoard">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" class="form-control" id="title" v-model="editedBoard.title" required>
      </div>
      <div class="form-group">
        <label for="content">Content:</label>
        <textarea class="form-control" id="content" v-model="editedBoard.content" rows="6" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Update</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const route = useRoute();
const router = useRouter();
const editedBoard = ref({ title: '', content: '' });
const store = useCounterStore();

onMounted(async () => {
  try {
    const response = await axios.get(`${store.API_URL}/posts/${route.params.id}/`);
    editedBoard.value = response.data;
  } catch (err) {
    console.error('An error occurred:', err);
  }
});

async function updateBoard() {
  try {
    await axios.put(`${store.API_URL}/posts/${route.params.id}/update/`, editedBoard.value);
    router.push({ name: 'DetailView', params: { id: route.params.id } });
  } catch (err) {
    console.error('An error occurred:', err);
  }
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.form-group {
  margin-bottom: 15px;
}
.form-control {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
