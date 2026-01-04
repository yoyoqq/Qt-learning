<script setup>
import { ref, onMounted } from 'vue'
import { fetchItems } from '../services/api.js'

const items = ref([])
const loading = ref(true)
const error = ref(null)

const loadItems = async () => {
  try {
    items.value = await fetchItems()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadItems()
})
</script>

<template>
  <div>
    <h2>Items</h2>
    <p v-if="loading">Loading...</p>
    <p v-if="error">{{ error }}</p>

    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }} - {{ item.price }}
      </li>
    </ul>
  </div>
</template>
