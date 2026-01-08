<script setup>
import { ref } from "vue"
import { useAuthStore } from "@/stores/auth"
import { useRouter } from "vue-router"
import { login } from "@/services/api"

const email = ref("")
const password = ref("")
const error = ref(null)

const auth = useAuthStore()
const router = useRouter()

const submit = async () => {
  try {
    const res = await login(email.value, password.value)
    console.log("Login response:", res)
    console.log("Access token:", res.access_token)
    auth.login(res.access_token)
    router.push("/")
  } catch (err) {
    console.error("Login error:", err)
    error.value = "Invalid login"
  }
}

const logOut = async () => {
  auth.logout();
}
</script>

<template>
  
  <p v-if="auth.isLoggedIn" style="color: green; font-weight:bold"> LOGGED IN </p>
  <p v-else style="color:red,"> NOT LOGGED IN </p>
  
  <button @click="logOut"> LOG OUT </button>
  
  <h2>Login</h2>
  <input v-model="email" placeholder="email" />
  <input v-model="password" type="password" placeholder="password" />
  <button @click="submit">Login</button>
  <p v-if="error">{{ error }}</p>
</template>
