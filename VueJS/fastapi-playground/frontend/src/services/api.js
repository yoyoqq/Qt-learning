import axios from "axios";


const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getItems = () => api.get("/items");
export const addItem = (item) => api.post("/items", item);
export const updateItem = (id, item) => api.put(`/items/${id}`, item);  // URL, HTTP method, BODY 
export const deleteItem = (id) => api.delete(`/items/${id}`)
// export const updateItem = (id, item) => api.put(`/items/${id}`, item)

// security 
export const login = async (email, password) => {
  const res = await api.post("/auth/login", {
    email, password
  })
  return res.data
}


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