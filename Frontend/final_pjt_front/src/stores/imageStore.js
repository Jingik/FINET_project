import { defineStore } from 'pinia';

export const useImageStore = defineStore('imageStore', {
  state: () => ({
    images: [
      '@/assets/img/img1.jpg',
      '@/assets/img/img2.jpg',
      '@/assets/img/img3.jpg'
    ]
  })})