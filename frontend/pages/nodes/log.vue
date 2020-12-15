<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>      
      <v-card>
        <v-card-title>
          <h3>
            Node log
          </h3>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :headers="nodeLogsHeaders"
          :items="nodeLogs"
          :search="search"
        ></v-data-table>
      </v-card>    
    </v-flex>
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import * as actionBuilder from '@/api/actionBuilder';
  import * as viewParser from '@/api/viewParser';

  import { createHelpers } from 'vuex-map-fields';

  import { mapState } from 'vuex';
 
  // The getter and mutation types are provided to the vue module
  // they must be the same as the function names used in the store.
  const { mapFields } = createHelpers({
    getterType: 'views/getView',
    mutationType: 'views/updateView',
  });

  export default {
    layout: "dashboard",
    components: {
    },
    data: () => ({
      search: '',
      nodeLogsHeaders: [],
      nodeLogs: []
    }),
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
    },
    watch: {
      viewDictionary(newValue, oldValue) {

      },
      viewStates(newValue, oldValue) {
        //console.log("change on viewStates detected with", newValue, oldValue);
        if(newValue['nodes/nodeLogs'] === 'ready')  {
          this.nodeLogs = viewParser.parseEntries('nodes/nodeLogs', this.viewDictionary);
          this.nodeLogsHeaders = viewParser.parseHeader('nodes/nodeLogs', this.viewDictionary);
        } 

      }
    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("nodes", "nodeLogs")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);
    }        
  }
</script>

<style scoped>

</style>