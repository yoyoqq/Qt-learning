import { createRouter, createWebHistory } from 'vue-router'
import ItemList from '@/components/ItemList.vue'
import LogIn from '@/components/LogIn.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ItemList
    },
    {
      path: '/login',
      name: 'login',
      component: LogIn
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/'
    }
  ],
})

export default router
