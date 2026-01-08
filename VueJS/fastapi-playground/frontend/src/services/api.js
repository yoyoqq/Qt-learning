import axios from "axios";


const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  withCredentials: true,  // Include cookies
});

export const getItems = () => api.get("/items");
export const addItem = (item) => api.post("/items", item);
export const updateItem = (id, item) => api.put(`/items/${id}`, item);
export const deleteItem = (id) => api.delete(`/items/${id}`)

// Auth functions using fetch for cookie handling
const API_BASE = "http://127.0.0.1:8000/authenticateJWT";

export const login = async (email, password) => {
  const response = await fetch(`${API_BASE}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ email, password })
  });
  if (!response.ok) throw new Error("Login failed");
  return response.json();
};

export const signup = async (name, email, password) => {
  const response = await fetch(`${API_BASE}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ name, email, password })
  });
  if (!response.ok) throw new Error("Signup failed");
  return response.json();
};

export const logout = async () => {
  const response = await fetch(`${API_BASE}/logout`, {
    method: "POST",
    credentials: "include"
  });
  if (!response.ok) throw new Error("Logout failed");
  return response.json();
};

export const getMe = async () => {
  const response = await fetch(`${API_BASE}/me`, {
    credentials: "include"
  });
  if (!response.ok) throw new Error("Not authenticated");
  return response.json();
};



// export const fetchItems = async () => {
//   const response = await fetch("http://127.0.0.1:8000/items/")
//   if (!response.ok) {
//     throw new Error("Failed to fetch items")
//   }
//   return await response.json()
// }

// // create a new item
// export const createItem = async (item) => {
//     const response = await fetch("http://127.0.0.1:8000/items/", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(item)
//     })
//     if (!response.ok) throw new Error("FAILED")
//     return await response.json()
// }

// // delete the item 
// export const deleteItem = async (id) => {
//     const response = await fetch(`http://127.0.0.1:8000/items/${id}`, {
//         method: "DELETE"
//     })
//     if (!response.ok) throw new Error("FAILED delete item")
//     return true
// }