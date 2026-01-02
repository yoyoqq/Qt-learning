<template>
  <li>
    {{ task.title }}
    <button @click="remove">❌</button>
  </li>
</template>

<script setup>
const props = defineProps(['task'])
const emit = defineEmits(['delete'])


function remove() {
  emit('delete', props.task.id)
}
</script>
