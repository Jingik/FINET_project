<template>
    <div v-if="show" class="modal-overlay">
      <div class="modal-container">
        <div class="modal-header">
          <h3>{{ title }}</h3>
          <button class="close-button" @click="closeModal">X</button>
        </div>
        <div class="modal-body">
          <p>{{ message }}</p>
        </div>
        <div class="modal-footer">
          <button class="ok-button" @click="closeModal">확인</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const props = defineProps({
    show: Boolean,
    title: String,
    message: String,
  })
  
  const emit = defineEmits(['close'])
  
  const closeModal = () => {
    emit('close')
  }
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal-container {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    width: 300px;
    text-align: center;
  }
  
  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .close-button {
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
  }
  
  .modal-body {
    margin-bottom: 20px;
  }
  
  .ok-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
  }
  </style>
  