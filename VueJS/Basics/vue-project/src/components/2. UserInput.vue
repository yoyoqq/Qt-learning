<script setup>  
import { ref } from 'vue';

const msg = ref('User Input Component');

function reverseMessage(){
    msg.value = msg.value.split("").reverse().join("");
}

function notify(){
    alert("Button clicked!");
}

</script>

<template>
    <div></div>
    <h1> {{ msg }}</h1>

    <button @click="reverseMessage"> REVERSE MSG BUTTON </button>
    <button @click="msg += '!'"> ADD EXCML </button>
    <a href="" @click.prevent="notify"> CLICK ME </a>
</template>

<style scoped>
button {
    display: block;
    margin-bottom: 1em;
}
</style>