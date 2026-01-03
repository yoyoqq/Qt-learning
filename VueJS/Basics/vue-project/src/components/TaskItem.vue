<template>
  <li>
    {{ task.title }}
    <!-- v-on:click -->
    <button @click="remove">❌</button>
  </li>
</template>


<script setup>
// get properties wit hthe following names  
const props = defineProps(['task'])
// emit the event to the parent, delete event 
const emit = defineEmits(['delete'])

function remove() {
  emit('delete', props.task.id)
}
</script>
