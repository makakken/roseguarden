<template>
  <v-container>
    <v-row dense>
      <v-col cols="12" lg="12" sm="12" xs="12" align="center">
        <h1>Willkommen im Rosengarten des Konglomerat!</h1>
        <br />
        <v-alert type="info">
          Wenn du Bugs findest, poste sie bitte als Issue
          <a
            href="https://github.com/konglomerat/roseguarden/issues"
            style="color: white"
            target="_blank"
          >
            hier.
          </a>
          <br />
          Wenn dir das nichts ist, wende dich bitte mit allen Support-Anfragen
          an
          <a href="mailto:zugang@konglomerat.org">zugang@konglomerat.org</a> .
          <br />Unten gibt es eine FAQ Sektion, da lohnt es sich mal
          reinzuschauen.
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
      <v-col
        cols="12"
        lg="8"
        offset-lg="2"
        sm="8"
        offset-sm="2"
        xs="12"
        justify="center"
        align="center"
        dense
      >
        <div class="align-center">
          <!---
                  <img src="../static/konglo_logo.png" alt="Roseguarden logo" width="120" height="120">
                  ---->
          <h2 class="">Anmelden</h2>
        </div>
        <v-form v-model="valid_credentials">
          <v-text-field
            append-icon="person"
            name="login"
            label="Email"
            type="email"
            v-model="model.username"
            :rules="[rules.email, rules.required]"
          ></v-text-field>
          <v-text-field
            append-icon="lock"
            name="password"
            label="Passwort"
            id="password"
            type="password"
            v-model="model.password"
            :rules="[rules.required]"
          ></v-text-field>
        </v-form>
      </v-col>
      <v-col cols="9" lg="5" offset-lg="2" sm="5" offset-sm="2" xs="9">
        <v-btn
          dense
          text
          small
          color="primary"
          href="/user/lostpassword"
          target="_blank"
          >Passwort vergessen?</v-btn
        >
        <v-btn
          dense
          text
          small
          color="primary"
          href="/user/resendverificationmail"
          target="_blank"
          >Verifizierung nochmal senden?</v-btn
        >
      </v-col>
      <v-col
        cols="3"
        offset="0"
        lg="3"
        offset-lg="0"
        sm="3"
        offset-sm="0"
        xs="3"
        class="d-flex justify-end"
      >
        <v-btn
          color="primary"
          width="100%"
          @click="login"
          :disabled="!valid_credentials"
          >Anmelden</v-btn
        >
      </v-col>

      <v-col cols="1" />
      <v-col cols="12">
        <div class="text-center">
          <h2 class="flex my-4">Noch keinen Account?</h2>
          <p>
            Um das neue System zu nutzen, musst du dich zuerst registrieren.
            <br />Mit deinem Account kannst du dann deine Karte freischalten,
            den aktuellen Status anschauen und Änderungen vornehmen.
          </p>
          <v-btn dark color="primary" to="/user/register">Registrieren</v-btn>
        </div>
      </v-col>
      <v-col cols="1" />
      <v-col cols="12" lg="12" sm="12" xs="12" align="center">
        <v-alert type="error">
          Wenn du dich hier nicht registrierst, wird deine alten Karte ab
          xx.xx.xxxx nicht mehr funktionieren!
        </v-alert>
      </v-col>
    </v-row>
    <br />
  </v-container>
</template>

<script>
import Vue from "vue";
//import EChart from "@/components/chart/echartwrap";
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
    BoxChart,
    codemirror,
  },
  data: () => ({
    route: "abc",
    newuser: "testuser@fabba.space",
    color: Material,
    selectedTab: "tab-1",
    log: "Loading log ...",
    valid_credentials: false,
    rules: {
      required: (value) => !!value || "Notwendig.",
      email: (v) =>
        !v ||
        /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,5})+$/.test(v) ||
        "E-mail must be valid",
    },
    model: {
      username: "",
      password: "",
    },
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
    login() {
      let loginAction = [
        actionBuilder.newLoginUserAction(
          this.model.username,
          this.model.password
        ),
      ];
      this.$store.dispatch("actions/emitActionRequest", loginAction);
      this.$store.dispatch("user/login", null);
    },
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
