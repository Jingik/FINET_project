import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
// import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }


  return { count, doubleCount, increment}
})
