import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import AddTask from '@/pages/AddTask.vue'

// export const useCounterStore = defineStore('counter', () => {
//   const count = ref(0)
//   const doubleCount = computed(() => count.value * 2)
//   function increment() {
//     count.value++
//   }

//   return { count, doubleCount, increment }
// })

export const useTaskStore = defineStore( "tasks", {
  state: () => ({
    tasks: []
  }),
  actions: {
    AddTask(title){
      this.tasks.push({id: Date.now(), title})
    },
    deleteTask(id){
      this.tasks = this.tasks.filter(t => t.id !== id)
    }
  }
})
