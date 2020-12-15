<template>
  <v-container fluid>
    <v-card >
      <v-card-title >
        <h3>
          Contact
        </h3>
      </v-card-title>
      <v-card-text dense>
        <h3>
          Provider of the service
        </h3>
        <br/>          
        <p>
          The administration and operation of this roseguarden system is managed by:  <br/>
          <img src="../static/person_name.png" height="20px"> <br/>
          You can get in contact by: <br/> 
          <img src="../static/contact.png" height="40px"> <br/>  <br/>
          The provides service is for demonstration purpose only. <br/>
          Be aware that all data could be reset at any time. <br/>
          Don't store personal data here. It is visible to everyone. <br/>
        </p>
        <br>
        <h3>
          I don't get access to buildings, rooms, systems or devices?<br/>
        </h3>
        <br/>          
        <p>
          The provided service is for demonstration purpose only. <br/>
          No real rooms, buildings or rooms should be connected. <br/>
          Please install your own secure instance for in depth tests. <br/>
        </p>
        <br>        
        <h3>
          Questions concerning the roseguarden system
        </h3>
        <br/>          
        <p>
          Please visit the roseguarden homepage here: <a href="https://roseguarden.fabba.space">https://roseguarden.fabba.space</a>
        </p>
        <h3>
          Want to report bugs of the roseguarden system
        </h3>
        <br/>          
        <p>
          Bug reports are very welcome. Please feel free to make your report here: <a href="https://gitlab.com/roseguarden/roseguarden/-/issues"> https://gitlab.com/roseguarden/roseguarden/-/issues </a>
        </p>
        
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import { codemirror } from 'vue-codemirror';
  import { mapState } from 'vuex';
  import moment from 'moment';
  
  // import { GenericNode } from '@/nodes/generic'

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
