<template>
  <v-container grid-list-xl fluid>
    <v-flex lg12 sm12 xs12>      
      <v-card>
        <v-card-title>
          <h3>
            Users
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
          :loading="viewStates['users/userList'] !== 'ready'"
          :search="search"
          class="elevation-1"        
        >
          <template v-slot:item.actions="{ item }">
            <v-tooltip bottom v-for="action in actions" v-bind:key="action.name">
              <template v-slot:activator="{ on }">
                <v-btn  v-if="item.hasOwnProperty(action.name)" :color="action.color" v-on="on" @click="requestViewAction('users', 'userList', action.action, item)" :disabled="!item[action.name]" fab x-small :dark="item[action.name]">
                    <v-icon>{{action.icon}}</v-icon>
                </v-btn>
              </template>
              <span>{{action.tooltip}}</span>
            </v-tooltip>            
          </template>
        </v-data-table>
      </v-card>
        <br>

      <v-card>
        <v-card-title>
          <h3>
            Locked users
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
          :headers="lockedHeaders"
          :items="lockedUsers"
          :items-per-page="15"
          :loading="viewStates['users/userLockedList'] !== 'ready'"
          :search="search"
          class="elevation-1"        
        >
          <template v-slot:item.actions="{ item }">
            <v-tooltip bottom v-for="action in lockedActions" v-bind:key="action.name">
              <template v-slot:activator="{ on }">
                <v-btn v-if="item.hasOwnProperty(action.name)" :color="action.color" v-on="on" @click="requestViewAction('users', 'userLockedList', action.action, item)" :disabled="!item[action.name]" fab x-small :dark="item[action.name]">
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
      requestViewAction(workspace, view, action, item) {
        let r = actionBuilder.requestViewAction(workspace, view, action, item, this.actions)
        this.$store.dispatch('actions/emitActionRequest', r);
        this.loading = true;
        this.loadingLocked = true;
      },
    },
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
    },
    watch: {
      viewStates(newValue) {
        if(newValue['users/userLockedList'] === 'loading')  {
          this.loadingLocked = true;
        }

        if(newValue['users/userList'] === 'loading')  {
          this.loading = true;
        }

        if(newValue['users/userLockedList'] === 'ready' && this.loadingLocked == true)  {
          this.lockedUsers = viewParser.parseEntries('users/userLockedList', this.viewDictionary);
          this.lockedHeaders = viewParser.parseHeader('users/userLockedList', this.viewDictionary);
          this.lockedActions = viewParser.parseActions('users/userLockedList', this.viewDictionary);
          this.loadingLocked = false;
        } 
        if(newValue['users/userList'] === 'ready' && this.loading == true)  {
          this.users =  viewParser.parseEntries('users/userList', this.viewDictionary);
          this.headers = viewParser.parseHeader('users/userList', this.viewDictionary);
          this.actions = viewParser.parseActions('users/userList', this.viewDictionary);          
          this.loading = false;
        } 

      }
    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("users", "userList")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);      
      let getLockedViewAction = [actionBuilder.newGetViewAction("users", "userLockedList")];
      this.$store.dispatch('actions/emitActionRequest', getLockedViewAction);      
    }    
  }

</script>

<style scoped>

.v-btn {
  margin-right: 5px;
}

</style>
