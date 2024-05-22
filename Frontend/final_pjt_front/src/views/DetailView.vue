<template>
  <div class="container">
    <div class="post-buttons">
      <button v-if="isCurrentUserAuthor()" @click="confirmDelete" class="post-button">삭제</button>
      <button v-if="isCurrentUserAuthor()" @click="editBoard" class="post-button">수정</button>
      <router-link :to="{ name: 'BoardView' }"><button class="post-button">뒤로가기</button></router-link>
    </div>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else-if="board" class="post">
      <div class="post-header" style="display: flex; justify-content: space-between">
        <h1 class="post-title">{{ board.title }}</h1>
        <div style="display: flex; flex-direction: column">
          <br>
          <p class="post-meta">
            <span class="post-author">작성자 : {{ board.user.username }}</span>
          </p>
          <p class="post-meta">
            <span class="post-date">{{ formatDate(board.created_at) }}</span>
          </p>
        </div>
      </div>
      <div class="post-body">
        <div class="post-content">{{ board.content }}</div>
        
        <p class="post-meta">
          <img 
            :src="likeslist.includes(board.id) ? '/src/assets/img/filledlike.png' : '/src/assets/img/like.png'" 
            class="likeslist-button" style="height: 20px; width:20px;"
            @click="toggleBoardLike(board.id)" 
            alt="likeslist icon">
          좋아요 <span class="like-count">{{ likeslist.length }}</span>
          댓글 <span class="comment-count">{{ comments.length }}</span>
        </p>
      </div>
      <div class="comments-section">
        <h2>댓글</h2>
        <div v-for="comment in comments" :key="comment.id" class="comment">
          <div class="comment-content">
            <span style="margin-right: auto">
              {{ comment.content }}
              <span class="comment-meta" style="margin-left: 10px">
                {{ comment.user.username }} |
                {{ formatDate(comment.created_at) }}
              </span>
            </span>
            <img  
              :src="commentLikes.includes(comment.id) ? '/src/assets/img/filledlike.png' : '/src/assets/img/like.png'" 
              style="width: 20px; height: 20px; margin-right: 10px;"
              @click="toggleCommentLike(comment.id)" 
              alt="comment likes icon">
            <div v-if="isCurrentUserCommentAuthor(comment)" class="comment-actions">
              <button @click="startEditingComment(comment)" class="post-button">수정</button>
              <button @click="confirmDeleteComment(comment.id)" class="post-button">삭제</button>
            </div>
          </div>
        </div>
        <div v-if="editingComment" class="comment-form">
          <h3>댓글 수정</h3>
          <form @submit.prevent="submitEditedComment">
            <div class="form-group">
              <textarea v-model="editedComment.content" class="form-control" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">댓글 수정</button>
            <button type="button" @click="cancelEditingComment" class="btn btn-secondary">취소</button>
          </form>
        </div>
        <div v-else class="comment-form">
          <h3>댓글 작성</h3>
          <form @submit.prevent="submitComment">
            <div class="form-group">
              <textarea v-model="newComment" class="form-control" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">댓글 작성</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const likeslist = ref([]);
const commentLikes = ref([]);

const board = ref(null);
const loading = ref(true);
const error = ref(null);
const comments = ref([]);
const newComment = ref("");
const editingComment = ref(false);
const editedComment = ref({});

onMounted(async () => {
  await store.fetchCurrentUser();
  await fetchBoard();
  await fetchComments();
  await fetchLikeslist();
});

async function fetchBoard() {
  try {
    const response = await axios.get(`${store.API_URL}/posts/${route.params.id}/`, {
      headers: { Authorization: `Token ${store.token}` },
    });
    board.value = response.data;
  } catch (err) {
    console.error("An error occurred:", err);
    error.value = "Failed to load the board details.";
  } finally {
    loading.value = false;
  }
}

async function fetchComments() {
  try {
    const response = await axios.get(`${store.API_URL}/posts/${route.params.id}/comments/`, {
      headers: { Authorization: `Token ${store.token}` },
    });
    comments.value = response.data;
  } catch (err) {
    console.error("An error occurred:", err);
  }
}

async function fetchLikeslist() {
  try {
    const response = await axios.get(`${store.API_URL}/posts/liked_content/`, {
      headers: { Authorization: `Token ${store.token}` },
    });
    const data = response.data;
    likeslist.value = data.liked_boards.map(board => board.id);
    commentLikes.value = data.liked_comments.map(comment => comment.id);
  } catch (err) {
    console.error("An error occurred while fetching the likes list:", err);
  }
}

function formatDate(dateString) {
  const options = { year: "numeric", month: "long", day: "numeric" };
  return new Date(dateString).toLocaleDateString("ko-KR", options);
}

function isCurrentUserAuthor() {
  return board.value && store.currentUser && board.value.user.id === store.currentUser.id;
}

function isCurrentUserCommentAuthor(comment) {
  return comment.user && store.currentUser && comment.user.id === store.currentUser.id;
}

function toggleBoardLike(boardId) {
  if (likeslist.value.includes(boardId)) {
    likeslist.value = likeslist.value.filter(id => id !== boardId);
    updateBoardLikeslist(boardId, 'unlike');
  } else {
    likeslist.value.push(boardId);
    updateBoardLikeslist(boardId, 'like');
  }
}

async function updateBoardLikeslist(boardId, action) {
  try {
    console.log(`Sending request to ${action} board with ID: ${boardId}`);
    const url = `${store.API_URL}/posts/${action}_board/${boardId}/`;
    const response = await axios.post(url, {}, {
      headers: { Authorization: `Token ${store.token}` },
    });
    console.log('Response status:', response.status);
    if (response.status === 201 && action === 'like') {
      console.log("Board liked successfully.");
    } else if (response.status === 204 && action === 'unlike') {
      console.log("Board unliked successfully.");
    } else if (response.status === 400) {
      console.warn(action === 'like' ? "Already liked" : "Not liked yet");
    }
  } catch (err) {
    console.error(`An error occurred while updating the board likes list: ${err.response ? err.response.data : err.message}`);
  }
}

function toggleCommentLike(commentId) {
  if (commentLikes.value.includes(commentId)) {
    // Unlike the comment
    commentLikes.value = commentLikes.value.filter(id => id !== commentId);
    updateCommentLikeslist(commentId, 'unlike');
  } else {
    // Like the comment
    commentLikes.value.push(commentId);
    updateCommentLikeslist(commentId, 'like');
  }
}

async function updateCommentLikeslist(commentId, action) {
  try {
    console.log(`Sending request to ${action} comment with ID: ${commentId}`);
    const url = `${store.API_URL}/posts/${action}_comment/${commentId}/`;
    const response = await axios.post(url, {}, {
      headers: { Authorization: `Token ${store.token}` },
    });
    console.log('Response status:', response.status);
    if (response.status === 201 && action === 'like') {
      console.log("Comment liked successfully.");
    } else if (response.status === 204 && action === 'unlike') {
      console.log("Comment unliked successfully.");
    } else if (response.status === 400) {
      console.warn(action === 'like' ? "Already liked" : "Not liked yet");
    }
  } catch (err) {
    console.error(`An error occurred while updating the comment likes list: ${err.response ? err.response.data : err.message}`);
  }
}

async function editBoard() {
  router.push({ name: "EditBoardView", params: { id: board.value.id } });
}

async function deleteBoard() {
  try {
    await axios.delete(`${store.API_URL}/posts/${board.value.id}/`, {
      headers: { Authorization: `Token ${store.token}` },
    });
    router.push({ name: "BoardView" });
  } catch (err) {
    console.error("An error occurred:", err);
  }
}

function confirmDelete() {
  if (confirm("정말로 이 게시물을 삭제하시겠습니까?")) {
    deleteBoard();
  }
}

function startEditingComment(comment) {
  editingComment.value = true;
  editedComment.value = { ...comment };
}

function cancelEditingComment() {
  editingComment.value = false;
  editedComment.value = {};
}

async function submitComment() {
  try {
    const response = await axios.post(`${store.API_URL}/posts/${board.value.id}/comments/`, {
      content: newComment.value,
    }, {
      headers: { Authorization: `Token ${store.token}` },
    });
    comments.value.push(response.data);
    newComment.value = "";
  } catch (err) {
    console.error("An error occurred while submitting the comment:", err);
  }
}

async function submitEditedComment() {
  try {
    const response = await axios.put(`${store.API_URL}/posts/${board.value.id}/comments/${editedComment.value.id}/`, {
      content: editedComment.value.content,
    }, {
      headers: { Authorization: `Token ${store.token}` },
    });
    const index = comments.value.findIndex((c) => c.id === editedComment.value.id);
    comments.value[index] = response.data;
    editingComment.value = false;
    editedComment.value = {};
  } catch (err) {
    console.error("An error occurred while editing the comment:", err);
  }
}

async function deleteComment(commentId) {
  try {
    await axios.delete(`${store.API_URL}/posts/${board.value.id}/comments/${commentId}/`, {
      headers: { Authorization: `Token ${store.token}` },
    });
    comments.value = comments.value.filter((comment) => comment.id !== commentId);
  } catch (err) {
    console.error("An error occurred while deleting the comment:", err);
  }
}

function confirmDeleteComment(commentId) {
  if (confirm("정말로 이 댓글을 삭제하시겠습니까?")) {
    deleteComment(commentId);
  }
}
</script>

<style scoped>
.container {
  max-width: 1300px;
  margin: 0 auto;
  padding: 50px 20px;
}

.loading,
.error {
  text-align: center;
  font-size: 24px;
  color: red;
}

.post {
  border: 1px solid #e1e1e1;
  border-radius: 8px;
  margin-bottom: 20px;
  background-color: #fff;
}

.post-header {
  padding: 20px;
  border-bottom: 1px solid #e1e1e1;
}

.post-title {
  font-size: 32px;
  font-weight: bold;
  color: #000;
}

.post-meta {
  font-size: 14px;
  color: #464646;
}

.post-body {
  padding: 20px;
}

.post-content {
  font-size: 16px;
  margin: 20px 0;
}

.post-buttons {
  display: flex;
  flex-direction: row-reverse;
  gap: 10px;
  margin-bottom: 5px;
}

.post-button {
  background-color: white;
  border: 1px solid #828282;
}

.comments-section {
  padding: 20px;
  border-top: 1px solid #e1e1e1;
}

.comment {
  margin-bottom: 15px;
  padding: 10px;
  border-top: 1px solid #ddd;
}

.comment-content {
  display: flex;
  font-size: 14px;
}

.comment-meta {
  font-size: 12px;
  color: #888;
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

@media (max-width: 767px) {
  .likeslist-button {
    position: static; /* 작은 화면에서는 버튼의 위치를 고정하지 않음 */
    margin-top: 10px; /* 버튼 위에 여백 추가 */
  }
}
</style>
