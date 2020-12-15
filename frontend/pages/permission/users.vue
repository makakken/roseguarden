<template>
  <v-container fluid fill-height>
    <v-row lg12 sm12 xs12>      
      <v-col cols="12" md="4">
        <v-card min-height="650px">
          <v-card-title>
            <h3>
              User
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
          
          <v-list dense single-line style="height: 100%" class="overflow-y-auto">
            <v-list-item-group
              v-model="selected"
              mandatory
              active-class="blue--text"
            >
              <template v-for="(item, index) in filteredItems">
                <v-list-item :key="item.name" @click="selectUser(item)">
                  <template v-slot:default="{ active, toggle }">
                    <v-list-item-content>
                      <v-list-item-title>{{item.name}} ({{item.email}})</v-list-item-title>
                      <v-list-item-subtitle>
                        <span v-if="item.admin" class="red--text font-weight-bold">Admin</span>
                        <span v-else class="font-weight-bold">User</span>
                        {{item.roles}}
                      </v-list-item-subtitle>
                    </v-list-item-content>

                    <v-list-item-action>

                    </v-list-item-action>
                  </template>
                </v-list-item>


              </template>
            </v-list-item-group>
          </v-list>
        </v-card>  
      </v-col>

      <v-col v-if="!isMobile" cols="12" md="8">
        <v-card min-height="100%">
          <v-card-title>
            <h3>
              {{userName}}
            </h3>
            <v-spacer></v-spacer>

          </v-card-title>
          <v-container lg12 sm12 xs12 height="100%" align="center" justify="center" class="overflow-y-auto">
            <PermissionUserView :permissionGroups="permissionGroups" :user="selectedUser" v-on:submit="submitChange"/>            
          </v-container>
        </v-card>  
      </v-col>
    </v-row>

    <v-dialog
        v-model="mobileDialog"
        fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-card width="100%">
          <v-toolbar dark color="primary">
            <v-btn icon dark @click="cancelChange()">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>{{userName}}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn small style="margin-left: 5px;" color="error" :disabled="!validSelection" @click="onRemoveGroup()">Delete</v-btn>
            <v-toolbar-items>
            </v-toolbar-items>
          </v-toolbar>
          <v-container lg12 sm12 xs12 height="100%" align="center" justify="center" class="overflow-y-auto">
            <PermissionUserView :permissionGroups="permissionGroups" :user="selectedUser" v-on:submit="submitChange" />            
          </v-container>
        </v-card>
    </v-dialog>  

  </v-container>
</template>

<script>

  import Vue from 'vue';
  import * as actionBuilder from '@/api/actionBuilder';
  import _ from 'lodash'; 
  import * as viewParser from '@/api/viewParser';
  import { createHelpers } from 'vuex-map-fields';

  import PermissionUserView from "@/components/permissions/PermissionUserView";

  import { mapState } from 'vuex';
 
  // The getter and mutation types are provided to the vue module
  // they must be the same as the function names used in the store.
  const { mapFields } = createHelpers({
    getterType: 'views/getView',
    mutationType: 'views/updateView',
  });

  export default {
    layout: "dashboard",
    components: { PermissionUserView },
    data: () => ({
      search: '', 
      loading: true,
      isMobile: false,
      mobileDialog: false,
      userName: "Please select a user",
      validSelection: false,
      permissionGroups: [],
      headers: [],
      todos: [],
      actions: [],
      selected: null,
      selectedUser: null,
      users: [],        
    }),
    methods: {
      selectUser(item) {
        this.validSelection = true;
        this.userName = item.name + '(' + item.email + ')';
        this.selectedUser = {...item};
        if(this.isMobile === true) {
          this.mobileDialog = true;
        }
      },
      onResize () {
        this.isMobile = window.innerWidth < 950;
      },
      updateDone (item) {
        console.log('Toggle', item);
      },
      submitChange() {
        console.log("submitChange", this.selectedGroup);
        let updateViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("permissions", "userList", this.selectedUser)];
        this.$store.dispatch('actions/emitActionRequest', updateViewEntryAction);
      },       
      cancelChange() {
        this.mobileDialog = false; 
        this.selectedUser = {...this.users[this.selected]};
      },         
      requestViewAction(view, action, item) {

      },   
    },   
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
      isLoading: function() {
        return this.viewStates['permissions/userList'] !== 'ready';
      },
      filteredItems() {
          return _.orderBy(this.users.filter(item => {
            if(!this.search) return this.users;
              return (item.name.toLowerCase().includes(this.search.toLowerCase()) ||
                  item.roles.toLowerCase().includes(this.search.toLowerCase())   ||
                  item.email.toLowerCase().includes(this.search.toLowerCase()));
          }), 'headline');
      }
    },
    watch: {
      viewStates(newValue, oldValue) {
        if(newValue['permissions/userList'] === 'ready')  {
          this.users = viewParser.parseEntries('permissions/userList', this.viewDictionary);
        } 
        if(newValue['permissions/groupsList'] === 'ready')  {
          this.permissionGroups = viewParser.parseEntries('permissions/groupsList', this.viewDictionary);
          console.log("this.permissions", this.permissionGroups);
        }         
      }
    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("permissions", "userList"),
      actionBuilder.newGetViewAction("permissions", "groupsList")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);
      this.onResize()
      window.addEventListener('resize', this.onResize, { passive: true })         
    }        
  }
</script>

<style scoped>


</style>
