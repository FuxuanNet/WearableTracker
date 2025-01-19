import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/Clothing',
      name: 'Clothing',
      component: () => import('../views/ClothingPage.vue'),
      children: [
        {
          path: '/Clothing/',
          name: 'AllClothes',
          component: () => import('../views/AllClothes.vue'),
        },
        {
          path: '/Clothing/Drying/',
          name: 'Drying',
          component: () => import('../views/AllClothes.vue'),
        },
        {
          path: '/Clothing/Sunning',
          name: 'Sunning',
          component: () => import('../views/AllClothes.vue'),
        },
        {
          path: '/Clothing/Favorite',
          name: 'Favorite',
          component: () => import('../views/AllClothes.vue'),
        },
      ]
    },
  ],
})

export default router
