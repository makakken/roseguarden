<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>
      <v-card min-height="100%">
        <v-card-title>
          <h3>Dein Nachrichten-Postfach</h3>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Suche"
            single-line
            hide-details
          ></v-text-field>
          <v-spacer></v-spacer>

          <div>
            <span>Sortieren:</span>
            <v-btn class="ma-2" tile color="primary" icon @click="toggleSort()">
              <v-icon v-if="sortAscending"> mdi-chevron-double-down</v-icon>
              <v-icon v-else> mdi-chevron-double-up</v-icon>
            </v-btn>
          </div>
        </v-card-title>

        <v-list
          dense
          single-line
          :style="isShort ? 'height: 450px' : 'height: 220px'"
          class="overflow-y-auto"
        >
          <v-list-item-group
            v-model="selected"
            mandatory
            dense
            active-class="blue--text"
          >
            <template v-for="(item, index) in sortedMessages">
              <v-list-item :key="item.id" @click="selectMessage(item)">
                <template v-slot:default="{ active, toggle }">
                  <v-list-item-content>
                    <v-list-item-title v-text="item.sender"></v-list-item-title>
                    <v-list-item-subtitle
                      class="text--primary"
                      v-text="item.subject"
                    ></v-list-item-subtitle>
                  </v-list-item-content>

                  <v-list-item-action>
                    <v-list-item-action-text
                      v-text="item.datetime"
                    ></v-list-item-action-text>
                    <v-icon v-if="!item.read" color="black" small>
                      email
                    </v-icon>
                  </v-list-item-action>
                </template>
              </v-list-item>
            </template>
          </v-list-item-group>
        </v-list>
      </v-card>
      <div v-if="!isShort">
        <br />
        <v-card min-height="300px">
          <v-card-title>
            <h3>
              {{ subject }}
            </h3>
            <v-spacer></v-spacer>
            <h5 style="text-align: right">
              {{ date }}
              <br />
              {{ sender }}
            </h5>
          </v-card-title>
          <v-container
            lg12
            sm12
            xs12
            style="height: 250px"
            class="overflow-y-auto"
          >
            <div v-html="messageHtml"></div>
          </v-container>
        </v-card>
      </div>
    </v-flex>
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <v-card width="100%">
        <v-toolbar dark color="primary">
          <v-btn icon dark @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>{{ subject }}</v-toolbar-title>
          <v-spacer></v-spacer>
          <div style="text-align: right">
            {{ date }}
            <br />
            {{ sender }}
          </div>
          <v-toolbar-items> </v-toolbar-items>
        </v-toolbar>
        <v-card-text class="text--primary" style="padding: 24px 24px 20px">
          <div v-html="messageHtml"></div>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import Vue from "vue";
import _ from "lodash";
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
  components: {},
  data: () => ({
    search: "",
    dialog: false,
    subject: "Keine Nachricht ausgewählt",
    date: "",
    sender: "",
    loading: true,
    isShort: false,
    sortAscending: false,
    search: "",
    headers: [],
    messages: [],
    actions: [],
    selected: null,
    messageHtml: "",
    items: [],
  }),
  beforeDestroy() {
    if (typeof window !== "undefined") {
      window.removeEventListener("resize", this.onResize, { passive: true });
    }
  },
  methods: {
    toggleSort() {
      if (this.sortAscending == true) {
        this.sortAscending = false;
      } else {
        this.sortAscending = true;
      }
    },
    selectMessage(item) {
      console.log("llll", item);
      let getMessageAction = [
        actionBuilder.newExecuteDataViewActionAction(
          "account",
          "userMessages",
          "getMesasge",
          { id: item.id }
        ),
      ];
      this.$store.dispatch("actions/emitActionRequest", getMessageAction).then(
        (response) => {
          console.log("getMessageAction - Succesfull", response);
          this.messageHtml = response.message;
          this.date = item.datetime;
          this.sender = item.sender;
        },
        (error) => {
          console.log("getMessageAction - Failed", error);
          this.messageHtml = "Not found";
          this.date = "";
          this.sender = "";
        }
      );

      if (this.isShort === true) {
        this.subject = item.subject;
        this.dialog = true;
        item.read = true;
      } else {
        this.subject = item.subject;
        item.read = true;
      }
    },
    onResize() {
      this.isShort = window.innerHeight < 700;
    },
    updateDone(item) {
      console.log("Toggle", item);
    },
    update(item) {
      // let createViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("account", "todoList", item)];
      // this.$store.dispatch('actions/emitActionRequest', createViewEntryAction);
      // console.log('Data saved', item);
    },
    requestViewAction(view, action, item) {},
    parseEntries(view) {
      if (this.viewDictionary.hasOwnProperty(view)) {
        return this.viewDictionary[view].entries;
      } else {
        return [];
      }
    },
    parseHeader(view) {
      let headers = [];
      let actionExist = false;
      if (this.viewDictionary.hasOwnProperty(view)) {
        this.viewDictionary[view].properties.forEach(function (item, index) {
          if (item.type === "action") {
            if (actionExist === false) {
              headers.push({
                text: "Actions",
                value: "actions",
                tooltip: item.label,
                action: item.action,
                name: item.name,
              });
            }
            actionExist = true;
          } else {
            headers.push({ text: item.label, value: item.name });
          }
        });
        return headers;
      } else {
        return [];
      }
    },
    onAddTodo() {
      let createViewEntryAction = [
        actionBuilder.newCreateViewAction("account", "userMessages"),
      ];
      this.$store.dispatch("actions/emitActionRequest", createViewEntryAction);
    },
  },
  computed: {
    ...mapState("views", ["viewDictionary"]),
    ...mapState("views", ["viewStates"]),
    isLoading: function () {
      return this.viewStates["account/userMessages"] !== "ready";
    },
    sortedMessages: function () {
      let msgs = _.sortBy(this.messages, [
        function (o) {
          return o.datetime;
        },
      ]);
      if (this.sortAscending == true) {
        return msgs;
      } else {
        return msgs.reverse();
      }
    },
  },
  watch: {
    viewStates(newValue, oldValue) {
      if (newValue["account/userMessages"] === "ready") {
        this.messages = this.parseEntries("account/userMessages");
        console.log("kkkkkk", this.messages);
        this.headers = this.parseHeader("account/userMessages");
      }
    },
  },
  mounted() {
    let getViewAction = [
      actionBuilder.newGetViewAction("account", "userMessages"),
    ];
    this.$store.dispatch("actions/emitActionRequest", getViewAction);
    this.onResize();
    window.addEventListener("resize", this.onResize, { passive: true });
  },
};
</script>

<style scoped>
</style>
