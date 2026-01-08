<script setup>
import { ref, onMounted } from "vue"
import { useAuthStore } from "@/stores/auth"
import { useRouter } from "vue-router"
import { login, signup, logout } from "@/services/api"

const email = ref("")
const password = ref("")
const name = ref("")
const error = ref(null)
const isSignup = ref(false)

const auth = useAuthStore()
const router = useRouter()

const submit = async () => {
  try {
    if (isSignup.value) {
      await signup(name.value, email.value, password.value)
    } else {
      await login(email.value, password.value)
    }
    await auth.checkAuth()
    router.push("/")
  } catch (err) {
    console.error("Auth error:", err)
    error.value = isSignup.value ? "Signup failed" : "Invalid login"
  }
}

const toggleMode = () => {
  isSignup.value = !isSignup.value
  error.value = null
}

const logOut = async () => {
  try {
    await logout()
    auth.logout()
  } catch (err) {
    console.error("Logout error:", err)
  }
}

onMounted(async () => {
  try {
    await auth.checkAuth()
  } catch {
    // Not logged in, ignore
  }
})
</script>

<template>
  
  <p>hi</p>
  <p v-if="auth.isLoggedIn" style="color: green; font-weight:bold"> LOGGED IN </p>
  <p v-else style="color:red,"> NOT LOGGED IN </p>
  
  <button @click="logOut"> LOG OUT </button>
  
  <h2>{{ isSignup ? 'Signup' : 'Login' }}</h2>
  <input v-if="isSignup" v-model="name" placeholder="name" />
  <input v-model="email" placeholder="email" />
  <input v-model="password" type="password" placeholder="password" />
  <button @click="submit">{{ isSignup ? 'Signup' : 'Login' }}</button>
  <button @click="toggleMode">{{ isSignup ? 'Switch to Login' : 'Switch to Signup' }}</button>
  <p v-if="error">{{ error }}</p>

</template>
