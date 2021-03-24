<template>
  <v-container fluid>
    <v-card height="600px">
      <v-card-title>
        <h3>Über uns</h3>
      </v-card-title>
      <v-card-text dense>
        <p>
          Ja, es ist endlich soweit! Nach Jahren des Bangens, Hoffens und
          ehrenamtlichen Entwickelns läuft jetzt tatsächlich die neue Version
          des Konglomerat Schließsystems!! Das Open Source Projekt dahinter
          heißt Roseguarden und wurde extra aus dem #Rosenwerk für das
          #Rosenwerk entwickelt.
        </p>
        <p>
          Warum? Schlüssel sind so ziemlich 80er. Und kommerziell verfügbare
          RFID Systeme sind für unsere Möglichkeiten zu teuer bzw. kommen mit
          den verschiedenen Mitgliedstarifen und Zugangsberechtigungen des
          Konglomerat nicht ohne weiteres klar. Außerdem träumen wir davon, hier
          in Zukunft auch Mitgliederverwaltung, Motorschlösser und
          Maschinenzugänge einzubauen und diese Anpassbarkeit kriegt man mit den
          fertigen Lösungen nicht.
        </p>

        <p>
          Eine ausgiebige Huldigung geht an dieser Stelle raus an die
          Rosenritter-Crew ohne deren Arbeit das Zugangssystem und damit auch
          das #Rosenwerk nie so groß hätten werden können.
        </p>
        <v-alert type="info">
          Wir suchen weiterhin ehrenamtliche Unterstützung für die Betreung und
          Weiterentwicklung des Systems. Wenn du mitmachst, ist dir ewiger
          Konglo-Dank gewiss. Zu lernen gibt’s für dich sicher auch jede Menge.
          Melde dich bei Interesse unter zugang@konglomerat.org.
        </v-alert>
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
