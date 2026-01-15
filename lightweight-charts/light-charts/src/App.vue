<script setup lang="ts">
import { onMounted } from 'vue';
import { createChart } from 'lightweight-charts';

onMounted(() => {
  // @ts-ignore
  // Sample data for all charts
  const lineData = [
    { time: '2024-01-01', value: 30 },
    { time: '2024-01-02', value: 35 },
    { time: '2024-01-03', value: 25 },
    { time: '2024-01-04', value: 40 },
    { time: '2024-01-05', value: 45 },
    { time: '2024-01-06', value: 50 },
    { time: '2024-01-07', value: 55 },
    { time: '2024-01-08', value: 60 },
  ];

  const areaData = [
    { time: '2024-01-01', value: 20 },
    { time: '2024-01-02', value: 32 },
    { time: '2024-01-03', value: 28 },
    { time: '2024-01-04', value: 38 },
    { time: '2024-01-05', value: 42 },
    { time: '2024-01-06', value: 48 },
    { time: '2024-01-07', value: 52 },
    { time: '2024-01-08', value: 58 },
  ];

  const barData = [
    { time: '2024-01-01', value: 25 },
    { time: '2024-01-02', value: 30 },
    { time: '2024-01-03', value: 20 },
    { time: '2024-01-04', value: 35 },
    { time: '2024-01-05', value: 40 },
    { time: '2024-01-06', value: 45 },
    { time: '2024-01-07', value: 50 },
    { time: '2024-01-08', value: 55 },
  ];

  const candlestickData = [
    { time: '2024-01-01', open: 25, high: 35, low: 22, close: 32 },
    { time: '2024-01-02', open: 32, high: 38, low: 30, close: 36 },
    { time: '2024-01-03', open: 36, high: 40, low: 28, close: 30 },
    { time: '2024-01-04', open: 30, high: 42, low: 28, close: 40 },
    { time: '2024-01-05', open: 40, high: 48, low: 38, close: 45 },
    { time: '2024-01-06', open: 45, high: 52, low: 43, close: 50 },
    { time: '2024-01-07', open: 50, high: 58, low: 48, close: 55 },
    { time: '2024-01-08', open: 55, high: 62, low: 52, close: 60 },
  ];

  // ============ CHART 1: LINE CHART ============
  const lineChartContainer = document.getElementById('lineChart');
  if (lineChartContainer) {
    const lineChart = createChart(lineChartContainer as HTMLElement, {
      width: 400,
      height: 300,
      layout: { background: { color: '#ffffff' } },
      timeScale: { timeVisible: true, secondsVisible: false },
    });

    const lineSeries = lineChart.addSeries({
      color: '#2962FF',
      lineWidth: 2,
    });

    lineSeries.setData(lineData);
    lineChart.timeScale().fitContent();
  }

  // ============ CHART 2: AREA CHART ============
  const areaChartContainer = document.getElementById('areaChart');
  if (areaChartContainer) {
    const areaChart = createChart(areaChartContainer as HTMLElement, {
      width: 400,
      height: 300,
      layout: { background: { color: '#ffffff' } },
      timeScale: { timeVisible: true, secondsVisible: false },
    });

    const areaSeries = areaChart.addAreaSeries({
      lineColor: '#4CAF50',
      topColor: '#4CAF5099',
      bottomColor: '#4CAF5011',
      lineWidth: 2,
    });

    areaSeries.setData(areaData);
    areaChart.timeScale().fitContent();
  }

  // ============ CHART 3: BAR CHART (HISTOGRAM) ============
  const barChartContainer = document.getElementById('barChart');
  if (barChartContainer) {
    const barChart = createChart(barChartContainer as HTMLElement, {
      width: 400,
      height: 300,
      layout: { background: { color: '#ffffff' } },
      timeScale: { timeVisible: true, secondsVisible: false },
    });

    const barSeries = barChart.addBarSeries({
      color: '#FF9800',
    });

    barSeries.setData(barData);
    barChart.timeScale().fitContent();
  }

  // ============ CHART 4: CANDLESTICK CHART ============
  const candleChartContainer = document.getElementById('candleChart');
  if (candleChartContainer) {
    const candleChart = createChart(candleChartContainer as HTMLElement, {
      width: 400,
      height: 300,
      layout: { background: { color: '#ffffff' } },
      timeScale: { timeVisible: true, secondsVisible: false },
    });

    const candleSeries = candleChart.addCandlestickSeries({
      upColor: '#26a69a',
      downColor: '#ef5350',
      borderVisible: true,
      wickUpColor: '#26a69a',
      wickDownColor: '#ef5350',
    });

    candleSeries.setData(candlestickData);
    candleChart.timeScale().fitContent();
  }

  // ============ CHART 5: MULTI-SERIES CHART ============
  const multiChartContainer = document.getElementById('multiChart');
  if (multiChartContainer) {
    const multiChart = createChart(multiChartContainer as HTMLElement, {
      width: 400,
      height: 300,
      layout: { background: { color: '#ffffff' } },
      timeScale: { timeVisible: true, secondsVisible: false },
    });

    // Add multiple series to one chart
    const lineSeries1 = multiChart.addLineSeries({
      color: '#2962FF',
      lineWidth: 2,
      title: 'Line 1',
    });

    const lineSeries2 = multiChart.addLineSeries({
      color: '#FF6B6B',
      lineWidth: 2,
      title: 'Line 2',
    });

    lineSeries1.setData(lineData);
    lineSeries2.setData(areaData);

    multiChart.timeScale().fitContent();
  }

  // ============ CHART 6: HISTOGRAM CHART ============
  const histogramChartContainer = document.getElementById('histogramChart');
  if (histogramChartContainer) {
    const histogramChart = createChart(histogramChartContainer as HTMLElement, {
      width: 400,
      height: 300,
      layout: { background: { color: '#ffffff' } },
      timeScale: { timeVisible: true, secondsVisible: false },
    });

    const histogramSeries = histogramChart.addHistogramSeries({
      color: '#9C27B0',
    });

    histogramSeries.setData(barData);
    histogramChart.timeScale().fitContent();
  }

  // ============ CHART 7: MIXED TYPES CHART ============
  const mixedChartContainer = document.getElementById('mixedChart');
  if (mixedChartContainer) {
    const mixedChart = createChart(mixedChartContainer as HTMLElement, {
      width: 400,
      height: 300,
      layout: { background: { color: '#ffffff' } },
      timeScale: { timeVisible: true, secondsVisible: false },
    });

    // Mix candlestick with area
    const mixedCandle = mixedChart.addCandlestickSeries({
      upColor: '#26a69a',
      downColor: '#ef5350',
      borderVisible: true,
    });

    const mixedArea = mixedChart.addAreaSeries({
      lineColor: '#00BCD4',
      topColor: '#00BCD499',
      bottomColor: '#00BCD411',
    });

    mixedCandle.setData(candlestickData);
    mixedArea.setData(areaData);

    mixedChart.timeScale().fitContent();
  }
});
</script>

<template>
  <div class="container">
    <h1>📊 Lightweight Charts - Complete Tutorial</h1>
    <p class="subtitle">All possible chart types demonstrated below</p>

    <!-- CHART 1: LINE CHART -->
    <div class="chart-section">
      <h2>1. Line Chart</h2>
      <p class="description">Perfect for tracking trends over time. Shows price movements with connected points.</p>
      <div id="lineChart" class="chart-container"></div>
    </div>

    <!-- CHART 2: AREA CHART -->
    <div class="chart-section">
      <h2>2. Area Chart</h2>
      <p class="description">Similar to line chart but with filled area below the line, emphasizing magnitude.</p>
      <div id="areaChart" class="chart-container"></div>
    </div>

    <!-- CHART 3: BAR CHART -->
    <div class="chart-section">
      <h2>3. Bar Chart (Column Chart)</h2>
      <p class="description">Uses vertical bars to represent values. Great for comparing discrete values.</p>
      <div id="barChart" class="chart-container"></div>
    </div>

    <!-- CHART 4: CANDLESTICK CHART -->
    <div class="chart-section">
      <h2>4. Candlestick Chart</h2>
      <p class="description">Displays open, high, low, close (OHLC) data. Standard for financial/stock analysis.</p>
      <div id="candleChart" class="chart-container"></div>
    </div>

    <!-- CHART 5: MULTI-SERIES CHART -->
    <div class="chart-section">
      <h2>5. Multi-Series Chart (Multiple Lines)</h2>
      <p class="description">Combine multiple line series on one chart to compare different datasets.</p>
      <div id="multiChart" class="chart-container"></div>
    </div>

    <!-- CHART 6: HISTOGRAM CHART -->
    <div class="chart-section">
      <h2>6. Histogram Chart</h2>
      <p class="description">Similar to bars but typically for distributing continuous data (volume, counts).</p>
      <div id="histogramChart" class="chart-container"></div>
    </div>

    <!-- CHART 7: MIXED CHART -->
    <div class="chart-section">
      <h2>7. Mixed Chart (Candlestick + Area)</h2>
      <p class="description">Combine different series types on a single chart for complex analysis.</p>
      <div id="mixedChart" class="chart-container"></div>
    </div>
  </div>
</template>

<style scoped>
.container {
  padding: 30px;
  max-width: 1000px;
  margin: 0 auto;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

h1 {
  text-align: center;
  color: #ffffff;
  font-size: 2.5rem;
  margin-bottom: 10px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.subtitle {
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
  font-size: 1.1rem;
  margin-bottom: 40px;
}

.chart-section {
  background: white;
  border-radius: 12px;
  padding: 25px;
  margin-bottom: 30px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.chart-section:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
}

.chart-section h2 {
  color: #667eea;
  font-size: 1.5rem;
  margin-bottom: 8px;
  border-left: 4px solid #667eea;
  padding-left: 12px;
}

.description {
  color: #666;
  font-size: 0.95rem;
  margin-bottom: 15px;
  font-style: italic;
}

.chart-container {
  display: flex;
  justify-content: center;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 10px;
  border: 1px solid #e0e0e0;
}
</style>
