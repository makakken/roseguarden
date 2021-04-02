<template>
  <v-container fluid>
    <v-card>
      <v-card-title>
        <h3>
          FAQ:
        </h3>
      </v-card-title>
      <v-card-text dense>
        <h3>
          <br />
          <p>
            REGISTRIERUNG &amp; ANMELDUNG
          </p>
        </h3>

        <v-expansion-panels focusable>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Warum soll ich mich hier registrieren?
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <p>
                Mit der Registrierung auf dieser Seite hast du den letzten
                Schritt gemacht, um eigenständig in die Werkstatträume zu
                gelangen und diese zu nutzen.
              </p>
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>
              Muss ich als Neumitglied trotzdem noch einen Mitgliedsantrag
              ausfüllen?
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              Ja! Zuerst
              <a
                href="https://konglomerat.org/_Resources/Persistent/da0c10c749105d77eeb63776e2f07e2d05fabcbb/200805_Mitgliedschaftsantrag.pdf"
                target="_blank"
              >
                Mitgliedsantrag
                <small>(PDF - 1.6Mb)</small>
              </a>
              , dann Schließsystemregistrierung.
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>
              Ich habe mein Passwort vergessen.
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <a href="/user/lostpassword">Hier</a>
              kannst auch eine E-Mail zum Zurücksetzen anfordern.
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>

        <h3>
          <br />
          <p>
            KARTEN
          </p>
        </h3>

        <v-expansion-panels focusable>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Wie komm ich an meine Karte?
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <p>
                Deine Karte stellt Betti aus, du erreichst sie unter
                <a href="mailto:betti@konglomerat.org">
                  betti@konglomerat.org
                </a>
                .
              </p>
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>
              Ich habe meine Karte verloren!
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <p>
                Du kannst sie selbst sperren, wenn du dich hier anmeldest.
              </p>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>

        <h3>
          <br />
          <p>
            TÜREN
          </p>
        </h3>

        <v-expansion-panels focusable>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Welche Türen sind schließbar?
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <p>
                Die Außentür in Richtung Kunststoffschmeidecontainer sowie die
                Tür vom Flur in den RON (Raum ohne Namen = Der mit der Küche,
                dem Runden Tisch, Elektro-, Näh- und Digitaldruckwerkstatt
                drin).
              </p>
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>
              Worauf muss ich noch achten?
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <p>
                Nimm den Strick raus bitte!!!
              </p>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>

        <h3>
          <br />
          <p>
            DATENSCHUTZ
          </p>
        </h3>

        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">
                  Welche Daten sammelt ihr?
                </th>
                <th class="text-left">
                  Wie lange werden die gespeichert?
                </th>
                <th class="text-left">
                  Wer kann die Daten einsehen?
                </th>
                <th class="text-left">
                  Wie kann ich die Daten einsehen / löschen?
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  <p>
                    <strong>
                      Deine Mitgliedsdaten
                    </strong>
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
                    <strong>
                      Deine Türöffnungen
                    </strong>
                    <br />
                    (Wann hast du welche Tür mit welcher Karte geöffnet)
                  </p>
                </td>
                <td>
                  <p>
                    3 Tage / 72 Stunden
                  </p>
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

        <v-expansion-panels focusable>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Was macht ihr mit meinen Daten?
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <p>
                Wir geben sie niemandem weiter und nutzen sie nur dafür, dass
                unser Schließsystem technisch funktioniert.
                <br />
                Dafür muss es eindeutig personenbezogene Accounts geben und das
                System muss sich für die Funktion 48h die Öffnungen merken.
                <br />
                Um für das Debgging immer über ein Wochenende hinaus zu kommen,
                haben wir noch einen dritten Tag drangehängt, sodass nach 72
                Stunden die Logs alle vom System gelöscht werden.
                <br />
                Damit denken wir, eine datensparsame Variante gebaut zu haben,
                freuen uns aber über auch immer über Anmerkungen, wie das noch
                besser geht.
              </p>
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>
              Wer sind die Admins / Stewards, die eine Daten sehen können?
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <p>
                Die wenigsten Personen auf dieser Liste sehen wirklich deine
                Daten ein, aber alle haben theoretisch die Befugnis dazu. Daher
                haben alle eine Datenschutzbelehrung erhalten und
                unterschrieben, um klarzustellen, welche Verantwortung sie durch
                ihre Rolle tragen.
              </p>
              <p>
                Rechtlich verantwortlich für alles ist der
                <strong>Vorstand des Konglomerat e.V.</strong>: Carl Frenkel,
                Anna Seidel, Sarah Urban, Bettina Weber.
              </p>
              <p>
                Da der Vorstand aber traditionell auch die meisten
                Koordinations- und Verwaltungsarbeit macht, die sonst liegen
                bleibt, haben wir uns vor vielen Jahren entschlossen, einen
                <strong>Lichtvorstand</strong> an seine Seite zu stellen. Er
                trägt formell keine Verantwortung aber hat bei uns im Alltag die
                gleichen Rechte und Pflichten, nur mit weniger Arbeitspensum:
                Stephan Friedrich, Jens Kirchner, Robert Missbach, Fridolin
                Pflüger, Matthias Röder, Björn Seide
              </p>
              <p>
                Außerdem gibt es die ehrenamtliche Truppe der
                <strong>Rosenritter</strong>, die die Entwicklung des Systems
                vorantreibt udn dafür auch Zugang zu allen Daten braucht: Marcus
                Drobisch, Hannes Korn, Kevin Krechan, Stephan Kropop, Stephan
                Friedrich,
              </p>
              <p>
                Bis Ende Juli 2021 wird das ehrenamtliche Team auch noch von
                <a href="https://binarylabs.dev" targe="_blank">Binary Labs</a>
                (Lennart Schierling, Robert Kunz) unterstützt, die bis dahin
                ebenfalls einen Admin Status haben, der dann aber verwirkt und
                sie damit auch ihren Zugang zu den Daten verlieren. Innerhalb
                ihres Vertrages mit dem Konglomerat e.V. ist es ihnen untersagt,
                jegliche Daten weiterzugeben.
              </p>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
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
