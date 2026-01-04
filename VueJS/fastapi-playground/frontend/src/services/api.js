export const fetchItems = async () => {
  const response = await fetch("http://127.0.0.1:8000/items/")
  if (!response.ok) {
    throw new Error("Failed to fetch items")
  }
  return await response.json()
}

// create a new item
export const createItem = async (item) => {
    const response = await fetch("http://127.0.0.1:8000/items/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(item)
    })
    if (!response.ok) throw new Error("FAILED")
    return await response.json()
}

// delete the item 
export const deleteItem = async (id) => {
    const response = await fetch(`http://127.0.0.1:8000/items/${id}`, {
        method: "DELETE"
    })
    if (!response.ok) throw new Error("FAILED delete item")
    return true
}