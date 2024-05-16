<template>
  <div id="app">
    <!-- <NavigationHeader /> -->
    <main class="main-content">
      <RouterView />
    </main>
    <NavigationFooter />
  </div>
</template>

<script setup>
// import NavigationHeader from './components/NavigationHeader.vue'
import NavigationFooter from './components/NavigationFooter.vue'
import { RouterView } from 'vue-router'
</script>

<style src="@/assets/global.css"></style>
