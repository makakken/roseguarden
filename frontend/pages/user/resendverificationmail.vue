<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-text>
                <div class="layout column align-center">
                  <!---
                  <img src="../static/konglo_logo.png" alt="Roseguarden logo" width="120" height="120">
                  ---->
                  <h2 class="flex my-4 primary--text">
                    Resend verification request?
                  </h2>
                </div>
                <v-form v-model="valid">
                  <v-text-field
                    append-icon="person"
                    name="email"
                    label="Enter your email address"
                    type="email"
                    :rules="[rules.email, rules.required]"
                    v-model="email"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="error" @click="cancel">Cancel</v-btn>
                <v-btn color="primary" :disabled="!valid" @click="send"
                  >Send</v-btn
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
  props: ["actionhash"],
  data: () => ({
    showOld: false,
    showNew: false,
    email: "",
    valid: false,
    showRepeat: false,
    loading: true,
    error: true,
    password: "",
    confirmPassword: "",
    info: "",
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => v.length >= 8 || "Min. 8 characters",
      pin: (v) => v.length >= 4 || "Min. 4 characters",
      email: (v) =>
        !v ||
        /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,5})+$/.test(v) ||
        "E-mail must be valid",
    },
  }),
  computed: {
    ...mapState("actionlink", ["status", "message"]),
    passwordMatch() {
      return [
        this.password === this.confirmPassword || "The passwords don't match",
      ];
    },
  },
  watch: {
    status(newValue, oldValue) {
      if (newValue === "success") {
        this.error = false;
      } else {
        this.error = true;
      }

      this.info = this.message;
      this.loading = false;
    },
  },
  methods: {
    send() {
      let lostPasswordAction = [
        actionBuilder.newResendVerfificationMailAction(this.email),
      ];
      this.$store.dispatch("actions/emitActionRequest", lostPasswordAction);
    },
    cancel() {
      this.$router.push("/dashboard");
    },
  },
  mounted() {},
};
</script>
<style scoped lang="css">
#login {
  height: 50%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  z-index: 0;
}
</style>
