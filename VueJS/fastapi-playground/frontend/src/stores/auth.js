// src/stores/auth.js
import { defineStore } from "pinia"
import { getMe } from "@/services/api"

export const useAuthStore = defineStore("auth", {
  // global reactive data 
  state: () => ({
    user: null,
    isLoggedIn: false
  }),

  actions: {
    async checkAuth() {
      try {
        this.user = await getMe();
        this.isLoggedIn = true;
      } catch {
        this.user = null;
        this.isLoggedIn = false;
      }
    },
    logout() {
      this.user = null;
      this.isLoggedIn = false;
    }
  }
})
