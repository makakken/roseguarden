<template>
  <v-container fluid>
    <v-card height="600px">
      <v-card-title>
        <h3>
          Nutzungsbedingungen:
        </h3>      </v-card-title>
      <v-card-text dense>
        <p>
          Wenn du mit folgenden Punkten nicht einverstanden bist, kannst du das Konglomerat e.V. Türschließsystem leider nicht nutzen.
        </p>
        <p>
          <ul>
            <li>
              Ich willige ein, das meine Daten zum Betrieb des Türschließsystems verarbeitet werden.
            </li>
            <li>
              Ich erkläre, dass meine Kontaktangaben korrekt sind.
            </li>
            <li>
              Ich akzeptiere die <a href="/privacy" target="_blank">
                Datenschutzbestimmungen
              </a>.
            </li>
            <li>
              Ich werde das System nur für seinen Zweck – des Zugangs zu den Räumen des Konglomerats – nutzen.
            </li>
            <li>
              Wenn mir fehlerhaftes Verhalten oder Defekte am System auffallen, werde ich diese schnellstmöglich und direkt an <a href="mailto:zugang@konglomerat.org">zugang@konglomerat.org</a> melden.
            </li>
            <li>
              Ich werde das System nicht manipulieren, um mir oder anderen Vorteile zu verschaffen.
            </li>
            <li>
              Ich werde ohne mein Beisein keinen anderen Personen Zugang zu den Räumen des Konglomerats ermöglichen.
            </li>
            <li>
              Ich werde mich regelmäßig und eigenständig auf dieser Seite über Änderungen an den Nutzungsbedingungen informieren. Diese werden hervorgehoben dargestellt.
            </li>
          </ul>
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
