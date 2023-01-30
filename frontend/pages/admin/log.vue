<template>
  <v-container fluid>
    <v-card lg12 sm12 xs12>
      <v-card-title>
        <h3>
          Log
        </h3>
      </v-card-title>

      <v-flex lg12 sm12 xs12>      
        <v-card class="zindex-repair">
            <codemirror ref="cm" v-model="log" :options="cmOptions"  class="zindex-repair" @input="logChanged"></codemirror>
        </v-card>
      </v-flex>
    </v-card>
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import VWidget from '@/components/VWidget';
  import { codemirror } from 'vue-codemirror';
  import { mapState } from 'vuex';
  import * as actionBuilder from '@/api/actionBuilder';

// require styles
  import 'codemirror/lib/codemirror.css';
  import 'codemirror/theme/material.css';
  import CodeMirror from "codemirror";

  import axios from 'axios';
  import VueAxios from 'vue-axios';

  Vue.use(VueAxios, axios);

  CodeMirror.defineMode("log", () => {
    return {
      token(stream, _state) {
        var regexDate = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]/gi
        if (
          stream.match("[INFO]")
        ) {
          stream.next();
          return "property";
        } else if (stream.match("[WARN]")) {
          stream.next();
          return "builtin";    
        } else if (stream.match("[FAIL]")) {
          stream.next();
          return "atom";    
        } else if (stream.match(regexDate)) {
          return "variable";
        } else {
          stream.next();
          return null;
        }
      }
    };
  });



  export default {
    layout: "dashboard",
    components: {
      VWidget,
      codemirror
    },
    data: () => ({
      route: 'abc',
      selectedTab: 'tab-1',
      log: 'Loading log ...',
      cmOptions: {
        // codemirror options
        tabSize: 4,
        mode: 'text/javascript',
        theme: 'material',
        readOnly: true,
        lineNumbers: true,
        line: true,
        mode: "log"       
      }
    }),
    methods: {
      pollLog (now) {
        let timeout = 2500;
        if(now == true) {
          timeout = 0;
        }

        let token = $cookies.get("user_jwt");
        let options = {};
        if (token !== null) {
          options = {
            headers: { 'X-CSRF-TOKEN': token, 'Authorization': 'Bearer ' + token },
            withCredentials: true,
            responseType: "text"
          };
        }

        let setTimeoutObject = setTimeout(() => {
          axios
            .get("/api/v1/log", options)
            .then(r => r.data)
            .then(log => {
              this.log = log;
            })
            .catch(function (error) {
            });
          this.pollLog(false);

        }, timeout);
      },
      async logChanged() {
        await new Promise(resolve => setTimeout(resolve, 50));
        this.$refs.cm.codemirror.execCommand("goDocEnd");
      }
    },    
    computed: {
      codemirror() {
        return this.$refs.cm.codemirror 
      },
    },
    created () {
    },
    mounted () {
      this.codemirror.focus();
      this.codemirror.setCursor(this.codemirror.lineCount(), 0);
      this.codemirror.setSize("auto","auto");

      
      this.pollLog(true);

   
    }

  }
</script>

<style scoped>
.zindex-repair{
    z-index:1;
}

.CodeMirror {
 /* Set height, width, borders, and global font properties here */
    font-family: monospace;
    height: auto;
}
</style>
