<script setup lang="ts">

const params = new URLSearchParams({
  "symbol": "SPY",
  "start_time": "2023-01-02T00:00:00Z",
  "end_time": "2023-01-05T00:00:00Z",
  "mode": "bars",
  "bar_size": "5m",
  "indicators": [
    {
      "name": "string",
      "params": {}
    }
  ],
  "limit": 100000
})

const ws = new WebSocket(
  `ws://localhost:8000/ws/market/data?${params}`
)

ws.onmessage = (e) => {
  const tick = JSON.parse(e.data)
  updateChart(tick)
}


  
</script>

<template>
  <h1>You did it!</h1>
  <p>
    Visit <a href="https://vuejs.org/" target="_blank" rel="noopener">vuejs.org</a> to read the
    documentation
  </p>
</template>

<style scoped></style>
