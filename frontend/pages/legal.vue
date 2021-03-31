<template>
  <v-container fluid>
    <v-row dense justify="center">
      <v-col cols="12" height="100%">
        <v-card height="100%">
          <v-card-title>
            <h3>
              Impressum
            </h3>
          </v-card-title>
          <v-card-text dense>
            <p>
              Verantwortung für Administration und Betrieb des Systems sowie
              Inhalte dieser Webseite im Sinne des §5 TMG:
            </p>
            <strong>
              Konglomerat e.V.
            </strong>
            <p>
              Jagdweg 1-3
              <br />
              01159 Dresden
            </p>
            <p>
              vertreten durch den Vorstand: Carl Frenkel, Anna Seidel, Sarah
              Urban und Bettina Weber.
            </p>
            <p>
              Vereinsregisternummer: VR 5771, Amtsgericht Dresden
              <br />
              Steuernummer: 203 I 140 I 18533 K08
              <br />
              UST-ID: DE318655778
            </p>
            <p>
              Get in touch…
              <br />
              <a href="tel:+49 1639031023">01639031023</a>
              <br />
              <a href="mailto:vorstand@konglomerat.org">
                vorstand@konglomerat.org
              </a>
            </p>
            <p>
              Du kannst auch Mitglied werden, vorher aber bitte
              <a
                href="https://konglomerat.org/_Resources/Persistent/da0c10c749105d77eeb63776e2f07e2d05fabcbb/200805_Mitgliedschaftsantrag.pdf"
                target="_blank"
              >
                diesen Bogen
              </a>
              <small>(PDF - 1.6Mb)</small>
              ausfüllen
            </p>
            <br />

            <h3>
              LIZENZ
            </h3>
            <ul>
              <li>
                Server: GPLv3
              </li>
              <li>
                Website: MIT
              </li>
              <li>
                Hardware: Open Hardware bzw. GPLv3.
              </li>
            </ul>
            <br />

            <h3>
              HAFTUNGSAUSSCHLUSS
            </h3>
            <br />
            <h4>
              Haftung für Inhalte
            </h4>
            <p>
              Die Inhalte unserer Seiten wurden mit größter Sorgfalt erstellt.
              Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte
              kann ich jedoch keine Gewähr übernehmen. Als Diensteanbieter bin
              ich gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach
              den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG bin
              ich als Diensteanbieter jedoch nicht verpflichtet, übermittelte
              oder gespeicherte fremde Informationen zu überwachen oder nach
              Umständen zu forschen, die auf eine rechtswidrige Tätigkeit
              hinweisen. Verpflichtungen zur Entfernung oder Sperrung der
              Nutzung von Informationen nach den allgemeinen Gesetzen bleiben
              hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab
              dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung
              möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen
              werde ich diese Inhalte umgehend entfernen.
            </p>
            <br />
            <h4>
              Haftung für Links
            </h4>
            <p>
              Diese Webseite enthält Links zu externen Webseiten Dritter, auf
              deren Inhalte wir keinen Einfluss haben. Deshalb können wir für
              Inhalte 3. keine Gewähr übernehmen. Für die Inhalte der verlinkten
              Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten
              verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der
              Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige
              Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine
              permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch
              ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar.
              Bei Bekanntwerden von Rechtsverletzungen werden wir derartige
              Links umgehend entfernen.
            </p>
            <br />
            <h4>
              Urheberrecht
            </h4>
            <p>
              Die durch der Seitenbetreiber erstellten Inhalte und Werke auf
              diesen Seiten unterliegen dem deutschen Urheberrecht. Die
              Vervielfältigung, Bearbeitung, Verbreitung und jede Art der
              Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der
              schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.
              Downloads und Kopien dieser Seite sind nur für den privaten, nicht
              kommerziellen Gebrauch gestattet. Soweit die Inhalte auf dieser
              Seite nicht vom Betreiber erstellt wurden, werden die
              Urheberrechte Dritter beachtet. Insbesondere werden Inhalte
              Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine
              Urheberrechtsverletzung aufmerksam werden, bitten wir Sie um einen
              entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen
              werden wir derartige Inhalte umgehend entfernen.
            </p>

            <h4>
              Datenschutz
            </h4>
            <p>
              Die
              <a href="/privacy" target="_blank">
                Datenschutzerklärung
              </a>
              ist hier nachzulesen.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Vue from "vue";
import { codemirror } from "vue-codemirror";
import { mapState } from "vuex";
import moment from "moment";

// import { GenericNode } from '@/nodes/generic'

import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);

export default {
  layout: "dashboard",
  components: {},
  data: () => ({
    info: ""
  }),
  methods: {
    ok() {}
  },
  watch: {
    info: function(val) {}
  },
  computed: {
    test: function() {}
  },
  created() {},
  mounted() {}
};
</script>

<style scoped></style>
