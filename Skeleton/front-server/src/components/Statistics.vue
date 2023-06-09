<template>
  
  <v-tabs v-model="activeTab">
    <v-tab v-for="(tab, index) in tabs" :key="index" @click="changeTab(index)">
      {{ tab.label }}
     
    </v-tab>
    
    <v-tab-item v-for="(tab, index) in tabs" :key="index" v-show="activeTab === index">
  
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-row>
              
              <v-col cols="6"> 
                <h2>예금</h2>
                <canvas :ref="`depositchartCanvas${index}`" style="width: 50%; height:100%;"></canvas>
              </v-col>
              
              <v-col cols="6">
                <h2>적금</h2>
                <canvas :ref="`savingChartCanvas${index}`" style="width: 50%; height:50%;"></canvas>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import Chart from 'chart.js';

export default {
  name: 'Statistics',
  props: {
    savingProducts: {
      type: Array,
      required: true
    },
    depositProducts: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      activeTab: 0,
      tabs: [
        { label: '금리별' },
        { label: '기간별' },
        { label: '저축 금리 유형별' },
        { label: '은행별' }
      ],
      savingProducts: [],
      depositProducts: []
    };
  },
  created() {
    this.$nextTick(() => {
      this.drawCharts();
    });
  },
  methods: {
    drawCharts() {
      this.tabs.forEach((tab, index) => {
        const depositcanvasRef = `depositchartCanvas${index}`;
        const depositctx = this.$refs[depositcanvasRef][0].getContext('2d'); // Access native DOM element
          
        const savingCanvasRef = `savingChartCanvas${index}`;
        const savingCtx = this.$refs[savingCanvasRef][0].getContext('2d');
        // Generate chart data based on the tab
        let DepositchartData
        let SavingchartData
        switch (index) {
          case 0:
            DepositchartData = this.dgenerateInterestRateChartData();
            SavingchartData = this.sgenerateInterestRateChartData();
            break;
          case 1:
            DepositchartData = this.dgenerateDurationChartData();
            SavingchartData = this.sgenerateDurationChartData();
            break;
          case 2:
            DepositchartData = this.dgenerateSavingTypeChartData();
            SavingchartData = this.sgenerateSavingTypeChartData();
            break;
          case 3:
            DepositchartData = this.dgenerateBankChartData();
            SavingchartData = this.sgenerateBankChartData();
            break;
          default:
            DepositchartData = {};
            SavingchartData = {};
    }

      new Chart(depositctx, {
        type: 'bar',
        data: DepositchartData,
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
              stepSize: 0.5,
              max: 5
            },
            x: {
              offset: true,
              grid: {
                offset: true
              },
              ticks: {
                maxRotation: 0,
                minRotation: 0
              }
            }
          },
          plugins: {
            tooltip: {
              position: 'average',
              mode: 'index',
              intersect: false
            },
            legend: {
              display: true,
              position: 'top',
              align: 'center',
              labels: {
                boxWidth: 12,
                padding: 20
              }
            }
          }
        }
      });

      new Chart(savingCtx, {
        type: 'bar',
        data: SavingchartData,
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
              stepSize: 0.5,
              max: 5
            },
            x: {
              offset: true,
              grid: {
                offset: true
              },
              ticks: {
                maxRotation: 0,
                minRotation: 0
              }
            }
          },
          plugins: {
            tooltip: {
              position: 'average',
              mode: 'index',
              intersect: false
            },
            legend: {
              display: true,
              position: 'top',
              align: 'center',
              labels: {
                boxWidth: 12,
                padding: 20
              }
            }
          }
        }
      });
    });
  },
    dgenerateInterestRateChartData() {
      
      const depositLabels = this.depositProducts.map(product => product.fin_prdt_nm);
      const depositLabels2 = this.depositProducts.map(product => product.save_trm);
      const depositData = this.depositProducts.map(product => product.intr_rate);
      const labels = depositLabels.map((label, index) => `${label}(${depositLabels2[index]}개월)`);
      
      return {
        labels: labels,
        datasets: [
          {
            label: '금리(%)',
            data: depositData,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 3
          },
        ],
        }
    }, 
    sgenerateInterestRateChartData() {
      const savingLabels = this.savingProducts.map(product => product.fin_prdt_nm);
      const savingLabels2 = this.savingProducts.map(product => product.save_trm);
      const savingData = this.savingProducts.map(product => product.intr_rate);
      const labels = savingLabels.map((label, index) => `${label}(${savingLabels2[index]}개월)`);
      
      return {
        labels: labels,
        datasets: [
          {
            label: '금리(%)',
            data: savingData,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 3
          },
        ],
        }
    }, 
    dgenerateDurationChartData() {
      const depositLabels_s = this.depositProducts.map(product => product.fin_prdt_nm);
      const depositLabels_s2 = this.depositProducts.map(product => product.save_trm);
      const depositData_s = this.depositProducts.map(product => product.save_trm);
      const labels = depositLabels_s.map((label, index) => `${label}(${depositLabels_s2[index]}개월)`);
 
      return {
        labels: labels,
        datasets: [
          {
            label: '가입 기간(월)',
            data: depositData_s,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 3
          },
        ],
        }
    }, 
    sgenerateDurationChartData() {
      const savingLabels_s = this.savingProducts.map(product => product.fin_prdt_nm);
      const savingLabels_s2 = this.savingProducts.map(product => product.save_trm);
      const savingData = this.savingProducts.map(product => product.save_trm);
      const labels_s = savingLabels_s.map((label, index) => `${label}(${savingLabels_s2[index]}개월)`);
      
      return {
        labels: labels_s,
        datasets: [
          {
            label: '가입기간(월)',
            data: savingData,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 3
          },
        ],
        }
    }, 
    dgenerateSavingTypeChartData() {
        const depositData = this.depositProducts.map(product => product.intr_rate_type_nm);
        const countMap = {
          '단리': 0,
          '복리': 0
        };

        for (let i = 0; i < depositData.length; i++) {
          const rateType = depositData[i];
         
          if (rateType === '단리' || rateType === '복리') {
            countMap[rateType]++;
          }
        }

        const savingData = Object.values(countMap);
        const labels = Object.keys(countMap);

        return {
          labels: labels,
          datasets: [
            {
              label: '금리 유형',
              data: savingData,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 3
            },
          ],
        };
      },
      sgenerateSavingTypeChartData() {
      
        const savingData = this.savingProducts.map(product => product.intr_rate_type_nm);
        
        const countMap = {
          '단리': 0,
          '복리': 0
        };

        for (let i = 0; i < savingData.length; i++) {
          const rateType = savingData[i];
          if (rateType === '단리' || rateType === '복리') {
            countMap[rateType]++;
          }
        }

        const savingDataCount = Object.values(countMap);
        const labels = Object.keys(countMap)
        return {
          labels: labels,
          datasets: [
            {
              label: '금리 유형',
              data: savingDataCount,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 3
            },
          ],
        };
    },
    dgenerateBankChartData() {
      const depositLabels = this.depositProducts.map(product => product.kor_co_nm);
      const depositData = [];

      for (let i = 0; i < depositLabels.length; i++) {
        const label = depositLabels[i];
        const count = this.depositProducts.filter(product => product.kor_co_nm === label).length;
        depositData.push(count);
      }

      return {
        labels: depositLabels,
        datasets: [
          {
            label: '은행명',
            data: depositData,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 3
          },
        ],
      };
    },
    sgenerateBankChartData() {
    const savingLabels = this.savingProducts.map(product => product.kor_co_nm);
    const savingData = [];
    const bankCount = {};

    for (let i = 0; i < savingLabels.length; i++) {
      const label = savingLabels[i];
      if (bankCount[label]) {
        bankCount[label]++;
      } else {
        bankCount[label] = 1;
      }
    }

    for (const label in bankCount) {
      savingData.push(bankCount[label]);
    }

    return {
      labels: Object.keys(bankCount),
      datasets: [
        {
          label: '은행명',
          data: savingData,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 3
        },
      ],
    };
},
    changeTab(index) {
      const previousScrollPosition = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
  
  this.activeTab = index;
  this.$nextTick(() => {
    this.drawCharts();
    window.scrollTo(0, previousScrollPosition);
  });
}
  }
}
</script>