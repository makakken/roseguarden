<template>
  <v-container fluid>
    <v-card>
      <v-card-title>
        <h3>Datenschutzbestimmung:</h3>
      </v-card-title>
      <v-card-text dense>
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Welche Daten sammelt ihr?</th>
                <th class="text-left">Wie lange werden die gespeichert?</th>
                <th class="text-left">Wer kann die Daten einsehen?</th>
                <th class="text-left">
                  Wie kann ich die Daten einsehen / löschen?
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  <p>
                    <strong> Deine Mitgliedsdaten </strong>
                    <br />
                    (Name, Email, ggfs. Gruppenzugehörigkeit,Handynummer)
                  </p>
                </td>
                <td>
                  <p>
                    So lange du Mitglied bist / Zugang hast + max. 12 Monate
                    <br />
                    (Wir machen einmal im Jahr Datenputz)
                  </p>
                </td>
                <td>
                  <p>
                    Du, wenn du dich
                    <a href="/user/register">hier</a>
                    anmeldest
                    <br />
                    Und die Admins / Stewards (Vorstand + Lichtvorstand +
                    Rosenritter-Entwicklerteam)
                  </p>
                </td>
                <td>
                  <p>
                    <strong>Einsehen und bearbeiten:</strong>
                    <br />
                    Melde dich
                    <a href="/user/register">hier</a>
                    an.
                    <br />
                    <strong>Löschen:</strong>
                    <br />
                    Mitgliedschaft / Nutzung kündigen über
                    <a href="mailto:vorstand@konglomerat.org">
                      vorstand@konglomerat.org
                    </a>
                  </p>
                </td>
              </tr>

              <tr>
                <td>
                  <p>
                    <strong> Deine Türöffnungen </strong>
                    <br />
                    (Wann hast du welche Tür mit welcher Karte geöffnet)
                  </p>
                </td>
                <td>
                  <p>3 Tage / 72 Stunden</p>
                </td>
                <td>
                  <p>
                    Nur Admins / Stewards
                    <br />
                    (Konglomerat Vorstand + Lichtvorstand +
                    Rosenritter-Entwicklungsteam)
                  </p>
                </td>
                <td>
                  <p>
                    <strong>Einsehen:</strong>
                    <br />
                    Durch eine Anfrage an
                    <a href="mailto:zugang@konglomerat.org">
                      zugang@konglomerat.org
                    </a>
                    <br />
                    <strong>Löschen:</strong>
                    <br />
                    3 Tage warten, dann werden sie automatisch gelöscht
                  </p>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>

        <h3>Was macht ihr mit meinen Daten?</h3>
        <br />
        <p>
          Wir geben sie niemandem weiter und nutzen sie nur dafür, dass unser
          Schließsystem technisch funktioniert. Dafür muss es eindeutig
          personenbezogene Accounts geben und das System muss sich für die
          Funktion 48h die Öffnungen merken. Um für das Debgging immer über ein
          Wochenende hinaus zu kommen, haben wir noch einen dritten Tag
          drangehängt, sodass nach 72 Stunden die Logs alle vom System gelöscht
          werden. Damit denken wir, eine datensparsame Variante gebaut zu haben,
          freuen uns aber über auch immer über Anmerkungen, wie das noch besser
          geht.
        </p>

        <h3>Wer sind die Admins / Stewards, die deine Daten sehen können?</h3>
        <br />

        <p>
          Die wenigsten Personen auf dieser Liste sehen wirklich deine Daten
          ein, aber alle haben theoretisch die Befugnis dazu. Daher haben alle
          eine Datenschutzbelehrung erhalten und unterschrieben, um
          klarzustellen, welche Verantwortung sie durch ihre Rolle tragen.
        </p>
        <p>
          Rechtlich verantwortlich für alles ist der
          <strong>Vorstand des Konglomerat e.V.</strong>: Carl Frenkel, Anna
          Seidel, Sarah Urban, Bettina Weber.
        </p>
        <p>
          Da der Vorstand aber traditionell auch die meisten Koordinations- und
          Verwaltungsarbeit macht, die sonst liegen bleibt, haben wir uns vor
          vielen Jahren entschlossen, einen
          <strong>Lichtvorstand</strong> an seine Seite zu stellen. Er trägt
          formell keine Verantwortung aber hat bei uns im Alltag die gleichen
          Rechte und Pflichten, nur mit weniger Arbeitspensum: Stephan
          Friedrich, Jens Kirchner, Robert Missbach, Fridolin Pflüger, Matthias
          Röder, Björn Seide
        </p>
        <p>
          Außerdem gibt es die ehrenamtliche Truppe der
          <strong>Rosenritter</strong>, die die Entwicklung des Systems
          vorantreibt und dafür auch Zugang zu allen Daten braucht: Marcus
          Drobisch, Stephan Friedrich,
        </p>
        <p>
          Bis Ende Juli 2021 wird das ehrenamtliche Team auch noch von
          <a href="https://binarylabs.dev" targe="_blank">Binary Labs</a>
          (Lennart Schierling, Robert Kunz) unterstützt, die bis dahin ebenfalls
          einen Admin Status haben, der dann aber verwirkt und sie damit auch
          ihren Zugang zu den Daten verlieren. Innerhalb ihres Vertrages mit dem
          Konglomerat e.V. ist es ihnen untersagt, jegliche Daten weiterzugeben.
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

<style scoped></style>
