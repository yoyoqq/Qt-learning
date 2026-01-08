// src/stores/auth.js
import { defineStore } from "pinia"

export const useAuthStore = defineStore("auth", {
  // global reactive data 
  state: () => ({
    token: localStorage.getItem("token") || null
  }),

  getters: {
    isLoggedIn: (state) => !!state.token
  },

  actions: {
    login(token) {
      this.token = token
      localStorage.setItem("token", token)
    },
    logout() {
      this.token = null
      localStorage.removeItem("token")
    }
  }
})
