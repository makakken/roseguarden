<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md5 lg5>
            <v-card class="elevation-1 pa-3">
              <v-card-text>
                <div class="layout column align-center">
                  <h2 class="flex my-4 primary--text">Registrieren</h2>
                  <v-alert type="info" class="mt-10">
                    <p>
                      Bitte achte darauf, dass Name und E-Mail mit deinen
                      <br />
                      Konglomerat-Mitgliedsdaten übereinstimmen!
                    </p>
                  </v-alert>
                </div>
                <v-form ref="form" v-model="valid">
                  <v-text-field
                    append-icon="email"
                    name="login"
                    label="E-Mail:"
                    required
                    type="text"
                    v-model="model.email"
                    :rules="rules.email"
                  >
                  </v-text-field>
                  <v-text-field
                    append-icon="lock"
                    name="password"
                    label="Passwort:"
                    id="password"
                    type="password"
                    v-model="model.password"
                    :rules="rules.password"
                  >
                  </v-text-field>
                  <v-text-field
                    append-icon="lock_open"
                    name="password"
                    label="Passwort wiederholen:"
                    id="password_verification"
                    type="password"
                    v-model="model.password_verification"
                    :rules="[rules.required, passwordVerificationRule]"
                  >
                  </v-text-field>
                  <v-text-field
                    append-icon="person"
                    name="login"
                    label="Vorname:"
                    type="text"
                    v-model="model.firstname"
                    :rules="[rules.required]"
                  >
                  </v-text-field>
                  <v-text-field
                    append-icon="people"
                    name="login"
                    label="Nachname:"
                    type="text"
                    v-model="model.lastname"
                    :rules="[rules.required]"
                  >
                  </v-text-field>
                  <v-text-field
                    append-icon="home"
                    name="login"
                    label="Gruppenzugehörigkeit (nur für Gruppenmitglieder relevant):"
                    type="text"
                    v-model="model.organization"
                  >
                  </v-text-field>
                  <v-text-field
                    append-icon="phone"
                    label="Telefonnummer (optional):"
                    name="phone"
                    v-model="model.phone"
                    type="text"
                  >
                  </v-text-field>
                  <v-row>
                    <v-col cols="1">
                      <v-switch
                        dense
                        v-model="switchMe"
                        :rules="[rules.accept]"
                        style="display: inline-block; margin: 0; padding: 0"
                      >
                      </v-switch>
                    </v-col>
                    <v-col cols="11">
                      <p class="v-label theme--light">
                        Ich bestätige, dass ich zugangsberechtigtes Mitglied des
                        Konglomerat e.V. bin oder eine temporäre Nutzung des
                        #Rosenwerks erworben habe.
                      </p>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="1">
                      <v-switch
                        dense
                        v-model="switchMe2"
                        :rules="[rules.accept]"
                        style="display: inline-block; margin: 0; padding: 0"
                      >
                      </v-switch>
                    </v-col>
                    <v-col cols="11">
                      <p class="v-label theme--light">
                        Ich habe die
                        <a href="/termsofuse" target="_blank">
                          Nutzungsvereinbarung
                        </a>
                        und die
                        <a href="/privacy" target="_blank">
                          Datenschutzerklärung
                        </a>
                        gelesen und erkläre mich damit einverstanden.
                      </p>
                    </v-col>
                  </v-row>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-row>
                  <v-col cols="12"> </v-col>
                </v-row>
                <v-row justify="end">
                  <v-col cols="6" md="5" lg="4" class="text-right">
                    <v-btn color="secondary" @click="cancel"> Abbrechen </v-btn>
                  </v-col>
                  <v-col cols="6" md="5" lg="4" class="text-right">
                    <v-btn
                      color="primary"
                      @click="signup"
                      :disabled="!valid"
                      :loading="loading"
                    >
                      Registrieren
                    </v-btn>
                  </v-col>
                  <v-col cols="1" />
                </v-row>
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
    switchMe2: false,
    switchMe: false,
    model: {
      email: "",
      firstname: "",
      lastname: "",
      organization: "",
      phone: "",
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
