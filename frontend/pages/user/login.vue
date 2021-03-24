<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md5 lg5>
            <v-card width="100%" class="pa-3">
              <v-card-text>
                <div class="layout column align-center">
                  <!---
                  <img src="../static/konglo_logo.png" alt="Roseguarden logo" width="120" height="120">
                  ---->
                  <h2 class="flex my-4 primary--text">Anmelden</h2>
                </div>
                <v-form v-model="valid">
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
                    label="Password"
                    id="password"
                    type="password"
                    v-model="model.password"
                    :rules="[rules.required]"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
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
                <v-spacer></v-spacer>
                <v-btn color="error" @click="cancel">Zurück</v-btn>
                <v-btn
                  color="primary"
                  @click="login"
                  :disabled="!valid"
                  :loading="loading"
                  >Anmelden</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapState } from "vuex";
import * as actionBuilder from "@/api/actionBuilder";

export default {
  layout: "default",
  data: () => ({
    loading: false,
    query: "-",
    valid: false,
    rules: {
      required: (value) => !!value || "Required.",
      email: (v) =>
        !v ||
        /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,5})+$/.test(v) ||
        "E-mail must be valid",
    },
    model: {
      username: "",
      password: "",
    },
  }),

  methods: {
    login() {
      //this.loading = true;

      let redirect = "";
      if (this.$route.query.hasOwnProperty("redirect")) {
        redirect = this.$route.query.redirect;
      }
      let loginAction = [
        actionBuilder.newLoginUserAction(
          this.model.username,
          this.model.password,
          { redirect: redirect }
        ),
      ];
      this.$store.dispatch("actions/emitActionRequest", loginAction);
      this.$store.dispatch("user/login", null);
    },
    cancel() {
      this.$store.dispatch("user/logout", null);
      this.$router.push("/dashboard");
    },
  },
  mounted() {
    let redirect = "no";
    if (this.$route.query.hasOwnProperty("redirect")) {
      redirect = this.$route.query.redirect;
    }
    console.log("---->", redirect);
  },
};
</script>
<style scoped lang="css">
#login {
  height: 50%;
  width: 100%;
  min-width: 600px;
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  z-index: 0;
}
</style>
