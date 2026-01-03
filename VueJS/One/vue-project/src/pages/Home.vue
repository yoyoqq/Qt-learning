<template>
  <h2>Tasks</h2>
  <ul>
    <TaskItem
      v-for="task in store.tasks"
      :key="task.id"
      :task="task"
      @delete="store.deleteTask"
    />
  </ul>

</template>

<script setup>
import { useTaskStore } from '../stores/taskStore'
import TaskItem from '../components/TaskItem.vue'

const store = useTaskStore()
</script>
