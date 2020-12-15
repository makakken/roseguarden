<template>
  <v-container fluid fill-height>
    <v-row lg12 sm12 xs12>      
      <v-col cols="12" md="3">
        <v-card min-height="100%">
          <v-card-title>
            <h3>
              Permission groups
            </h3>
            <v-spacer></v-spacer>
              <v-btn dark small color="success" @click="onAddGroup()">Add</v-btn>
          </v-card-title>
          
          <v-list dense single-line style="height: 100%" min-height="600px" class="overflow-y-auto">
            <v-list-item-group
              v-model="selected"
              mandatory
              active-class="blue--text"
            >
              <template v-for="(item, index) in groups">
                <v-list-item :key="item.id" @click="selectGroup(item)">
                  <template v-slot:default="{ active, toggle }">
                    <v-list-item-content>
                      <v-list-item-title v-text="item.name"></v-list-item-title>
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

      <v-col v-if="!isMobile" cols="12" md="9">
        <v-card min-height="100%">
          <v-card-title>
            <h3>
              {{groupName}}
            </h3>
            <v-spacer></v-spacer>
              <v-btn small style="margin-left: 5px;" color="error" :disabled="!validSelection" @click="onRemoveGroup()">Delete</v-btn>

          </v-card-title>
          <v-container lg12 sm12 xs12 style="height: 100%" class="overflow-y-auto">
            <PermissionGroupView :permissions="permissions" :group="selectedGroup" v-on:submit="submitChange"/>            
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
            <v-toolbar-title>{{groupName}}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn small style="margin-left: 5px;" color="error" :disabled="!validSelection" @click="onRemoveGroup()">Delete</v-btn>
            <v-toolbar-items>
            </v-toolbar-items>
          </v-toolbar>
          <v-container lg12 sm12 xs12 height="100%" align="center" justify="center" class="overflow-y-auto">
            <PermissionGroupView :permissions="permissions" :group="selectedGroup" v-on:submit="submitChange" />            
          </v-container>
        </v-card>
    </v-dialog>  


    <v-dialog
        v-model="newGroupDialog"
        hide-overlay
        transition="dialog-bottom-transition"
        width="90%"
      >
        <v-card>
            <v-toolbar dense dark color="primary">
              <v-toolbar-title>New group</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
              </v-toolbar-items>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                v-model="newGroupName"
                label="Group name"
                single-line
                style="padding-left: 15px; padding-right: 15px"
                hide-details
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="error" @click="newGroupDialog = false" >Cancel</v-btn>
              <v-btn color="primary" @click="requestNewGroup">Ok</v-btn>
            </v-card-actions>
          </v-card>
      </v-dialog>            
  </v-container>
</template>

<script>

  import Vue from 'vue';
  import * as actionBuilder from '@/api/actionBuilder';
  import * as viewParser from '@/api/viewParser';
  import { createHelpers } from 'vuex-map-fields';

  import PermissionGroupView from "@/components/permissions/PermissionGroupView";

  import { mapState } from 'vuex';
 
  // The getter and mutation types are provided to the vue module
  // they must be the same as the function names used in the store.
  const { mapFields } = createHelpers({
    getterType: 'views/getView',
    mutationType: 'views/updateView',
  });

  export default {
    layout: "dashboard",
    components: { PermissionGroupView },
    data: () => ({
      newGroupDialog: false,
      mobileDialog: false,
      loading: true,
      isMobile: false,
      groupName: "Please select a group",
      validSelection: false,
      groups: [],
      permissions: [],
      newGroupName: "New group",
      validSelection: false,
      selected: null,
      selectedGroup: null,
    }),
    methods: {
      selectGroup(item) {
        this.validSelection = true;
        this.selectedGroup = {...item};
        this.groupName = item.name;
        if(this.isMobile === true) {
          this.mobileDialog = true;
        }        
      },
      onResize () {
        this.isMobile = window.innerWidth < 950;
      },
      onRemoveGroup() {
        let removeViewEntryAction = [actionBuilder.newRemoveDataViewEntryAction("permissions", "groupsList", this.selectedGroup)];
        this.$store.dispatch('actions/emitActionRequest', removeViewEntryAction); 
        this.groupName = "Please select a group";
      },
      submitChange() {
        let updateViewEntryAction = [actionBuilder.newUpdateDataViewEntryAction("permissions", "groupsList", this.selectedGroup)];
        this.$store.dispatch('actions/emitActionRequest', updateViewEntryAction);  
      },       
      cancelChange() {
        this.mobileDialog = false; 
        this.selectedGroup = {...this.groups[this.selected]};
      },          
      onAddGroup() {
        this.newGroupDialog = true;
        this.newGroupName = "New permission group";
      },
      requestNewGroup() {
        let createViewEntryAction = [actionBuilder.newCreateViewAction("permissions", "groupsList", {'name' : this.newGroupName})];
        this.$store.dispatch('actions/emitActionRequest', createViewEntryAction);  
        this.newGroupDialog = false;
      },           
    },   
    computed: {
      ...mapState('views', ['viewDictionary']),
      ...mapState('views', ['viewStates']),
      isLoading: function() {
        return this.viewStates['permissions/groupsList'] !== 'ready';
      },

    },
    watch: {
      viewStates(newValue, oldValue) {
        if(newValue['permissions/groupsList'] === 'ready')  {
          this.groups = viewParser.parseEntries('permissions/groupsList', this.viewDictionary);
        } 
        if(newValue['permissions/permissionList'] === 'ready')  {
          this.permissions = viewParser.parseEntries('permissions/permissionList', this.viewDictionary);
        } 
      }
    },
    mounted () {
      let getViewAction = [actionBuilder.newGetViewAction("permissions", "groupsList"), 
                            actionBuilder.newGetViewAction("permissions", "permissionList")];
      this.$store.dispatch('actions/emitActionRequest', getViewAction);
      this.onResize()
      window.addEventListener('resize', this.onResize, { passive: true })         
    }        
  }
</script>

<style scoped>


</style>
