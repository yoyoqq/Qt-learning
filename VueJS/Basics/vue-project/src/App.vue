<!-- html part component, what appears on screen -->
<!-- <template>       -->
<!-- must be imported before its use  -->
<!-- <Navbar /> -->
<!-- placeholder for the current page, matched page component here -->
<!-- <router-view /> -->
<!-- </template> -->

<template>
  <!-- navbar and footer always visible, pages change in the middle ..  -->
  <Navbar />
  <main>
    <router-view />
    <p>asdfasdfasdf</p>
  </main>
  <Footer />
</template>

<!-- setup means -> run when the component is created -->
<script setup>
import Navbar from './components/NavigationBar.vue'
</script>
