<template>
    <div>
      <NavigationHeader />
      <RouterLink :to="{ name: 'maps' }">지도</RouterLink> |
      <RouterView />
    </div>
    <NavigationFooter />
  </template>
  
  <script setup>
  import NavigationFooter from './components/NavigationFooter.vue'
  import NavigationHeader from './components/NavigationHeader.vue'
  import { RouterView, RouterLink } from 'vue-router'
  </script>
  