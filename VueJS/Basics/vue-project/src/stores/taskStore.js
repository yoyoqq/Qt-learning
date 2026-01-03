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

// defineStore(storeId, storeDefinition)
// storeId -> unique streing identifier 
// storeDefinition -> object with optional properties  
//    state -> reactive data, must be a function that returns an object 
//    getters -> computer properties (optional)
//    actions -> functionsd that modify state 

// arrow function returns an object       () => ({ tasks: []})
// state: function(){
//   return {
//     tasks: []
//   }
// }

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
