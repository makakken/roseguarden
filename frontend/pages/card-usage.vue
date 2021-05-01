<template>
  <v-container fluid>
    <v-card>
      <v-card-title>
        <h2>
          Kartenbenutzung:
        </h2>
      </v-card-title>
      <v-card-text dense>
        <p>
          Bitte habt Geduld mit dem Schließsystem.
          <br />
          Wie unten gezeigt, gibt es jetzt ein direktes Feedback am Display des
          Schließsystem's.
        </p>
        <p>
          <strong>
            Hinweis:
          </strong>
          <br />
          Das Abfragen der Zugangsberechtigung kann ca.
          <strong>10 - 30sec.</strong> dauern.
          <br />
          Falls ihr keinen Zugang bekommt, liegt dass warscheinlich an einer
          fehlenden Berechtigung.
        </p>
        <p>
          Die Abfrage der Zugangsberechtigung sollte nicht länger als
          <strong>1 Minute</strong> dauern.
          <br />
          Wartet ihr schon länger, legt die Schlüsselkarte erneut an den Sensor.
          <br />
          Hilft das nicht, könnt ihr erst einmal nur eine Support-E-Mail an
          <a href="mailto:zugang@konglomerat.org">zugang@konglomerat.org</a>
          schreiben.
        </p>

        <p>
          Weiter Hilfe bekommt ihr auch im
          <nuxt-link to="/faq">FAQ</nuxt-link>
        </p>

        <br />
        <h2>
          Türöffnung's Schritte
        </h2>
        <p>
          <br />
          Hier eine bebilderte Beschreibung, wie ihr das Schließsystem vor Ort
          nutzt.
        </p>

        <v-container class="lighten-5">
          <v-row class="xs-12">
            <v-col>
              <CardInfo attrImgSource="/images/1-card-reader-infoyer.jpg">
                <template v-slot:header>
                  1.1. Tür Schließsystem, Infoyer
                </template>
                <template v-slot:content>
                  Außenansicht des Eingangs
                </template>
                <template v-slot:content-hidden>
                  <ol>
                    <li>
                      Internes Display mit Statusanzeige
                    </li>
                    <li>
                      Externer RFID-Sensor
                    </li>
                  </ol>
                </template>
              </CardInfo>
            </v-col>
            <v-col>
              <CardInfo attrImgSource="/images/1-card-reader-ron.jpg">
                <template v-slot:header>
                  1.2. Tür Schließsystem, RON
                </template>
                <template v-slot:content>
                  Außenansicht des Eingangs
                </template>
                <template v-slot:content-hidden>
                  <ol>
                    <li>
                      Internes Display mit Statusanzeige
                    </li>
                    <li>
                      Externer RFID-Sensor
                    </li>
                  </ol>
                </template>
              </CardInfo>
            </v-col>
          </v-row>
          <v-row class="xs-12">
            <v-col>
              <CardInfo attrImgSource="/images/2-present-card.jpg">
                <template v-slot:header>
                  3. -- Karte anlegen
                </template>
                <template v-slot:content>
                  Status Display (normal)
                </template>
                <template v-slot:content-hidden>
                  <ul>
                    <li>
                      <p>
                        <strong>RON</strong>
                        Name des Schließsystem's:
                        <br />
                        (Anzeige, oben Links)
                      </p>
                    </li>
                    <li>
                      <p>
                        <strong>PRESENT CARD</strong>
                        <br />
                        Haupt Statusanzeige
                        <br />
                        (Aufforderung die Schlüsselkarte anzulegen.)
                      </p>
                    </li>
                    <li>
                      <p>
                        <strong>NO CARD DETECTED</strong>
                        <br />
                        Statusanzeige der Kartenerkennung
                        <br />
                        (Es ist keine Schlüsselkarte angelegt.)
                      </p>
                    </li>
                    <li>
                      <p>
                        <strong>DOOR LOCKED</strong>
                        <br />
                        Statusanzeige des Türschlosses
                        <br />
                        (Die Tür ist verriegelt.)
                      </p>
                    </li>
                    <li>
                      <p>
                        <strong>CONNECTED TO AP</strong>
                        <br />
                        Statusanzeige des Netzwerk's
                        <br />
                        (Das Schließsystem ist mit dem Access-Point, dem Server
                        verbunden)
                      </p>
                    </li>
                  </ul>
                </template>
              </CardInfo>
            </v-col>
            <v-col>
              <CardInfo attrImgSource="/images/3-card-attached.jpg">
                <template v-slot:header>
                  4. -- Karte wird angelegt
                </template>
                <template v-slot:content-hidden>
                  <ul>
                    <li>
                      Die Schlüsselkarte an die markierten Stelle des
                      RFID-Lesegerätes (unteres Ende) halten.
                    </li>
                  </ul>
                </template>
              </CardInfo>
            </v-col>
            <v-col>
              <CardInfo attrImgSource="/images/4-card-detected.jpg">
                <template v-slot:header>
                  5 -- Karten erkennung
                </template>
                <template v-slot:content-hidden>
                  <ul>
                    <li>
                      <p>
                        <strong>CARD DETECTED</strong>
                        <br />
                        (Statusanzeige des Kartenlesegeräte)
                      </p>
                    </li>
                  </ul>
                  <ol>
                    <li>
                      <p>
                        Eine Schlüsselkarte wurde erkannt
                      </p>
                    </li>
                    <li>
                      <p>
                        Die Zugangsberechtigung wird am System abgefragt.
                        <br />
                        Das kann <strong>ca. 10-30sec</strong> dauern
                      </p>
                    </li>
                  </ol>
                </template>
              </CardInfo>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <CardInfo attrImgSource="/images/5-access-denied.jpg">
                <template v-slot:header>
                  6.1 -- Zugang verweigert
                </template>
                <template v-slot:content-hidden>
                  <ol>
                    <li>
                      Die verwendete Schlüsselkarte wurde erkannt.
                    </li>
                    <li>
                      Die Schlüsselkarte hat
                      <strong>
                        keine Zugangsberechtigung
                      </strong>
                      vom System erhalten.
                    </li>
                  </ol>
                </template>
              </CardInfo>
            </v-col>
            <v-col>
              <CardInfo attrImgSource="/images/5-access-granted.jpg">
                <template v-slot:header>
                  6.1 -- Zugang gewährt
                </template>
                <template v-slot:content-hidden>
                  <ol>
                    <li>
                      Die verwendete Schlüsselkarte wurde erkannt.
                    </li>
                    <li>
                      Das Schließsystem "klackt", und
                      <strong>öffnet</strong> die Tür.
                    </li>
                  </ol>
                </template>
              </CardInfo>
            </v-col>
          </v-row>
        </v-container>
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
import CardInfo from "@/components/card-info/card-info";

Vue.use(VueAxios, axios);

export default {
  layout: "dashboard",
  components: {
    CardInfo
  },
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
