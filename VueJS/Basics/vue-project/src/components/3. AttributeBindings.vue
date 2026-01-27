<script setup>
import { ref } from 'vue';

const msg = ref('Hello, Vue 3 Attribute Bindings!');
const isRed = ref(true);
const color = ref("green")

function toggleRed(){
    isRed.value = !isRed.value;
}

function toggleColor() {
  color.value = color.value === 'green' ? 'blue' : 'green'
}

</script>

<template>
    <p>
    <span :title="message">
    Hover your mouse over me for a few seconds to see my dynamically bound title!
    </span>

  <!--
  class bindings have special support for objects and arrays
  in addition to plain strings
  -->
  <p :class="{ red: isRed }" @click="toggleRed">
    This should be red... but click me to toggle it.
  </p>

  <!-- style bindings also support object and arrays -->
  <p :style="{ color }" @click="toggleColor">
    This should be green, and should toggle between green and blue on click.
  </p>
</template>
<style scoped>
.red{
    color: red;
}
</style>