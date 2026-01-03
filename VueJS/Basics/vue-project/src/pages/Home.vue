<template>
  <h2>Tasks</h2>
  <ul>
    <!-- loop over tasks in store, each is individual item -->
    <!-- pass item for update -->
    <!-- pass task as prop to TaskItem -->
    <!-- listen event by TaskItem and calls store.deleteTask -->
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
