<!-- <script setup>
import { ref, onMounted } from 'vue'

const items = ref([])
const loading = ref(true)
const error = ref(null)

// async function returns data from FastAPI
const fetchItems = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/items')

    if (!response.ok) {
      throw new Error('Failed to fetch items')
    } 

    items.value = await response.json()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

// mount it to the DOM  
onMounted(() => {
  fetchItems()
})
</script>

<template>
  <div>
    <h1>Items</h1>

    <p v-if="loading">Loading...</p>
    <p v-if="error">{{ error }}</p>

    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }} — €{{ item.price }}
      </li>
    </ul>
  </div>
</template>


<style scoped></style> -->
<!-- scoped style only to this component -->

<!-- 
<script setup>

import {ref, onMounted} from "vue"

const items = ref([])
const loading = ref(true)
const error = ref(null)

const fetchItems = async () => {
  try{
    const response = await fetch("http://127.0.0.1:8000/items")
    if (!response.ok){
      throw new Error("failed fetch items")
    } 
    items.value = await response.json()
    } catch (err){
      error.value = err.message
    } finally {
      loading.value = false
    }
}

onMounted(() => {
  fetchItems()
})

</script>


<template>
  <div>
    <h1>ITEMS</h1>

    <p v-if="loading">loading...</p>
    <p v-if="error">{{ error }}</p>

    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }} - {{ item.price }}
      </li>
    </ul>
  </div>
</template> -->


<!-- <template>

  <div id="app">
    <h1>Playsground</h1>
    <ItemList />
  </div>
  
</template>

<script setup>
  import ItemList from "./components/ItemList.vue"

</script> -->


<script setup>
// import {ref} from "vue"
// import Items from "./components/ItemsManager.vue"
// import ItemList from './components/ItemList.vue'
// import AddItem from './components/AddItem.vue'
import LogIn from './components/LogIn.vue';

// const reloadList = ref(0) // trigger reload
</script>

<template>
  <LogIn />
  <!-- <Items /> -->
  <!-- <div>
    <h1>My FastAPI + Vue App</h1>
    <AddItem @item-added="reloadList++" />
    <ItemList :key="reloadList" />
  </div> -->
</template>
