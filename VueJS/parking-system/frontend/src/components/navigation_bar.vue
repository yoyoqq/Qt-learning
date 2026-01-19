<script lang="ts" setup>

</script>


<template>
    <nav class="flex items-center justify-between px-6 py-4 bg-blue-600 shadow-lg">
        <RouterLink to="/" class="hover:opacity-80 transition">
            <img src="@/images/icon.png" alt="Back" class="h-6 w-6">
        </RouterLink>
        <div class="flex gap-8 items-center">
            <RouterLink to="/" class="text-white font-medium hover:text-blue-100 transition">
                Home
            </RouterLink>
            <RouterLink to="/" class="text-white font-medium hover:text-blue-100 transition">
                Stats
            </RouterLink>
        </div>
    </nav>
</template>


<style scoped>
</style>