<template>
  <v-container>
    <v-row>
      <v-col cols="12" lg="12" sm="12" xs="12" align="center">
        <h1>Welcome to the roseguarden test server</h1>
        <br />
        <v-alert type="info">
          Please feel encouraged to test the features and the worklow of
          roseguarden on this server. <br />
          If you find bugs or have feature requests, please start with an issue
          <a
            href="https://gitlab.com/roseguarden/roseguarden/-/issues"
            style="color: white"
            target="_blank"
          >
            here.
          </a>
        </v-alert>
      </v-col>
    </v-row>
    <v-row v-if="loading" align="center" justify="center">
      <v-progress-circular
        :size="70"
        :width="7"
        color="primary"
        indeterminate
      ></v-progress-circular>
    </v-row>
    <v-row v-else-if="valid && !loading">
      <v-col cols="3" lg="4" sm="4" />
      <v-col cols="6" lg="4" sm="4" align="center">
        <!--
        <div class="text-xs-center">Welcome {{ firstname }} {{ lastname }}</div>
        -->
        <div class="text-xs-center">
          <v-btn dark color="primary" @click="onTestLogout()">Logout</v-btn>
        </div>
      </v-col>
      <v-col cols="3" lg="4" sm="4" />
    </v-row>
    <v-row v-else>
      <v-col cols="12" lg="12" sm="12" xs="12" align="center">
        <h2>Please login to start testing</h2>
      </v-col>
      <v-col cols="12" lg="4" sm="4" xs="12" align="center">
        <div class="text-xs-center">
          <v-btn
            color="success"
            @click="onTestLogin('roseguarden@fabba.space', 'test1234')"
            >Test as a normal user (login)</v-btn
          >
        </div>
      </v-col>
      <v-col cols="12" lg="4" sm="4" xs="12" align="center">
        <div class="text-xs-center">
          <v-btn
            dark
            color="success"
            @click="onTestLogin('super@fabba.space', 'test1234')"
            >Test as a supervisor user (login)</v-btn
          >
        </div>
      </v-col>
      <v-col cols="12" lg="4" sm="4" xs="12" align="center">
        <div class="text-xs-center">
          <v-btn
            dark
            color="success"
            @click="onTestLogin('admin@fabba.space', 'admin1234')"
            >Test as an admin user (login)</v-btn
          >
        </div>
      </v-col>
      <v-col cols="12" lg="12" sm="12" xs="12" align="center">
        (The pin for all default users is '123456' but can be changed at any
        time)
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" lg="12" sm="12" xs="12" align="center">
        <v-alert type="error">
          This is a public server. Please be aware that all data is visible to
          anybody.
          <br />
          It's meant to be only for test purposes. The data can be reset at any
          time.
        </v-alert>
      </v-col>
    </v-row>
    <br />
  </v-container>
</template>

<script>
import Vue from "vue";
import EChart from "@/components/chart/echartwrap";
import VWidget from "@/components/VWidget";
import Material from "vuetify/es5/util/colors";
import BoxChart from "@/components/widgets/chart/BoxChart";
import { codemirror } from "vue-codemirror";
import { mapState } from "vuex";

import * as actionBuilder from "@/api/actionBuilder";

// require styles
import "codemirror/lib/codemirror.css";
import "codemirror/theme/mbo.css";

import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);

export default {
  layout: "dashboard",
  components: {
    VWidget,
    EChart,
    BoxChart,
    codemirror,
  },
  data: () => ({
    route: "abc",
    newuser: "testuser@fabba.space",
    color: Material,
    selectedTab: "tab-1",
    log: "Loading log ...",
    cmOptions: {
      // codemirror options
      tabSize: 4,
      mode: "text/javascript",
      theme: "mbo",
      readOnly: true,
      lineNumbers: true,
      line: true,
    },
  }),
  methods: {
    onRoute() {
      this.$router.push(this.route);
    },
    onToggleRoute() {
      this.$store.commit("app/togglePage");
    },
    onScroll(e) {},
    onNotification() {
      console.log(this.jwttoken);
      this.$store.dispatch("notifications/pushSuccess", "Test");
    },
    onTestLogin(user, password) {
      let loginAction = [];
      loginAction = [actionBuilder.newLoginUserAction(user, password)];
      this.$store.dispatch("actions/emitActionRequest", loginAction);
      this.$store.dispatch("user/login", null);
    },
    onTestRegistration() {
      let model = {
        email: this.newuser,
        firstname: "Auto",
        lastname: "Generated",
        organization: "Test",
        password: "12345678",
        password_verification: "12345678",
      };
      let registerAction = [
        actionBuilder.newRegisterUserAction(model, { route: false }),
      ];
      this.$store.dispatch("actions/emitActionRequest", registerAction);
    },
    onTestLogout() {
      this.$store.dispatch("user/resetToken");
      this.$store.dispatch("user/logout");
    },
  },
  computed: {
    ...mapState("user", [
      "jwttoken",
      "valid",
      "firstname",
      "lastname",
      "loading",
    ]),
  },
  created() {},
  mounted() {},
};
</script>

<style scoped>
.zindex-repair {
  z-index: 1;
}

.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  font-family: monospace;
  height: 600px;
}
</style>
