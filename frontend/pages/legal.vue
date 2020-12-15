<template>
  <v-container fluid>
    <v-row dense justify="center">
      <v-col cols="12" height="100%">
        <v-card height="100%">
          <v-card-title >
            <h3>
              Legal notice
            </h3>
          </v-card-title>
          <v-card-text dense>        
            <h2>
              Information in accordance with § 5 TMG 
            </h2>
            <br/>          
            <img src="../static/person_eng.png" height="110px">    
            <br/>
            <br/>
            <h2>
              Contact
            </h2>
            <br/>
            <img src="../static/contact.png" height="40px">    
            <br/>
            <br/>

            <h2>
              Disclaimer
            </h2>
            <br/>
            <h3>
              Warranty
            </h3>
            <p>
              This service is based on free software. It comes without any warranty, to
              the extent permitted by applicable law. Be aware that the usage of roseguarden is on your own risk.
            </p>
            <br>            
            <h3>
              Accountability for content
            </h3>
            <br/>
            <p>
              The contents of this pages have been created with great care. However, we cannot guarantee all the contents 
              accuracy, completeness or topicality. According to statutory provisions, we are furthermore responsible for our
              own content on these web pages. In this matter, please note that we are not obliged to monitor the transmitted or 
              saved information of third parties, or investigate circumstances pointing to illegal activity. Our obligations 
              to remove or block the use of information under generally applicable laws remain unaffected by this as per 
              §§ 8 to 10 of the Telemedia Act (TMG). 
            </p>
            <br/>
            <h3>
              Accountability for links
            </h3>
            <br/>
            <p>
              This website contains links to external third-party websites, over the content of which we have no control. 
              We cannot, therefore, make any guarantees regarding this third-party content. Responsibility for the content 
              of linked sites lies solely with the provider or operator of the site concerned. All linked sites were checked 
              for possible violations of the law when they were linked to mine. At that time we was not aware of any content 
              which may violate the law. However, we cannot be expected to monitor the content of linked sites on an ongoing 
              basis unless we have reason to suspect a violation of the law. On becoming aware of such a violation we shall 
              remove the respective link immediately.
            </p>
            <br/>
            <h2>
              Copyright
            </h2>
            <br/>
            <p>
              We take every effort to respect the copyrights of outside parties and to employ 
              our own material and material in the public domain. All content and material on this site created by the 
              us is governed by German copyright law. Downloads and copies of this site may be made for 
              private, non-commercial use only. Reproduction, processing, distribution and any form of exploitation 
              beyond that permitted by copyright law requires the written consent of the author or creator concerned. 
              Contributions by third parties are identified as such. Should anyone become aware of a possible copyright 
              infringement, we kindly request that you inform me of such. Upon becoming aware of such a violation we will 
              remove the respective content immediately.
            </p>
            <h2>
              Privacy policy
            </h2>
            <br/>
            <p>
              The privacy policiy can be found <router-link to="privacy"> here </router-link>.
            </p>
          </v-card-text>
        </v-card>
        <br/>
      </v-col>
      <v-col v-if="false" cols="6" height="100%">

        <v-card height="100%">
          <v-card-title >
            <h3>
              Impressum
            </h3>
          </v-card-title>
          <v-card-text dense>        
            <h2>
              Angaben gemäß § 5 TMG
            </h2>
            <br/>
            <img src="../static/person_ger.png" height="110px">   
            <br/>
            <br/>
            <h2>
              Kontakt
            </h2>
            <br/>
            <img src="../static/contact.png" height="40px">   
            <br/>
            <br/>
            <h2>
              Haftungsausschluss
            </h2>
            <br/>
            <h3>
              Haftung für Inhalte
            </h3>
            <br/>
            <p>
              Die Inhalte unserer Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, 
              Vollständigkeit und Aktualität der Inhalte kann ich jedoch keine Gewähr übernehmen. 
              Als Diensteanbieter bin ich gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten 
              nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG bin ich als Diensteanbieter 
              jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu 
              überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. 
              Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen
              Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem 
              Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von 
              entsprechenden Rechtsverletzungen werde ich diese Inhalte umgehend entfernen.
            </p>
            <br/>
            <h3>
              Haftung für Links
            </h3>
            <br/>
            <p>
              Diese Webseite enthält Links zu externen Webseiten Dritter, auf deren Inhalte wir keinen Einfluss haben. 
              Deshalb können wir für Inhalte 3. keine Gewähr übernehmen. Für die Inhalte der verlinkten 
              Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten 
              wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren 
              zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche Kontrolle der verlinkten 
              Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden 
              von Rechtsverletzungen werden wir derartige Links umgehend entfernen.
            </p>
            <br/>
            <h2>
              Urheberrecht
            </h2>
            <br/>
            <p>
              Die durch der Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen 
              Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der 
              Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. 
              Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet. 
              Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter 
              beachtet. Insbesondere werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine 
              Urheberrechtsverletzung aufmerksam werden, bitten wir Sie um einen entsprechenden Hinweis. Bei Bekanntwerden 
              von Rechtsverletzungen werden wir derartige Inhalte umgehend entfernen.
            </p>
            <h2>
              Datenschutz
            </h2>
            <br/>
            <p>
              Die Datenschutzerklärung ist <router-link to="privacy"> hier </router-link> nachzulesen.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import { codemirror } from 'vue-codemirror';
  import { mapState } from 'vuex';
  import moment from 'moment';

  
  // import { GenericNode } from '@/nodes/generic'

  import axios from 'axios';
  import VueAxios from 'vue-axios';
  
  Vue.use(VueAxios, axios); 


  export default {
    layout: "dashboard",
    components: {
    },
    data: () => ({
      info: "",
    }),
    methods: {
      ok() {
      },
    },
    watch: {
      info: function (val) {
      },
    },
    computed: {
      test: function() {
      }             
    },
    created () {
    },
    mounted () {
    }

  }
</script>

<style scoped>

</style>
