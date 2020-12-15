<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>      
      <v-card>
        <v-card-title>
          <h3>
            Permissions
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
          :headers="headers"
          :items="users"
          :items-per-page="15"
          :loading="viewStates['permissions/permissionList'] !== 'ready'"
          :search="search"
          class="elevation-1"        
        >
          <template v-slot:item.actions="{ item }">
            <v-tooltip bottom v-for="action in actions" v-bind:key="action.name">
              <template v-slot:activator="{ on }">
                <v-btn :color="action.color" v-on="on" @click="requestViewAction('userList', action.action, item)" :disabled="!item[action.name]" fab x-small :dark="item[action.name]">
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
      loading: true,
      loadingLocked: true,
      search: '',
      headers: [],
      users: [],
      actions: [],
      lockedHeaders: [],
      lockedUsers: [],
      lockedActions: []
    }),
    methods: {
      requestViewAction(view, action, item) {
        console.log("requestViewAction", view, action, item);
        let entry = { ...item }
        this.actions.forEach(element => delete entry[element.action]);
        let dataViewAction = [actionBuilder.newExecuteDataViewActionAction('users', view, action, entry)];

        this.$store.dispatch('actions/emitActionRequest', dataViewAction);
        this.loading = true;
        this.loadingLocked = true;
      },
      parseEntries(view) {
        if(this.viewDictionary.hasOwnProperty(view)) {
          return this.viewDictionary[view].entries;
        } else {
          return [];
        }
      },
      parseActions(view) {
        let actions = [];
        if(this.viewDictionary.hasOwnProperty(view)) {        
          this.viewDictionary[view].properties.forEach(function (item, index) {
            if(item.type === 'action') {
              actions.push({ name: item.name, icon: item.icon, tooltip: item.label, action: item.action, color: item.color });
            }
          });        
          return actions;
        } else {
          return [];
        }
      },
      parseHeader(view) {
        let headers = [];
        let actionExist = false;
        if(this.viewDictionary.hasOwnProperty(view)) {
          this.viewDictionary[view].properties.forEach(function (item, index) {
            if(item.type === 'action') {
              if(actionExist === false) {
                headers.push({ text: 'Actions',  value: 'actions', tooltip: item.label, action: item.action, name: item.name });
              }
              actionExist = true;
            } else {
              headers.push({ text: item.label,  value: item.name });
            }
          });        
          return headers;
        } else {
          return [];
        }
      }
    },
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
    },
    watch: {
      viewDictionary(newValue, oldValue) {

      },
      viewStates(newValue, oldValue) {
        //console.log("change on viewStates detected with", newValue, oldValue);
        if(newValue['permissions/permissionList'] === 'ready')  {
          let entries = this.parseEntries('permissions/permissionList');
          this.users = entries;
          this.headers = this.parseHeader('permissions/permissionList');
          this.actions = this.parseActions('permissions/permissionList');
          this.loading = false;      
        } 

      }

    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("permissions", "permissionList")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);       
    }    
  }

</script>

<style scoped>

.v-btn {
  margin-right: 5px;
}

</style>
