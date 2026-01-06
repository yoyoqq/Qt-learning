<template>
  <div class="items">
    <h2>Items</h2>

    <!-- Input + Button -->
    <input
      v-model="newItem"
      placeholder="Enter item name"
    />
    <input
      v-model="newPrice"
      type="number"
      placeholder="Enter item price"
      step="0.01"
    />
    <button @click="createItem">Add Item</button>

    <!-- Items List -->
    <ul>
      <li v-for="item in items" :key="item.id">
        
        <template v-if="editingId === item.id">
          <input v-model="editValue" />
          <button @click="saveEdit(item.id)">💾</button>
          <button @click="cancelEdit">✖</button>
        </template>

        <template v-else>
          {{ item.name }}
          <button @click="startEdit(item)">✏️</button>
          <button @click="removeItem(item.id)">❌</button>
        </template>

      </li>
    </ul>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getItems, addItem, deleteItem, updateItem } from "@/services/api";

const items = ref([]);
const newItem = ref("");
const newPrice = ref(0);

const fetchItems = async () => {
  const response = await getItems();
  items.value = response.data;
};

const createItem = async () => {
  if (!newItem.value.trim() || !newPrice.value) return;

  await addItem({ name: newItem.value, price: parseFloat(newPrice.value) });
  newItem.value = "";
  newPrice.value = 0;
  await fetchItems(); // refresh list
};

const removeItem = async (id) => {
  await deleteItem(id);
  await fetchItems();
}

// EDIT VALUE 
const editingId = ref(null)
const editValue = ref("")

const startEdit = (item) => {
  editingId.value = item.id;
  editValue.value = item.name;
}

const cancelEdit = () => {
  editingId.value = null;
  editValue.value = "";
}

const saveEdit = async (id) => {
  if (!editValue.value.trim()) return;

  const currentItem = items.value.find(i => i.id === id);
  const response = await updateItem(id, { name: editValue.value, price: currentItem.price });
  const index = items.value.findIndex(i => i.id === id);
  items.value[index] = response.data;

  cancelEdit();
}

onMounted(() => {
  fetchItems();
});
</script>

<style scoped>
.items {
  max-width: 400px;
  margin: auto;
}

input {
  margin-right: 8px;
}
</style>
