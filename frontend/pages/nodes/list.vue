<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>      
      <AuthorizeDialog v-model="authentification_secret" :node="selectedNode" :identification="identification" :show.sync="showAuthorizeDialog" />        
      <v-card>
        <v-card-title>
          <h3>
            Nodes
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
          :headers="nodeListHeaders"
          :items="nodeList"
          :search="search"
        >


          <template v-slot:item.status="{ item }">
            <div align="center">            
              <v-chip class="center" dark :color="item.active ? 'success' : 'error'" style="justify-content: center; min-width: 100%;">
                {{item.status}}
              </v-chip>
            </div>
          </template>

          <template v-slot:item.authorization_status="{ item }">
            <div align="center">            
              <v-chip class="center" style="justify-content: center; min-width: 100%;" :color="item.authorized ? 'success' : 'error'">
                {{item.authorization_status}}
              </v-chip>
            </div>
          </template>

          <template v-slot:item.fingerprint="{ item }">
            <div align="center">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn color="grey darken-2" fab  dark v-on="on" x-small>
                    <v-icon>fingerprint</v-icon> 
                  </v-btn>
                </template>              
                <span>{{item.fingerprint}}</span>
              </v-tooltip>
            </div>
          </template>

          <template v-slot:item.nodeclass="{ item }">
            <div align="center">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn color="grey darken-2" fab dark v-on="on" x-small>
                    <v-icon>device_hub</v-icon> 
                  </v-btn>
                </template>              
                <span>{{item.nodeclass}}</span>
              </v-tooltip>
            </div>
          </template>

          <template v-slot:item.actions="{ item }">
            <v-tooltip bottom v-if="!item.authorized">
              <template v-slot:activator="{ on }">
                <v-btn color="success"  v-on="on" @click="clickAuthorizeNode(item)" fab x-small>
                  <v-icon>mdi-checkbox-marked-circle-outline</v-icon> 
                </v-btn>
              </template>
              <span>Authorize node</span>
            </v-tooltip>
            <v-tooltip bottom v-for="action in activeActions(item)" v-bind:key="action.name">
              <template v-slot:activator="{ on }">
                <v-btn :color="action.color" v-on="on" style="margin-right: 2px;" @click="requestViewAction('nodeList', action.action, item)" :disabled="!item[action.name]" fab x-small :dark="item[action.name]">
                    <v-icon>{{action.icon}}</v-icon> 
                </v-btn>
              </template>
              <span>{{action.tooltip}}</span>
            </v-tooltip>
          </template>        
        </v-data-table>
      </v-card>    
    </v-flex>
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import * as actionBuilder from '@/api/actionBuilder';
  import * as viewParser from '@/api/viewParser';

  import { createHelpers } from 'vuex-map-fields';
  import AuthorizeDialog from '~/components/dialogs/authorizeNodeDialog'

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
      AuthorizeDialog
    },
    data: () => ({
      search: '',
      nodeListHeaders: [],
      nodeList: [],
      actions: [],
      selectedNode: {},
      showAuthorizeDialog: false,
      identification: {},
      authentification_secret: "",
    }),
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
    },
    methods: {
      activeActions(item) {
        return this.actions.filter(i => item.hasOwnProperty(i.name));
      },
      clickAuthorizeNode(item) {
        this.selectedNode = item;
        let getIdentificationAction = [actionBuilder.newExecuteDataViewActionAction('nodes', "nodeList", "getIdentification", {'id': item.id})];
        this.$store.dispatch('actions/emitActionRequest', getIdentificationAction).then(response => {
          this.identification = response;
        }, error => {
          this.dispatch('notifications/pushNotification', [error, "error"]);
          this.identification = {};
        })     
        this.showAuthorizeDialog = true;
      },
      requestViewAction(view, action, item) {
        console.log("requestViewAction", view, action, item);
        let entry = { ...item }
        this.actions.forEach(element => delete entry[element.action]);
        let dataViewAction = [actionBuilder.newExecuteDataViewActionAction('nodes', view, action, entry)];

        this.$store.dispatch('actions/emitActionRequest', dataViewAction);
        this.loading = true;
        this.loadingLocked = true;
      }
    },   
    watch: {
      viewStates(newValue, oldValue) {
        //console.log("change on viewStates detected with", newValue, oldValue);
        if(newValue['nodes/nodeList'] === 'ready')  {
          this.nodeList = viewParser.parseEntries('nodes/nodeList', this.viewDictionary);
          this.nodeListHeaders = viewParser.parseHeader('nodes/nodeList', this.viewDictionary);
          this.actions = viewParser.parseActions('nodes/nodeList', this.viewDictionary);             
        } 
      }
    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("nodes", "nodeList")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);
    }        
  }
</script>

<style scoped>

</style>
