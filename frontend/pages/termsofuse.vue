<template>
  <v-container fluid>
    <v-card height="600px">
      <v-card-title>
        <h3>Terms of use</h3>
      </v-card-title>
      <v-card-text dense>
        <h4>Last updated on 14.03.2021</h4>
        <br />
        <h4>AGREEMENT TO TERMS</h4>
        <p>
          These Terms and Conditions constitute a legally binding agreement made
          between you, whether personally or on behalf of an entity (“you”) and
          the Konglomerat e.V. Dresden (“we,” “us” or “our”), concerning your
          access to and use of the roseguarden.konglomerat.org website as well
          as any other media form, media channel, mobile website or mobile
          application related, linked, or otherwise connected thereto
          (collectively, the “Site”).
        </p>
        <p>
          You agree that by accessing the Site, you have read, understood, and
          agree to be bound by all of these Terms and Conditions. If you do not
          agree with all of these Terms and Conditions, then you are expressly
          prohibited from using the Site and you must discontinue use
          immediately.
        </p>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import Vue from "vue";
import { codemirror } from "vue-codemirror";
import { mapState } from "vuex";
import moment from "moment";

import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);

export default {
  layout: "dashboard",
  components: {},
  data: () => ({
    info: "",
  }),
  methods: {
    ok() {},
  },
  watch: {
    info: function (val) {},
  },
  computed: {
    test: function () {},
  },
  created() {},
  mounted() {},
};
</script>

<style scoped>
</style>
