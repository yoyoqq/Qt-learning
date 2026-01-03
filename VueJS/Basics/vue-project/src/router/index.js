import { createRouter, createWebHistory } from 'vue-router'
import Home from "../pages/Home.vue"
import AddTask from '@/pages/AddTask.vue'
import Login from '@/pages/Login.vue'

const routes = [
  { path: "/", component: Home}, 
  { path: "/add", component: AddTask},
  { path: "/login", component: Login}
]

// export -> make available to other files
// export default -> main for module exports 
// createRouter() -> create the router instance 
export default createRouter({
  // mode of routing, HTML5 for /about 
  history: createWebHistory(),
  routes
})

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes,
// })

// export default router
