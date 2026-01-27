<script setup>
import { ref } from 'vue';

const show = ref(true);
const list = ref([1, 2, 3])
</script>

<template>
    <button @click="show = !show"> Toggle list </button>
    <button @click="list.push(list.length + 1)"> Add item </button>
    <button @click="list.pop()"> Remove item</button>
    <button @click="list.reverse()"> Reverse list </button>

    <!-- show the list -->
    <ul v-if="show && list.length">
        <!-- <li v-for="item of list">{{ item }}</li> -->
        <li v-for="item in list" :key="item"> {{ item }}</li>
    </ul>
    <p v-else-if="list.length"> List is not empty but hidden </p>
    <p v-else> list is empty </p>
    
</template>

<style scoped>

</style>