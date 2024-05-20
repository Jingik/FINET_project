<template>
  <div class="container">
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else-if="board" class="card my-4">
      <div class="card-body">
        <h5 class="card-title">{{ board.title }}</h5>
        <hr>
        <p class="card-text">
          <small class="text-muted">
            작성자: {{ board.user_name }} | 작성일: {{ formatDate(board.created_at) }}
          </small>
        </p>
        <p class="card-text" style="padding-top: 50px; padding-bottom: 50px;">{{ board.content }}</p>
        <router-link :to="{ name: 'BoardView' }" class="btn btn-primary">뒤로가기</router-link>
        <button v-if="isCurrentUserAuthor()" @click="editBoard" class="btn btn-warning">수정</button>
        <button v-if="isCurrentUserAuthor()" @click="confirmDelete" class="btn btn-danger">삭제</button>
      </div>
      <!-- 댓글 목록 -->
      <div class="comments">
        <h5>댓글</h5>
        <div v-for="comment in comments" :key="comment.id" class="comment">
          <p>{{ comment.content }}</p>
          <small class="text-muted">작성자: {{ comment.user_name }} | 작성일: {{ formatDate(comment.created_at) }}</small>
          <div class="comment-actions">
            <button v-if="isCurrentUserCommentAuthor(comment)" @click="startEditingComment(comment)" class="btn btn-warning btn-sm">수정</button>
            <button v-if="isCurrentUserCommentAuthor(comment)" @click="confirmDeleteComment(comment.id)" class="btn btn-danger btn-sm">삭제</button>
          </div>
        </div>
      </div>
      <!-- 댓글 작성 폼 -->
      <div class="comment-form">
        <h5>댓글 작성</h5>
        <form @submit.prevent="submitComment">
          <div class="form-group">
            <textarea v-model="newComment" class="form-control" rows="3" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary">댓글 작성</button>
        </form>
      </div>
      <!-- 댓글 수정 폼 -->
      <div v-if="editingComment" class="comment-form">
        <h5>댓글 수정</h5>
        <form @submit.prevent="submitEditedComment">
          <div class="form-group">
            <textarea v-model="editedComment.content" class="form-control" rows="3" required></textarea>
          </div>
          <button type="submit" class="btn btn-warning">댓글 수정</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router';

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const board = ref(null);
const loading = ref(true);
const error = ref(null);
const comments = ref([]);
const newComment = ref('');
const editingComment = ref(false);
const editedComment = ref({});

onMounted(async () => {
  await store.fetchCurrentUser();
  await fetchBoard();
  await fetchComments();
});

async function fetchBoard() {
  try {
    const response = await axios.get(`${store.API_URL}/posts/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    board.value = response.data;
  } catch (err) {
    console.error('An error occurred:', err);
    error.value = 'Failed to load the board details.';
  } finally {
    loading.value = false;
  }
}

async function fetchComments() {
  try {
    const response = await axios.get(`${store.API_URL}/posts/${route.params.id}/comments/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    comments.value = response.data;
  } catch (err) {
    console.error('An error occurred:', err);
  }
}

function formatDate(dateString) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString('ko-KR', options);
}


function isCurrentUserAuthor() {
  return board.value && store.currentUser && board.value.user.id === store.currentUser.id;
}



function isCurrentUserCommentAuthor(comment) {
  return comment.user && store.currentUser && comment.user.id === store.currentUser.id;
}


async function editBoard() {
  router.push({ name: 'EditBoardView', params: { id: board.value.id } });
}

async function deleteBoard() {
  try {
    await axios.delete(`${store.API_URL}/posts/${board.value.id}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    router.push({ name: 'BoardView' });
  } catch (err) {
    console.error('An error occurred:', err);
  }
}

function confirmDelete() {
  if (confirm('정말로 이 게시물을 삭제하시겠습니까?')) {
    deleteBoard();
  }
}

function startEditingComment(comment) {
  editingComment.value = true;
  editedComment.value = { ...comment };
}

async function submitComment() {
  try {
    const response = await axios.post(`${store.API_URL}/posts/${board.value.id}/comments/`, {
      content: newComment.value
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    comments.value.push(response.data);
    newComment.value = '';
  } catch (err) {
    console.error('An error occurred while submitting the comment:', err);
  }
}

async function submitEditedComment() {
  try {
    const response = await axios.put(`${store.API_URL}/posts/${board.value.id}/comments/${editedComment.value.id}/`, {
      content: editedComment.value.content
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    const index = comments.value.findIndex(c => c.id === editedComment.value.id);
    comments.value[index] = response.data;
    editingComment.value = false;
    editedComment.value = {};
  } catch (err) {
    console.error('An error occurred while editing the comment:', err);
  }
}

async function deleteComment(commentId) {
  try {
    await axios.delete(`${store.API_URL}/posts/${board.value.id}/comments/${commentId}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    comments.value = comments.value.filter(comment => comment.id !== commentId);
  } catch (err) {
    console.error('An error occurred while deleting the comment:', err);
  }
}

function confirmDeleteComment(commentId) {
  if (confirm('정말로 이 댓글을 삭제하시겠습니까?')) {
    deleteComment(commentId);
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  padding-top: 150px;
  padding-bottom: 150px;
}

.card {
  border-radius: 10px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  width: 800px;
  margin: 0 auto;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

.card-title {
  font-weight: bold;
  font-size: 60px;
}

.card-text {
  font-size: 30px;
}

.text-muted {
  font-size: 0.9rem;
}

.comments {
  margin-top: 30px;
}

.comment {
  margin-bottom: 15px;
  padding: 10px;
  border-top: 1px solid #ddd;
}

.comment-actions {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.comment-form {
  margin-top: 30px;
}

.comment-form textarea {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn-sm {
  margin-left: 10px;
}
</style>
