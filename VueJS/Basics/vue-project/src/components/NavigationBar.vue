<template>
  <!-- navigation section -->
  <nav>
    <!-- links to an URL path not to the component file -->
     <!-- the link happens in the router/index.js -->
    <router-link to="/">Home</router-link> | <router-link to="/add">Add Task</router-link> |
    <router-link to="/login">Login</router-link>
  </nav>
</template>

<style scoped>
nav {
  padding: 50px;
}
</style>
