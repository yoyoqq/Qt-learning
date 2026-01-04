<script setup>
import { ref, onMounted } from 'vue'
import { fetchItems, deleteItem } from '../services/api.js'

const items = ref([])
const loading = ref(true)
const error = ref(null)

const loadItems = async () => {
  loading.value = true
  error.value = null
  try {
    items.value = await fetchItems()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

const removeItem = async (id) => {
  try {
    await deleteItem(id)
    items.value = items.value.filter(item => item.id !== id)
  } catch (err) {
    alert(err.message)
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
        {{ item.name }} - €{{ item.price }}
        <button @click="removeItem(item.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>
