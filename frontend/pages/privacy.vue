<template>
  <v-container fluid>
    <v-card height="600px">
      <v-card-title >
        <h3>
          Privacy policy
        </h3>
      </v-card-title>
      <v-card-text dense>
        <h3>
          Data protection <br/>
        </h3>
        <br/>          
        <p>        
          As a rule the use of this website is possible without providing any personally relevant data. 
          Any provision of personal data (e.g. name, address or email addresses) occurs entirely on a voluntary basis. 
          These data will not be provided to any third parties without the user's express approval. Be aware that 
          the transmission of data via the internet (e.g. communication by email) is subject to security gaps. 
          Complete protection of data from unauthorized access by third parties is not possible. The use of contact 
          details published under the statutory requirement to provide acknowledgements by third parties for the purpose 
          of the transmission of unsolicited advertising and informational material is expressly opposed. The site 
          operator expressly reserves the right to take legal action against the unsolicited mailing of advertising 
          information by way of spamming or similar.
        </p>
        <h3>
          Use of cookies <br/>
        </h3>
        <br/>          
        <p>        
          This website uses cookies (<a href="https://www.cookiesandyou.com/">learn more about cookies</a>). <br/>
          Only necessary cookies needed to use this website will be used. <br>
          They are used for: <br>
          <ul>
            <li>authentification</li>
            <li>saving your personal settings</li>
          </ul>
          No marketing, tracking, advertising or functional cookies will be stored. We take big effort to develop 
          a service, that respect our users privacy. This include using only needed cookies and absolutly avoid 
          3rd party dependecies using cookies. Should anyone become aware of possible 3rd party cookies, please 
          contact us, and we will remove them.
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
