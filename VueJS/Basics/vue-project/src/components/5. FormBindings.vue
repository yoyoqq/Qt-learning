<script setup>
import { ref } from 'vue';

const text = ref('Edit me')
const checked = ref(true)
const checkedNames = ref([])
const picked = ref('One')
const selected = ref()
const multiSelected = ref([])

</script>

<template>
    <!-- v-model, binds the input with the value -->
    <h2> Text Input </h2>
    <input v-model="text"> 
    <p>{{ text }}</p>

    <h2> Checkbox </h2>
    <input type="checkbox" id="checkbox" v-model="checked"> 
    <label for="checkbox"> Checked: {{ checked }}</label>     <!-- associate with a form control --> 
    
    <!-- multi check box  -->
    <h2> Multi checkbox </h2>
    <input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
    <label for="jack"> Jack </label>
    <input type="checkbox" id="john" value="John" v-model="checkedNames">
    <label for="john"> John </label>
    <input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
    <label for="mike"> Mike </label>
    <p> Checked names: {{ checkedNames }}</p>

    <!-- radio  -->
    <h2> Radio buttons </h2>
    <input type="radio" id="one" v-model="picked" value="One">
    <label for="one"> One </label>
    <input type="radio" id="two" v-model="picked" value="Two">
    <label for="two"> Two </label>
    <p> Picked: {{ picked }} </p>

    <!-- select from many  -->
    <select v-model="selected">
        <option disabled value="">Select One</option>
        <option> A </option>
        <option> B </option>
        <option> C </option>
    </select>
    <p> Selected: {{ selected }}</p>

    <!-- multi select  -->  
    <h2> Multi Select </h2>
    <select v-model="multiSelected" multiple style="width: 100px">
        <option> A </option>
        <option> B </option>
        <option> C </option>
        </select>
    <p> Multi Selected: {{ multiSelected }}</p> 
    

</template>

<style scoped>

</style>