import { createRouter, createWebHistory } from 'vue-router'
import Home from "../pages/Home.vue"
import AddTask from '@/pages/AddTask.vue'
import Login from '@/pages/Login.vue'

const routes = [
  { path: "/", component: Home}, 
  { path: "/add", component: AddTask},
  { path: "/login", component: Login}
]

export default createRouter({
  history: createWebHistory(),
  routes
})

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes,
// })

// export default router
