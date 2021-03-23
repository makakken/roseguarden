<template>
  <v-container fluid>
    <v-card>
      <v-card-title>
        <h3>Kontakt</h3>
      </v-card-title>
      <v-card-text dense>
        Für alle Support Fragen zu deinen persönlichen Karten, dem Schließsystem
        und allem, was damit zusammenhängt melde dich bitte bei 📩
        <a href="mailto:zugang@konglomerat.org">zugang@konglomerat.org</a>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import Vue from "vue";
import { codemirror } from "vue-codemirror";
import { mapState } from "vuex";
import moment from "moment";

// import { GenericNode } from '@/nodes/generic'

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
