const API = "http://127.0.0.1:8000"

export const login = async (email, password) => {
  const res = await fetch(`${API}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  })

  if (!res.ok) throw new Error("Login failed")

  return await res.json()
}
