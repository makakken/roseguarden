<template>
  <v-container fluid>
    <v-card height="600px">
      <v-card-title >
        <h3>
          About
        </h3>
      </v-card-title>
      <v-card-text dense>
        This roseguarden instance is setuped for demonstration and test purpose of the roseguarden project. <br/> 
        This service is ment to be for testing a roseguarden instance before use. <br/>
        The provides service is for demonstration purpose only. <br/>
        No real rooms, buildings or rooms should be connected. <br/>
        Please install your own secure instance for in depth tests. <br/>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import { codemirror } from 'vue-codemirror';
  import { mapState } from 'vuex';
  import moment from 'moment';
  
  import axios from 'axios';
  import VueAxios from 'vue-axios';
  
  Vue.use(VueAxios, axios); 


  export default {
    layout: "dashboard",
    components: {
    },
    data: () => ({
      info: "",
    }),
    methods: {
      ok() {
      },
    },
    watch: {
      info: function (val) {
      },
    },
    computed: {
      test: function() {
      }             
    },
    created () {
    },
    mounted () {
    }

  }
</script>

<style scoped>

</style>
