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
                    Register Roseguarden account
                  </h2>
                </div>
                <v-form ref="form" v-model="valid">
                  <v-text-field
                    append-icon="email"
                    name="login"
                    label="eMail"
                    required
                    type="text"
                    v-model="model.email"
                    :rules="rules.email"
                  ></v-text-field>
                  <v-text-field
                    append-icon="lock"
                    name="password"
                    label="Password"
                    id="password"
                    type="password"
                    v-model="model.password"
                    :rules="rules.password"
                  ></v-text-field>
                  <v-text-field
                    append-icon="lock_open"
                    name="password"
                    label="Repeat password"
                    id="password_verification"
                    type="password"
                    v-model="model.password_verification"
                    :rules="[rules.required, passwordVerificationRule]"
                  ></v-text-field>
                  <v-text-field
                    append-icon="person"
                    name="login"
                    label="First name"
                    type="text"
                    v-model="model.firstname"
                    :rules="[rules.required]"
                  ></v-text-field>
                  <v-text-field
                    append-icon="people"
                    name="login"
                    label="Last name"
                    type="text"
                    v-model="model.lastname"
                    :rules="[rules.required]"
                  ></v-text-field>
                  <v-text-field
                    append-icon="home"
                    name="login"
                    label="Organization"
                    type="text"
                    v-model="model.organization"
                  ></v-text-field>

                  <v-switch
                    dense
                    v-model="switchMe"
                    :rules="[rules.accept]"
                    style="display: inline-block"
                  >
                    <template v-slot:label>
                      I have read and accept the &nbsp;
                    </template>
                  </v-switch>
                  <router-link to="/termsofuse" target="_blank">
                    Terms of use.
                  </router-link>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="error" @click="cancel"> Cancel</v-btn>
                <v-btn
                  color="primary"
                  @click="signup"
                  :disabled="!valid"
                  :loading="loading"
                  >Register</v-btn
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
import Vue from "vue";
import * as actionBuilder from "@/api/actionBuilder";

export default {
  layout: "default",
  data: () => ({
    loading: false,
    valid: true,
    model: {
      email: "",
      firstname: "",
      lastname: "",
      organization: "",
      terms: "",
      password: "",
      password_verification: "",
    },
    rules: {
      required: (v) => !!v || "Value is required",
      accept: (v) => !!v || "Have to be accepted",

      password: [
        (v) =>
          /(.){7,}\w+/.test(v) || "Password have to have at least 8 characters",
        (v) => !!v || "Password is required",
      ],
      email: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
    },
  }),
  computed: {
    passwordVerificationRule() {
      return () =>
        this.model.password === this.model.password_verification ||
        "Password must match";
    },
  },
  methods: {
    cancel() {
      this.$router.push("/dashboard");
    },
    signup() {
      console.log(this.model);
      if (this.$refs.form.validate()) {
        let registerAction = [actionBuilder.newRegisterUserAction(this.model)];
        this.$store.dispatch("actions/emitActionRequest", registerAction);
      }
    },
  },
  mounted() {
    this.$validator.localize("en", this.validations);
  },
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
