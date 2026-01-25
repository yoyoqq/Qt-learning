<template>
  <div ref="lineChartContainer"></div>
  <div ref="candleChartContainer"></div>
</template>

<script lang="ts" setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { createChart, LineSeries, CandlestickSeries, HistogramSeries } from 'lightweight-charts'
import type { IChartApi } from 'lightweight-charts'

// =============================================================
// CONFIGURATIONS AND HELPERS
// =============================================================

// apply crosshair customization globally
function apply_crosshair(chart: IChartApi) {
    chart.applyOptions({
    crosshair: {
        mode: 1, // normal
        vertLine: {
        color: '#2962FF',
        width: 2,
        style: 2, // dashed
        labelBackgroundColor: '#2962FF',
        },
        horzLine: {
        color: '#2962FF',
        width: 2,
        style: 2, // dashed
        labelBackgroundColor: '#2962FF',
        },
    },
    })
}

// create SMA 
function calculateSMA(data: Candle[], period: number) {
  return data.map((candle, index) => {
    if (index < period - 1) return null

    const slice = data.slice(index - period + 1, index + 1)
    const avg =
      slice.reduce((sum, c) => sum + c.close, 0) / period

    return {
      time: candle.time,
      value: Number(avg.toFixed(2)),
    }
  }).filter(Boolean)
}




// =============================================================
// CANDLESTICKS DIFF CHARTS 
// =============================================================

// Create candlestick chart data 
const candleChartContainer = ref<HTMLDivElement | null>(null)
let candleChart : IChartApi | null = null

type Candle = {
  time: string
  open: number
  high: number
  low: number
  close: number
}

function generateNextCandle(lastCandle: Candle): Candle {
  const lastClose = lastCandle.close
  const randomChange = (Math.random() - 0.5) * 10 // random change between -5 and +5
  const open = lastClose
  const close = Math.max(lastClose + randomChange, 100) // ensure price stays positive
  const high = Math.max(open, close) + Math.random() * 3
  const low = Math.min(open, close) - Math.random() * 3

  // generate next timestamp (next business day)
  const lastDate = new Date(lastCandle.time)
  const nextDate = new Date(lastDate)
  nextDate.setDate(nextDate.getDate() + 1)
  
  const timeStr = nextDate.toISOString().split('T')[0]

  return {
    time: timeStr,
    open: Number(open.toFixed(2)),
    high: Number(high.toFixed(2)),
    low: Number(low.toFixed(2)),
    close: Number(close.toFixed(2)),
  }
}

function createCandleData(): Candle[] {
return [
  { time: '2024-01-16', open: 141, high: 145, low: 139, close: 143 },
  { time: '2024-01-17', open: 143, high: 146, low: 140, close: 142 },
  { time: '2024-01-18', open: 142, high: 148, low: 141, close: 147 },
  { time: '2024-01-19', open: 147, high: 150, low: 144, close: 148 },
  { time: '2024-01-20', open: 148, high: 152, low: 146, close: 151 },

  { time: '2024-01-21', open: 151, high: 154, low: 148, close: 149 },
  { time: '2024-01-22', open: 149, high: 153, low: 147, close: 152 },
  { time: '2024-01-23', open: 152, high: 156, low: 150, close: 155 },
  { time: '2024-01-24', open: 155, high: 158, low: 153, close: 156 },
  { time: '2024-01-25', open: 156, high: 160, low: 154, close: 159 },

  { time: '2024-01-26', open: 159, high: 162, low: 157, close: 160 },
  { time: '2024-01-27', open: 160, high: 163, low: 158, close: 161 },
  { time: '2024-01-28', open: 161, high: 165, low: 159, close: 164 },
  { time: '2024-01-29', open: 164, high: 168, low: 162, close: 166 },
  { time: '2024-01-30', open: 166, high: 170, low: 164, close: 169 },

  { time: '2024-01-31', open: 169, high: 172, low: 166, close: 168 },
  { time: '2024-02-01', open: 168, high: 171, low: 165, close: 170 },
  { time: '2024-02-02', open: 170, high: 174, low: 168, close: 173 },
  { time: '2024-02-03', open: 173, high: 176, low: 171, close: 175 },
  { time: '2024-02-04', open: 175, high: 178, low: 173, close: 176 },

  { time: '2024-02-05', open: 176, high: 179, low: 174, close: 177 },
  { time: '2024-02-06', open: 177, high: 181, low: 175, close: 180 },
  { time: '2024-02-07', open: 180, high: 184, low: 178, close: 183 },
  { time: '2024-02-08', open: 183, high: 186, low: 181, close: 184 },
  { time: '2024-02-09', open: 184, high: 188, low: 182, close: 187 },

  { time: '2024-02-10', open: 187, high: 190, low: 185, close: 189 },
  { time: '2024-02-11', open: 189, high: 193, low: 187, close: 192 },
  { time: '2024-02-12', open: 192, high: 195, low: 190, close: 194 },
  { time: '2024-02-13', open: 194, high: 198, low: 192, close: 197 },
  { time: '2024-02-14', open: 197, high: 200, low: 195, close: 199 },
];
}

function createCandleChart(container: HTMLDivElement) {
    const chart = createChart(container, {
        width: 600,
        height: 300,
        layout: {
            background: { color: '#ffffff' },
            textColor: '#333',
        },
        grid: {
            vertLines: { color: '#eee' },
            horzLines: { color: '#eee' },
        },
    })

    const candleSeries = chart.addSeries(CandlestickSeries, {
        upColor: '#26a69a',
        downColor: '#ef5350',
        borderDownColor: '#ef5350',
        borderUpColor: '#26a69a',
        wickDownColor: '#ef5350',
        wickUpColor: '#26a69a',
    })

    // create horizontal price line
    const priceLine = candleSeries.createPriceLine({
        price: 200,
        color: 'red',
        lineWidth: 2,
        lineStyle: 2,
        axisLabelVisible: true,
        title: 'Resistance',
    })
    // set candle data 
    candleSeries.setData(createCandleData())

    // add SMA data 
    const smaSeries = chart.addSeries(LineSeries, {
    color: 'orange',
    lineWidth: 1,
    })
    smaSeries.setData(calculateSMA(createCandleData(), 20) as { time: string; value: number }[])

    chart.timeScale().fitContent()  // Controls the zoom panning and initial view 

    // apply_crosshair(chart)

    // apply_histogram(chart)

    // real time updates 
    let candles = createCandleData()
    candleSeries.setData(candles)

    setInterval(() => {
        const next = generateNextCandle(candles[candles.length - 1])
        candles.push(next)
        candleSeries.update(next)
        }, 10)

    return chart
}


// Create line chart data 
const lineChartContainer = ref<HTMLDivElement | null>(null)
let lineChart: IChartApi | null = null
function createLineChart(container: HTMLDivElement) {
  const chart = createChart(container, {
    width: 600,
    height: 300,
    layout: {
      background: { color: '#ffffff' },
      textColor: '#333',
    },
    grid: {
      vertLines: { color: '#eee' },
      horzLines: { color: '#eee' },
    },
  })

  const lineSeries = chart.addSeries(LineSeries, {
    color: '#2962FF',
    lineWidth: 2,
  })

  lineSeries.setData(lineData) 

  apply_crosshair(chart)

  return chart
}

const lineData = [
  { time: '2024-01-01', value: 100 },
  { time: '2024-01-02', value: 102 },
  { time: '2024-01-03', value: 101 },
  { time: '2024-01-04', value: 105 },
  { time: '2024-01-05', value: 108 },
  { time: '2024-01-08', value: 112 },
  { time: '2024-01-09', value: 110 },
  { time: '2024-01-10', value: 115 },
  { time: '2024-01-11', value: 118 },
  { time: '2024-01-12', value: 120 },
  { time: '2024-01-15', value: 125 },
  { time: '2024-01-16', value: 123 },
  { time: '2024-01-17', value: 128 },
  { time: '2024-01-18', value: 130 },
  { time: '2024-01-19', value: 135 },
  { time: '2024-01-22', value: 138 },
  { time: '2024-01-23', value: 140 },
  { time: '2024-01-24', value: 142 },
  { time: '2024-01-25', value: 145 },
]


onMounted(() => {
  if (!lineChartContainer.value) return
  lineChart = createLineChart(lineChartContainer.value)

  if (!candleChartContainer.value) return
  candleChart = createCandleChart(candleChartContainer.value)
})

onBeforeUnmount(() => {
    if (lineChart) {
    lineChart.remove()
    }

    if (candleChart) {
        candleChart.remove()
    }
})
</script>