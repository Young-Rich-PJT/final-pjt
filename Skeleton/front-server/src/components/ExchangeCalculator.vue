<template>
  <div id="calc">
    <br><br>
    <h1 class="ercword center">환율계산기</h1>
    <br>
    <p class="center">외화 환전금액을 계산하여 드립니다.</p>
    <div class="container-calc">
      <div class="container-one">
        <select name="first-currency" id="first-currency" v-model="currency_one">
          <!-- 기타 옵션들 -->
          <option value="AED">AED</option>
          <option value="ARS">ARS</option>
          <option value="AUD">AUD</option>
          <option value="BGN">BGN</option>
          <option value="BRL">BRL</option>
          <option value="BSD">BSD</option>
          <option value="CAD">CAD</option>
          <option value="CHF">CHF</option>
          <option value="CLP">CLP</option>
          <option value="CNY">CNY</option>
          <option value="COP">COP</option>
          <option value="CZK">CZK</option>
          <option value="DKK">DKK</option>
          <option value="DOP">DOP</option>
          <option value="EGP">EGP</option>
          <option value="EUR">EUR</option>
          <option value="FJD">FJD</option>
          <option value="GBP">GBP</option>
          <option value="GTQ">GTQ</option>
          <option value="HKD">HKD</option>
          <option value="HRK">HRK</option>
          <option value="HUF">HUF</option>
          <option value="IDR">IDR</option>
          <option value="ILS">ILS</option>
          <option value="INR">INR</option>
          <option value="ISK">ISK</option>
          <option value="JPY">JPY</option>
          <option value="KRW">KRW</option>
          <option value="KZT">KZT</option>
          <option value="MXN">MXN</option>
          <option value="MYR">MYR</option>
          <option value="NOK">NOK</option>
          <option value="NZD">NZD</option>
          <option value="PAB">PAB</option>
          <option value="PEN">PEN</option>
          <option value="PHP">PHP</option>
          <option value="PKR">PKR</option>
          <option value="PLN">PLN</option>
          <option value="PYG">PYG</option>
          <option value="RON">RON</option>
          <option value="RUB">RUB</option>
          <option value="SAR">SAR</option>
          <option value="SEK">SEK</option>
          <option value="SGD">SGD</option>
          <option value="THB">THB</option>
          <option value="TRY">TRY</option>
          <option value="TWD">TWD</option>
          <option value="UAH">UAH</option>
          <option value="USD">USD</option>
          <option value="UYU">UYU</option>
          <option value="VND">VND</option>
          <option value="ZAR">ZAR</option>
        </select>
        <input type="number" name="input-one" id="input" v-model="amountOne" @input="fetchData()" />
      </div>
      <div class="container-two">
        <button class="swap" @click="swapValues()">swap</button>
        <h4 id="baseValue">1 {{ currency_one }} = {{ rate }} {{ currency_two }}</h4>
      </div>
      <div class="container-three">
        <select name="second-currency" id="second-currency" v-model="currency_two">
          <!-- 기타 옵션들 -->
          <option value="AED">AED</option>
          <option value="ARS">ARS</option>
          <option value="AUD">AUD</option>
          <option value="BGN">BGN</option>
          <option value="BRL">BRL</option>
          <option value="BSD">BSD</option>
          <option value="CAD">CAD</option>
          <option value="CHF">CHF</option>
          <option value="CLP">CLP</option>
          <option value="CNY">CNY</option>
          <option value="COP">COP</option>
          <option value="CZK">CZK</option>
          <option value="DKK">DKK</option>
          <option value="DOP">DOP</option>
          <option value="EGP">EGP</option>
          <option value="EUR">EUR</option>
          <option value="FJD">FJD</option>
          <option value="GBP">GBP</option>
          <option value="GTQ">GTQ</option>
          <option value="HKD">HKD</option>
          <option value="HRK">HRK</option>
          <option value="HUF">HUF</option>
          <option value="IDR">IDR</option>
          <option value="ILS">ILS</option>
          <option value="INR">INR</option>
          <option value="ISK">ISK</option>
          <option value="JPY">JPY</option>
          <option value="KRW">KRW</option>
          <option value="KZT">KZT</option>
          <option value="MXN">MXN</option>
          <option value="MYR">MYR</option>
          <option value="NOK">NOK</option>
          <option value="NZD">NZD</option>
          <option value="PAB">PAB</option>
          <option value="PEN">PEN</option>
          <option value="PHP">PHP</option>
          <option value="PKR">PKR</option>
          <option value="PLN">PLN</option>
          <option value="PYG">PYG</option>
          <option value="RON">RON</option>
          <option value="RUB">RUB</option>
          <option value="SAR">SAR</option>
          <option value="SEK">SEK</option>
          <option value="SGD">SGD</option>
          <option value="THB">THB</option>
          <option value="TRY">TRY</option>
          <option value="TWD">TWD</option>
          <option value="UAH">UAH</option>
          <option value="USD">USD</option>
          <option value="UYU">UYU</option>
          <option value="VND">VND</option>
          <option value="ZAR">ZAR</option>
        </select>
        <div id="result">
          <h2>
            <input type="number" id="amount-two" placeholder="0" disabled v-model="amountTwo" />
          </h2>
        </div>
      </div>
      <div class="container-four">
        <h6 id="lastlyUpdated">최근 업데이트: {{ data.time_last_update_utc }}</h6>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      data: [],
      currency_one: 'USD',
      currency_two: 'KRW',
      rate: '',
      amountOne: 1,
      amountTwo: 0,
    }
  },
  methods: {
    fetchData() {
      fetch(`https://v6.exchangerate-api.com/v6/a1030034a3f8837e9ab84b03/latest/${this.currency_one}`)
      .then(res => res.json())
      .then(data => {
        this.data = data
        this.rate = data.conversion_rates[this.currency_two]
        this.amountTwo = this.amountOne * this.rate
      })
    },
    swapValues() {
      const temp = this.currency_one
      this.currency_one = this.currency_two
      this.currency_two = temp
      this.fetchData()
    }
  },
  mounted() {
    this.fetchData()
  },
}
</script>

<style scoped>
#calc {
  display: flex;
  flex-direction: column;
  align-items: center;
  align-content: center;
  width: 100%;
  height: 100%;
}

.ercword {
  color: #0dcaf0;
}

.center {
  text-align: center;
}

.container-calc {
  width: 70%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-content: center;
  align-items: center;
  text-align: center;
}

.container-two {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

.swap {
  background-color: #0dcaf0;
  color: #fff;
  padding: 5px 12px;
  border-radius: 10px;
  border: none;
  cursor: pointer;
}

.swap:hover {
  background-color: #0dcaf0;
}

#result {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px; /* 필요에 따라 높이 조정 */
}

select,
#input {
  padding: 5px;
  margin: 5px;
  border: 1px solid rgba(0, 0, 0, 0.5);
  outline: none;
  font-size: 16px;
  width: 100%;
  max-width: 200px;
}

#lastlyUpdated {
  font-weight: 500;
  margin-top: 10px;
}

#baseValue {
  font-weight: 500;
  margin-top: 10px;
}
</style>