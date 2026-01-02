<template>
    <h2>Add Task</h2>
    <input v-model="title" placeholder="Task title" \>
    <button @click="addTask">Add</button>
</template>

<script setup>
    import {ref} from 'vue'
    import { useTaskStore } from '@/stores/taskStore';
    import { useRoute, useRouter } from 'vue-router';

    const title = ref("")
    const store = useTaskStore()
    const router = useRouter()

    function addTask(){
        store.addTask(title.value)
        router.push("/")
        // console.log("Task:", title.value)
    }
</script>

<style>

</style>