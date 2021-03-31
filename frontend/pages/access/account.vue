<template>
  <v-container fluid>
    <v-card>
      <v-card-title>
        <h3>Deine Zugänge</h3>
        <v-spacer></v-spacer>
      </v-card-title>

      <v-row dense>
        <v-col cols="1" />
        <v-col cols="10">
          <v-alert type="info">Aktuell: Under Construction</v-alert>
        </v-col>
      </v-row>
      <!--
      <v-row dense>
        <v-progress-linear
          indeterminate
          color="primary"
          v-if="loading"
        ></v-progress-linear>
      </v-row>
      <v-row dense>
        <v-col cols="1"/>
        <v-col cols="10">
          <v-subheader>Access group:</v-subheader>
          <v-text-field
            label="eMail"
            v-model="accountdata.email"
            :loading="loading"
            hide-details
            disabled
            solo
            dense
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row dense>
        <v-col cols="1"/>
        <v-col cols="10">
          <v-subheader>Access info:</v-subheader>
          <v-text-field
            label="Your first name"
            value="Max"
            v-model="accountdata.firstname"
            :loading="loading"
            disabled
            hide-details
            solo
            dense
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row dense>
        <v-col cols="1"/>
        <v-col cols="5">
          <v-subheader>Valid from:</v-subheader>
          <v-text-field
            name="pin"
            label="Your new pin"
            id="pin"
            disabled
            hide-details
            solo
            dense
            v-model="pin" >
          </v-text-field>
        </v-col>
        <v-col cols="5">
          <v-subheader>Expires at:</v-subheader>
          <v-text-field
            name="pin_verification"
            label="Repeat your new pin"
            id="pin_verification"
            disabled
            hide-details
            solo
            dense
            v-model="pin_verification" >
          </v-text-field>
        </v-col>
      </v-row>
      <v-row dense>
        <v-col cols="1"/>
        <v-col cols="10">
          <v-subheader>On following weekdays</v-subheader>
          <v-text-field
            label="Your last name"
            v-model="accountdata.lastname"
            :loading="loading"
            disabled
            hide-details
            solo
            dense
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row dense>
        <v-col cols="1"/>
        <v-col cols="5">
          <v-subheader>From time:</v-subheader>
          <v-text-field
            name="pin"
            label="Your new pin"
            id="pin"
            disabled
            hide-details
            solo
            dense
            v-model="pin" >
          </v-text-field>
        </v-col>
        <v-col cols="5">
          <v-subheader>To time:</v-subheader>
          <v-text-field
            name="pin_verification"
            label="Repeat your new pin"
            id="pin_verification"
            disabled
            hide-details
            solo
            dense
            v-model="pin_verification" >
          </v-text-field>
        </v-col>
      </v-row>
      <v-row dense>
        <v-col cols="1"/>
        <v-col cols="10">
          <v-subheader>Access to spaces:</v-subheader>
          <v-text-field
            label="No organization"
            v-model="accountdata.organization"
            :loading="loading"
            hide-details
            disabled
            solo
            dense
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row dense>
        <v-col cols="1"/>
        <v-col cols="10">
          <v-subheader>Last updated at:</v-subheader>
          <v-text-field
            label="13.06.2020"
            v-model="accountdata.phone"
            :loading="loading"
            hide-details
            solo
            dense
          ></v-text-field>
        </v-col>
      </v-row>
      -->
      <br />
    </v-card>
    <br />
  </v-container>
</template>

<script>
import Vue from "vue";
import * as actionBuilder from "@/api/actionBuilder";
import { createHelpers } from "vuex-map-fields";

import { mapState } from "vuex";

// The getter and mutation types are provided to the vue module
// they must be the same as the function names used in the store.
const { mapFields } = createHelpers({
  getterType: "views/getView",
  mutationType: "views/updateView",
});

export default {
  layout: "dashboard",
  data() {
    return {
      showOld: false,
      showNew: false,
      showRepeat: false,
      loading: true,
      accountdata: {},
      valid_pin: true,
      valid_requestKey: true,
      pin_password: "",
      pin_verification: "",
      pin: "",
      valid_password: true,
      oldpassword: "",
      password: "",
      password_verification: "",
      cardStatus: "No card assigned",
      cardValid: true,
      cardRequestKey: "",
      rules: {
        required: (v) => !!v || "Is required",
        pin_digits: (v) => /([0-9]{6})/.test(v) || "Pin have to have 6 digits",
        pin_length: (v) => v.length == 6 || "Pin have to have 6 digits",
        requestKey_digits: (v) =>
          /([0-9A-Za-z]{12})/.test(v) ||
          "The request key have to have 12 characters",
        requestKey_length: (v) =>
          v.length == 12 || "The request key have to have 12 characters",
        pin: [
          (v) => /([0-9]{6})/.test(v) || "Pin have to have 6 digits",
          (v) => v.length == 6 || "Pin have to have 6 digits",
          (v) => !!v || "Pin is required",
        ],
        password: (v) =>
          /(.){7,}\w+/.test(v) || "Password have to have at least 8 characters",
        email: [
          (v) => !!v || "E-mail is required",
          (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
        ],
      },
    };
  },
  methods: {
    uppercase() {
      this.cardRequestKey = this.cardRequestKey.toUpperCase();
    },
    getAccountData(view) {
      if (this.viewDictionary.hasOwnProperty(view)) {
        return this.viewDictionary[view].entries[0];
      } else {
        return {};
      }
    },
    submitUnassignCard() {
      this.cardValid = false;
    },
    submitAssignCard() {
      this.cardValid = true;
    },
    cancelData() {
      this.accountdata = Object.assign({}, this.getAccountData("userInfo"));
      console.log("cancelData");
    },
    submitUserInfo() {
      let entry = {
        email: this.accountdata.email,
        firstname: this.accountdata.firstname,
        lastname: this.accountdata.lastname,
        organization: this.accountdata.organization,
        phone: this.accountdata.phone,
      };
      console.log("submitUserInfo", entry);
      let getViewAction = [
        actionBuilder.newUpdateDataViewEntryAction(
          "account",
          "userInfo",
          entry
        ),
      ];
      this.$store.dispatch("actions/emitActionRequest", getViewAction);
    },
    submitChangePin() {
      console.log("submitChangePin");
      let getViewAction = [
        actionBuilder.newChangePinAction(
          "account",
          this.pin_password,
          this.pin
        ),
      ];
      this.$store.dispatch("actions/emitActionRequest", getViewAction);
    },
    submitChangePassword() {
      console.log("submitChangePin");
      let getViewAction = [
        actionBuilder.newChangePasswordAction(
          "account",
          this.oldpassword,
          this.password
        ),
      ];
      this.$store.dispatch("actions/emitActionRequest", getViewAction);
    },
  },
  computed: {
    ...mapState("views", ["viewDictionary"]),
    ...mapState("views", ["viewStates"]),
    passwordVerificationRule() {
      return () =>
        this.password === this.password_verification ||
        this.password_verification === "" ||
        "Passwords must match";
    },
    pinVerificationRule() {
      return () =>
        this.pin === this.pin_verification ||
        this.pin_verification === "" ||
        "Pins must match";
    },
  },
  watch: {
    viewStates(newValue, oldValue) {
      console.log("change on viewStates detected with", newValue, oldValue);
      if (this.viewStates["account/userInfo"] === "ready") {
        this.accountdata = Object.assign(
          {},
          this.getAccountData("account/userInfo")
        );
        this.loading = false;
      } else {
        this.loading = true;
      }
    },
  },
  mounted() {
    let getViewAction = [actionBuilder.newGetViewAction("account", "userInfo")];
    this.$store.dispatch("actions/emitActionRequest", getViewAction);
  },
};
</script>

<style scoped>
</style>
