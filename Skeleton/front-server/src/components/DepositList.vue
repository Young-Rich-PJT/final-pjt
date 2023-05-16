<template>
  <v-flex class="dataList" column align-center>
    <v-card max-width='600' tile>
      <v-list-item v-for="(data, index) in propsdata.slice(0, 15)" :key='index'>
        <v-list-item-content>
            <v-list-item-title>은행명: {{data.kor_co_nm}}</v-list-item-title>
            <v-list-item-subtitle>상품이름: {{data.fin_prdt_nm}}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  name: 'DepositList',
  props: ["propsdata"],
}
</script>

<style>
.dataList {
  text-align: start;
  margin-top: 100px;
}
</style>